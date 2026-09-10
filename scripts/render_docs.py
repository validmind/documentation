#!/usr/bin/env python3
# Copyright © 2026 ValidMind Inc. All rights reserved.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""Render every Quarto input in isolated workers, preserving full project context.

Directory renders retain the full project input list (unlike changing project.render,
which breaks cross-directory navigation and listings). No output from a prior build
is reused. DOCS_RENDER_JOBS=1 selects Quarto's ordinary full-project render.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import glob
from html.parser import HTMLParser
import yaml
import filecmp
import json
import os
import re
from pathlib import Path
import shutil
import subprocess
import tempfile
import time


def defer_listing(content: str) -> str:
    """Rename listing keys only within a page's leading YAML metadata block."""
    front = re.match(
        r"\A(?:\ufeff)?---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.DOTALL
    )
    if not front:
        return content
    metadata = re.sub(r"(?m)^([ \t]*)listing:", r"\1docs-deferred-listing:", front[1])
    return content[: front.start(1)] + metadata + content[front.end(1) :]


def partition(inputs: list[str], jobs: int) -> list[list[str]]:
    """Cover each input exactly once with disjoint file/directory targets."""
    limit = max(1, (len(inputs) + jobs - 1) // jobs)
    targets: list[tuple[str, int]] = []

    def split(prefix: Path, files: list[str]) -> None:
        if prefix != Path(".") and len(files) <= limit:
            targets.append((prefix.as_posix(), len(files)))
            return
        children: dict[Path, list[str]] = {}
        for file in files:
            rel = Path(file).relative_to(prefix)
            if len(rel.parts) == 1:
                targets.append((file, 1))
            else:
                children.setdefault(prefix / rel.parts[0], []).append(file)
        for child, paths in sorted(children.items()):
            split(child, paths)

    split(Path("."), inputs)
    buckets: list[list[str]] = [[] for _ in range(jobs)]
    sizes = [0] * jobs
    for target, size in sorted(targets, key=lambda item: (-item[1], item[0])):
        index = min(range(jobs), key=lambda i: sizes[i])
        buckets[index].append(target)
        sizes[index] += size
    return [bucket for bucket in buckets if bucket]


def listing_targets(
    inputs: list[str], listings: list[str], jobs: int
) -> list[list[str]]:
    """Batch listings with nearby pages to amortize Quarto project finalization."""
    targets = {}
    for page in listings:
        target, size = page, 1
        for parent in reversed(Path(page).parents):
            if parent == Path("."):
                continue
            count = sum(p.startswith(parent.as_posix() + "/") for p in inputs)
            if count <= 160:
                target, size = parent.as_posix(), count
                break
        targets[target] = size
    buckets = [[] for _ in range(jobs)]
    sizes = [0] * jobs
    for target, size in sorted(targets.items(), key=lambda item: (-item[1], item[0])):
        index = min(range(jobs), key=lambda i: sizes[i])
        buckets[index].append(target)
        sizes[index] += size
    return buckets


def merge_outputs(outputs: list[Path], destination: Path) -> None:
    """Union indexes and require identical bytes for shared output resources."""
    indexes = {"search.json": "objectID", "listings.json": "listing"}
    for output in outputs:
        if not output.is_dir():
            raise RuntimeError(f"Missing worker output: {output}")
        for source in sorted(output.rglob("*")):
            if not source.is_file():
                continue
            relative = source.relative_to(output)
            if relative.as_posix() in indexes:
                continue
            # Quarto creates a temporary root redirect for directory renders
            # before the real index page is rendered in another worker.
            if (
                relative.as_posix() == "index.html"
                and "<title>Redirect to " in source.read_text()
                and 'http-equiv="refresh"' in source.read_text()
            ):
                continue
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                if not filecmp.cmp(source, target, shallow=False):
                    raise RuntimeError(f"Conflicting worker output: {relative}")
            else:
                shutil.copy2(source, target)
    for name, key in indexes.items():
        merged: dict[str, dict] = {}
        found = False
        for output in outputs:
            path = output / name
            if not path.exists():
                continue
            found = True
            items = json.loads(path.read_text())
            if not isinstance(items, list):
                raise ValueError(f"{path} must contain an array")
            for item in items:
                value = item.get(key)
                if not isinstance(value, str) or not value:
                    raise ValueError(f"{path}: missing {key}")
                if value in merged and merged[value] != item:
                    raise ValueError(f"Conflicting {name} entry: {value}")
                merged[value] = item
        if found:
            (destination / name).write_text(json.dumps(list(merged.values())))


def page_metadata(content: str) -> dict:
    front = re.match(
        r"\A(?:\ufeff)?---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.DOTALL
    )
    return (yaml.safe_load(front[1]) or {}) if front else {}


def independent_summary(path: Path) -> tuple[bool, bool]:
    """Whether a deferred listing page has its own paragraph/preview image."""

    class Summary(HTMLParser):
        def __init__(self):
            super().__init__()
            self.stack = []
            self.paragraph = self.image = False

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            inside = any(t == "main" for t, _ in self.stack)
            excluded = any(t in {"header", "nav"} for t, _ in self.stack)
            if inside and not excluded:
                self.paragraph |= tag == "p"
                self.image |= tag == "img"
            if tag not in {"img", "br", "hr", "input", "meta", "link", "source", "wbr"}:
                self.stack.append((tag, attrs))

        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break

    if not path.exists():
        return False, False
    summary = Summary()
    summary.feed(path.read_text())
    return summary.paragraph, summary.image


def descriptors(metadata: dict) -> list[dict]:
    listing = metadata.get("listing", [])
    return listing if isinstance(listing, list) else [listing]


def dependent_listings(
    site: Path, output: Path, metadata: dict[str, dict], listings: list[str]
) -> bool:
    """Fail back to native ordering when listing content depends on another listing."""
    members = set(listings)
    summaries = {
        p: independent_summary(output / Path(p).with_suffix(".html")) for p in listings
    }
    for page in listings:
        for listing in descriptors(metadata[page]):
            if not isinstance(listing, dict) or listing.get("template"):
                return True
            fields = listing.get("fields", ["description", "image"])
            contents = listing.get("contents", "*")
            for item in contents if isinstance(contents, list) else [contents]:
                spec = item if isinstance(item, str) else item.get("path", "")
                if spec.startswith(("https://", "http://")):
                    continue
                pattern = (
                    site / spec.lstrip("/")
                    if spec.startswith("/")
                    else site / Path(page).parent / spec
                )
                for match in glob.glob(str(pattern), recursive=True):
                    path = Path(match).resolve()
                    if path.suffix in {".yml", ".yaml"}:
                        return True  # External listing metadata may hide dependencies.
                    try:
                        relative = path.relative_to(site).as_posix()
                    except ValueError:
                        continue
                    if relative == page or relative not in members:
                        continue
                    target = {
                        **metadata[relative],
                        **(item if isinstance(item, dict) else {}),
                    }
                    paragraph, image = summaries[relative]
                    if (
                        "description" in fields
                        and not target.get("description")
                        and not paragraph
                    ):
                        return True
                    target_has_images = any(
                        not isinstance(d, dict) or "image" in d.get("fields", ["image"])
                        for d in descriptors(metadata[relative])
                    )
                    if (
                        "image" in fields
                        and not target.get("image")
                        and not image
                        and target_has_images
                    ):
                        return True
    return False


def repair_format_aliases(
    site: Path, output: Path, metadata: dict[str, dict], flags: list[str]
) -> None:
    """Quarto incremental renders prefer HTML for aliases; full renders prefer the primary format."""
    for page, meta in metadata.items():
        if (
            not meta.get("aliases")
            or not isinstance(meta.get("format"), dict)
            or len(meta["format"]) < 2
        ):
            continue
        info = json.loads(
            subprocess.check_output(
                ["quarto", "inspect", str(site / page), *flags], text=True
            )
        )
        primary = next(iter(info["formats"].values()))
        filename = primary["pandoc"].get("output-file")
        if not filename:
            raise ValueError(f"Cannot determine primary alias output for {page}")
        destination = output / Path(page).parent / filename
        for alias in primary["metadata"].get("aliases", []):
            href, _, anchor = alias.partition("#")
            if href.endswith("/") or not Path(href).suffix:
                href = href.rstrip("/") + "/index.html"
            redirect = (
                output / href.lstrip("/")
                if href.startswith("/")
                else destination.parent / href
            )
            content = redirect.read_text()
            match = re.search(r"var redirects = (.*?);", content)
            if not match:
                raise ValueError(f"Cannot update alias {redirect}")
            targets = json.loads(match[1])
            targets[anchor] = os.path.relpath(destination, redirect.parent).replace(
                os.sep, "/"
            )
            content = (
                content[: match.start(1)]
                + json.dumps(targets, separators=(",", ":"))
                + content[match.end(1) :]
            )
            redirect.write_text(content)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    parser.add_argument("--profile")
    parser.add_argument("--to")
    parser.add_argument(
        "--jobs",
        type=int,
        default=int(os.environ.get("DOCS_RENDER_JOBS", min(4, os.cpu_count() or 1))),
    )
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be positive")
    site = args.site.resolve()
    flags = ["--profile", args.profile] if args.profile else []
    render_flags = flags + (["--to", args.to] if args.to else [])
    started = time.monotonic()
    info = json.loads(
        subprocess.check_output(["quarto", "inspect", str(site), *flags], text=True)
    )
    project = info["config"]["project"]
    # Hooks may mutate sources or depend on all outputs. Preserve native semantics.
    if args.jobs == 1 or project.get("pre-render") or project.get("post-render"):
        print("Using native full-project render", flush=True)
        subprocess.run(["quarto", "render", *render_flags], cwd=site, check=True)
        return
    output_relative = Path(project["output-dir"])
    if (
        output_relative.is_absolute()
        or ".." in output_relative.parts
        or output_relative == Path(".")
    ):
        raise ValueError(
            "Parallel rendering requires an output directory inside the project"
        )
    inputs = [Path(p).relative_to(site).as_posix() for p in info["files"]["input"]]
    if not inputs:
        raise ValueError("Quarto found no render inputs")
    # This repository declares listings directly in page front matter. If listing
    # metadata is inherited, keep native full-project semantics instead.
    website = project.get("type") == "website" and args.to != "gfm"
    listing_pattern = re.compile(r"^\s*listing\s*:", re.MULTILINE)
    if website and (
        info["config"].get("website", {}).get("site-url")
        or not any(
            Path(p).parent == Path(".") and Path(p).stem == "index" for p in inputs
        )
        or any(
            listing_pattern.search(p.read_text())
            for p in site.rglob("*")
            if p.is_file()
            and p.suffix in {".yml", ".yaml"}
            and "_site" not in p.parts
            and "_source" not in p.parts
        )
    ):
        # Native sitemap generation and inherited listing metadata need a
        # complete project pass; do not silently merge partial versions.
        print("Using native full-project render", flush=True)
        subprocess.run(["quarto", "render", *render_flags], cwd=site, check=True)
        return
    listings = (
        [
            p
            for p in inputs
            if defer_listing((site / p).read_text()) != (site / p).read_text()
        ]
        if website
        else []
    )
    metadata = {p: page_metadata((site / p).read_text()) for p in inputs}
    buckets = partition(inputs, args.jobs)
    print(
        f"Rendering all {len(inputs)} inputs with {len(buckets)} isolated workers",
        flush=True,
    )
    with tempfile.TemporaryDirectory(prefix="docs-render-") as temp:
        root = Path(temp)
        workers = []
        for i in range(len(buckets)):
            worker = root / str(i) / site.name

            def ignore(directory, names):
                ignored = {
                    ".git",
                    ".quarto",
                    "_source",
                    "__pycache__",
                    ".venv",
                    "render_errors.log",
                } & set(names)
                for name in names:
                    path = Path(directory) / name
                    if (
                        path == site / output_relative
                        or path == site / "_site"
                        or path == site / "llm/_llm-output"
                    ):
                        ignored.add(name)
                return ignored

            shutil.copytree(site, worker, ignore=ignore)
            # A full root render uses the root project context for every input.
            # Directory/file CLI renders would otherwise switch into nested
            # projects such as site/llm. Disable only their copied entry configs.
            for name in ("_quarto.yml", "_quarto.yaml"):
                for config in worker.rglob(name):
                    if config.parent != worker:
                        config.unlink()
            # Preserve date:last-modified and repo metadata without copying Git objects.
            git = subprocess.run(
                ["git", "rev-parse", "--absolute-git-dir"],
                cwd=site,
                text=True,
                capture_output=True,
            )
            if git.returncode == 0:
                (worker.parent / ".git").write_text(f"gitdir: {git.stdout.strip()}\n")
            for page in listings:
                path = worker / page
                stat = path.stat()
                content = path.read_text()
                # Defer only the front-matter key; retain the body, titles,
                # navigation, and full input inventory for every worker.
                content = defer_listing(content)
                path.write_text(content)
                os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
            workers.append(worker)

        def render_worker(index: int) -> Path:
            worker = workers[index]
            log = root / f"worker-{index}.log"
            with log.open("w") as stream:
                print(
                    f"[worker {index + 1}] rendering {len(buckets[index])} targets",
                    flush=True,
                )
                result = subprocess.run(
                    [
                        "quarto",
                        "render",
                        *buckets[index],
                        "--use-freezer",
                        *render_flags,
                    ],
                    cwd=worker,
                    stdout=stream,
                    stderr=subprocess.STDOUT,
                )
                if result.returncode:
                    raise RuntimeError(f"Worker {index + 1} failed\n{log.read_text()}")
            # Keep warnings visible to the existing CI warning gate.
            print(log.read_text(), flush=True)
            return worker / output_relative

        with ThreadPoolExecutor(max_workers=len(workers)) as pool:
            outputs = list(pool.map(render_worker, range(len(workers))))
        merged = root / "merged"
        merged.mkdir()
        merge_outputs(outputs, merged)
        # Listings need all rendered descriptions and thumbnails, so finalize them
        # against the fresh union, never against a previous site's HTML.
        if listings and dependent_listings(site, merged, metadata, listings):
            print(
                "Using native full-project render for dependent listing content",
                flush=True,
            )
            subprocess.run(["quarto", "render", *render_flags], cwd=site, check=True)
            return
        if listings:
            print(
                f"Finalizing {len(listings)} listing pages against complete fresh HTML",
                flush=True,
            )

            final_buckets = listing_targets(inputs, listings, len(workers))

            def finalize(index: int) -> Path:
                worker = workers[index]
                for page in listings:
                    shutil.copy2(site / page, worker / page)
                shutil.rmtree(worker / ".quarto", ignore_errors=True)
                shutil.rmtree(worker / output_relative)
                shutil.copytree(merged, worker / output_relative)
                log = root / f"listings-{index}.log"
                with log.open("w") as stream:
                    for target in final_buckets[index]:
                        # All listings are explicitly covered. Avoid Quarto's
                        # supplemental pass repeatedly rendering other listings.
                        shutil.rmtree(worker / ".quarto/listing", ignore_errors=True)
                        result = subprocess.run(
                            [
                                "quarto",
                                "render",
                                target,
                                "--use-freezer",
                                *render_flags,
                            ],
                            cwd=worker,
                            stdout=stream,
                            stderr=subprocess.STDOUT,
                        )
                        if result.returncode:
                            raise RuntimeError(
                                f"Listing render failed\n{log.read_text()}"
                            )
                print(log.read_text(), flush=True)
                delta = root / f"listing-delta-{index}"
                delta.mkdir()
                for source in (worker / output_relative).rglob("*"):
                    if not source.is_file():
                        continue
                    relative = source.relative_to(worker / output_relative)
                    original = merged / relative
                    if original.exists() and filecmp.cmp(
                        source, original, shallow=False
                    ):
                        continue
                    target = delta / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    if relative.as_posix() in {"search.json", "listings.json"}:
                        key = (
                            "objectID" if relative.name == "search.json" else "listing"
                        )
                        base = (
                            {
                                item[key]: item
                                for item in json.loads(original.read_text())
                            }
                            if original.exists()
                            else {}
                        )
                        items = [
                            item
                            for item in json.loads(source.read_text())
                            if base.get(item[key]) != item
                        ]
                        target.write_text(json.dumps(items))
                    else:
                        shutil.copy2(source, target)
                return delta

            with ThreadPoolExecutor(max_workers=len(workers)) as pool:
                deltas = list(pool.map(finalize, range(len(workers))))
            updates = root / "listing-updates"
            updates.mkdir()
            merge_outputs(deltas, updates)
            for source in updates.rglob("*"):
                if not source.is_file():
                    continue
                relative = source.relative_to(updates)
                target = merged / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                if relative.as_posix() in {"search.json", "listings.json"}:
                    key = "objectID" if relative.name == "search.json" else "listing"
                    items = (
                        {item[key]: item for item in json.loads(target.read_text())}
                        if target.exists()
                        else {}
                    )
                    items.update(
                        {item[key]: item for item in json.loads(source.read_text())}
                    )
                    target.write_text(json.dumps(list(items.values())))
                else:
                    shutil.copy2(source, target)
        if website:
            repair_format_aliases(site, merged, metadata, flags)
        destination = site / output_relative
        if destination.exists():
            shutil.rmtree(destination)
        shutil.move(str(merged), destination)
    print(
        f"Complete render: {len(inputs)} inputs in {time.monotonic() - started:.1f}s",
        flush=True,
    )


if __name__ == "__main__":
    main()

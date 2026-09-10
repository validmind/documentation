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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("site"))
    parser.add_argument("--profile")
    parser.add_argument("--to")
    parser.add_argument(
        "--jobs",
        type=int,
        default=int(os.environ.get("DOCS_RENDER_JOBS", min(2, os.cpu_count() or 1))),
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
                for target in buckets[index]:
                    target_started = time.monotonic()
                    print(f"[worker {index + 1}] {target}", flush=True)
                    result = subprocess.run(
                        ["quarto", "render", target, "--use-freezer", *render_flags],
                        cwd=worker,
                        stdout=stream,
                        stderr=subprocess.STDOUT,
                    )
                    print(
                        f"[worker {index + 1}] finished {target} in {time.monotonic() - target_started:.1f}s",
                        flush=True,
                    )
                    if result.returncode:
                        raise RuntimeError(
                            f"Worker {index + 1} failed on {target}\n{log.read_text()}"
                        )
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
        if listings:
            final_site = workers[0]
            for page in listings:
                shutil.copy2(site / page, final_site / page)
            shutil.rmtree(final_site / ".quarto", ignore_errors=True)
            shutil.rmtree(final_site / output_relative)
            shutil.move(str(merged), final_site / output_relative)
            print(
                f"Finalizing {len(listings)} listing pages against complete fresh HTML",
                flush=True,
            )
            for target in listings:
                subprocess.run(
                    ["quarto", "render", target, "--use-freezer", *render_flags],
                    cwd=final_site,
                    check=True,
                )
            shutil.move(str(final_site / output_relative), merged)
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

#!/usr/bin/env python3
"""Generate Lighthouse preview URLs from PR diffs or sitemap depth."""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import requests

ROOT_PAGES = [
    "index.html",
    "get-started/get-started.html",
    "guide/guides.html",
    "developer/validmind-library.html",
    "support/support.html",
    "releases/all-releases.html",
    "training/training.html",
]

GLOBAL_PATTERNS = [
    "site/_quarto.yml",
    "site/_quarto-*.yml",
    "site/_variables.yml",
    "site/theme.scss",
    "site/styles.css",
    "site/_extensions/**",
]

OUTPUT_FILE_RE = re.compile(
    r"^\s*output-file:\s*[_]?([^\s#]+\.html)\s*$",
    re.MULTILINE,
)

SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def _matches_global_pattern(path: str) -> bool:
    for pattern in GLOBAL_PATTERNS:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False


def _parse_output_file(qmd_path: Path) -> str | None:
    try:
        text = qmd_path.read_text(encoding="utf-8")
    except OSError:
        return None
    match = OUTPUT_FILE_RE.search(text)
    if not match:
        return None
    name = match.group(1).lstrip("_")
    return str(qmd_path.parent.relative_to(Path("site")) / name).replace("\\", "/")


def qmd_path_to_html(path: str) -> str | None:
    """Map a site/ source path to a preview HTML path."""
    if not path.startswith("site/"):
        return None

    rel = path[len("site/") :]
    p = Path(rel)

    if p.suffix == ".qmd":
        if p.name == "index.qmd":
            return str(p.parent / "index.html").replace("\\", "/")
        return str(p.with_suffix(".html")).replace("\\", "/")

    return None


def asset_path_to_html(path: str) -> str | None:
    """Map co-located assets under site/ to their page HTML."""
    if not path.startswith("site/"):
        return None
    rel = Path(path[len("site/") :])
    if rel.suffix == ".qmd":
        return qmd_path_to_html(path)

    parent = rel.parent
    if parent == Path("."):
        return None

    site_parent = Path("site") / parent
    index_qmd = site_parent / "index.qmd"
    if index_qmd.exists():
        return str(parent / "index.html").replace("\\", "/")

    for qmd in sorted(site_parent.glob("*.qmd")):
        if qmd.name != "index.qmd":
            return str(parent / f"{qmd.stem}.html").replace("\\", "/")

    return None


def changed_file_to_html(path: str) -> list[str]:
    """Return HTML paths affected by a single changed file."""
    if _matches_global_pattern(path):
        return list(ROOT_PAGES)

    if path.endswith(".qmd"):
        html = qmd_path_to_html(path)
        if html:
            qmd_file = Path(path)
            custom = _parse_output_file(qmd_file) if qmd_file.exists() else None
            results = [html]
            if custom and custom not in results:
                results.append(custom)
            return results
        return []

    html = asset_path_to_html(path)
    return [html] if html else []


def git_changed_files(base_ref: str) -> list[str]:
    subprocess.run(
        ["git", "fetch", "origin", base_ref],
        check=True,
        capture_output=True,
    )
    result = subprocess.run(
        ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD", "--", "site/"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def urls_from_changed_files(base_ref: str) -> tuple[list[str], bool]:
    """Return sorted HTML paths and whether global fallback was used."""
    changed = git_changed_files(base_ref)
    if not changed:
        return [], False

    html_paths: set[str] = set()
    used_global_fallback = False

    for path in changed:
        if _matches_global_pattern(path):
            used_global_fallback = True
            html_paths.update(ROOT_PAGES)
            continue
        for html in changed_file_to_html(path):
            html_paths.add(html)

    if used_global_fallback:
        return sorted(ROOT_PAGES), True

    return sorted(html_paths), False


def _path_depth(html_path: str) -> int:
    path = html_path.replace(".html", "").strip("/")
    if not path or path == "index":
        return 0
    return len([s for s in path.split("/") if s])


def urls_from_sitemap(preview_base_url: str, max_depth: int) -> list[str]:
    sitemap_url = f"{preview_base_url.rstrip('/')}/sitemap.xml"
    response = requests.get(sitemap_url, timeout=60)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    urls: set[str] = set()

    for url_el in root.findall(".//sm:url", SITEMAP_NS):
        loc = url_el.find("sm:loc", SITEMAP_NS)
        if loc is None or not loc.text:
            continue
        parsed = urlparse(loc.text)
        path = parsed.path.lstrip("/")
        if not path.endswith(".html"):
            continue

        segments = path.split("/")
        pr_idx = next((i for i, s in enumerate(segments) if s == "pr_previews"), -1)
        if pr_idx >= 0 and len(segments) > pr_idx + 4:
            path = "/".join(segments[pr_idx + 4 :])

        if _path_depth(path) <= max_depth:
            urls.add(path)

    if max_depth == 0:
        return sorted(ROOT_PAGES)

    return sorted(urls)


def verify_urls(
    preview_base_url: str,
    html_paths: list[str],
    installation_user: str | None = None,
    installation_password: str | None = None,
) -> list[str]:
    """Keep only paths that return HTTP 200 on the preview."""
    base = preview_base_url.rstrip("/")
    ok: list[str] = []

    for path in html_paths:
        path = path.lstrip("/")
        url = f"{base}/{path}"
        if path.startswith("installation/") and installation_user and installation_password:
            parsed = urlparse(url)
            url = (
                f"https://{installation_user}:{installation_password}@"
                f"{parsed.netloc}{parsed.path}"
            )

        try:
            status = requests.head(
                url,
                allow_redirects=True,
                timeout=30,
                headers={"User-Agent": "Mozilla/5.0"},
            ).status_code
            if status == 405:
                status = requests.get(
                    url,
                    allow_redirects=True,
                    timeout=30,
                    headers={"User-Agent": "Mozilla/5.0"},
                ).status_code
        except requests.RequestException as exc:
            print(f"WARN: Could not reach {path}: {exc}", file=sys.stderr)
            continue

        if status == 200:
            ok.append(path)
            print(f"OK: {path}", file=sys.stderr)
        else:
            print(f"WARN: Skipping {path} (HTTP {status})", file=sys.stderr)

    return ok


def write_url_list(preview_base_url: str, html_paths: list[str], out_path: Path) -> None:
    base = preview_base_url.rstrip("/")
    lines = [f"{base}/{p.lstrip('/')}" for p in html_paths]
    out_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Lighthouse URL list")
    parser.add_argument("--mode", choices=["changed", "depth"], required=True)
    parser.add_argument("--base-ref", default="main")
    parser.add_argument("--depth", type=int, default=0, choices=[0, 1, 2])
    parser.add_argument("--preview-url", required=True)
    parser.add_argument("--output", default="lhci-urls.txt")
    parser.add_argument("--metadata", default="lighthouse-metadata.json")
    parser.add_argument(
        "--skip-file",
        help="If set and no URLs, write this path so workflow can detect skip",
    )
    args = parser.parse_args()

    metadata: dict = {
        "mode": args.mode,
        "depth": args.depth if args.mode == "depth" else None,
        "global_fallback": False,
        "skip": False,
        "paths": [],
    }

    if args.mode == "changed":
        paths, global_fallback = urls_from_changed_files(args.base_ref)
        metadata["global_fallback"] = global_fallback
    else:
        paths = urls_from_sitemap(args.preview_url, args.depth)

    if not paths:
        metadata["skip"] = True
        Path(args.metadata).write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        if args.skip_file:
            Path(args.skip_file).write_text("skip\n", encoding="utf-8")
        print("No pages to audit in this PR.", file=sys.stderr)
        return 0

    verified = verify_urls(
        args.preview_url,
        paths,
        installation_user=os.environ.get("INSTALLATION_USER"),
        installation_password=os.environ.get("INSTALLATION_PW"),
    )
    if not verified:
        print("Error: No URLs returned HTTP 200 on the preview.", file=sys.stderr)
        return 1

    metadata["paths"] = verified
    Path(args.metadata).write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    write_url_list(args.preview_url, verified, Path(args.output))
    print(f"Wrote {len(verified)} URL(s) to {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

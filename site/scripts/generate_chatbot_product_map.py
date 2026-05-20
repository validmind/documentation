#!/usr/bin/env python3
# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Refer to the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""
Generate a product-to-documentation map for the in-app chatbot (LanceDB / RAG).

Correlates frontend routes and help links with documentation pages and headings.

Usage (from documentation repo root):
    python site/scripts/generate_chatbot_product_map.py
    python site/scripts/generate_chatbot_product_map.py --frontend-root ../frontend
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


DOCS_URL_PATTERN = re.compile(
    r"(?:VALIDMIND_DOCS_URL|docs\.validmind\.ai)"
    r'[^`"\']*?'
    r'(/(?:guide|get-started|developer|faq|support|training|about|reference)[^`"\')\s#]+)'
    r"(?:#([a-zA-Z0-9_-]+))?"
)

HELP_LINK_PATTERN = re.compile(
    r"helpLink=\{?`(?:\$\{CONFIG\.VALIDMIND_DOCS_URL\}|https://docs\.validmind\.ai)"
    r'(/[^`"\')\s#]+)(?:#([a-zA-Z0-9_-]+))?`?\}?'
)

DOCUMENTATION_LINK_PATTERN = re.compile(
    r'documentationLink=\{?`(?:\$\{CONFIG\.VALIDMIND_DOCS_URL\}|https://docs\.validmind\.ai)'
    r'(/[^`"\')\s#]+)(?:#([a-zA-Z0-9_-]+))?`?\}?'
)

LINK_PROP_PATTERN = re.compile(
    r'link=\{?`(?:\$\{CONFIG\.VALIDMIND_DOCS_URL\}|https://docs\.validmind\.ai)'
    r'(/[^`"\')\s#]+)(?:#([a-zA-Z0-9_-]+))?`?\}?'
)

SETTING_GROUP_TITLE_PATTERN = re.compile(
    r'<SettingGroup\b[^>]*\btitle="([^"]+)"',
)

SETTING_LINK_PATTERN = re.compile(
    r'<SettingLink\b[^>]*\btitle="([^"]+)"[^>]*\bpath="([^"]+)"',
)

ATTR_PATTERN = re.compile(r'(\w+)=["{`]([^"`}]+)["`}]')

HEADING_PATTERN = re.compile(r"^(#{2,3})\s+(.+)$", re.MULTILINE)

SIDEBAR_PATH_PATTERN = re.compile(
    r"(?:path|documentationLink):\s*['\"](/[^'\"]+)['\"]"
)
SIDEBAR_LABEL_PATTERN = re.compile(
    r"label:\s*(?:copy\([^)]+\)|['\"]([^'\"]+)['\"])"
)

# Map settings link titles (lowercase) to likely guide doc path segments for related docs.
# Frontend help URLs that do not match published doc paths.
DOC_PATH_ALIASES: dict[str, str] = {
    "/guide/model-workflows/setting-up-model-workflows.html": (
        "/guide/workflows/setting-up-workflows.html"
    ),
}

RELATED_DOC_PREFIXES = (
    "/guide/",
    "/get-started/",
    "/support/",
    "/faq/faq-",
    "/about/contributing/",
)

RELATED_DOC_KEYWORDS: dict[str, list[str]] = {
    "workflows": ["workflows", "model-workflows"],
    "workflow": ["workflows", "model-workflows"],
    "roles": ["configuration/manage-roles", "configuration/managing-users"],
    "permissions": ["configuration/manage-permissions", "configuration/managing-users"],
    "groups": ["configuration/manage-groups", "configuration/managing-users"],
    "users": ["configuration/managing-users", "configuration/manage-users"],
    "invitation": ["configuration/managing-users", "configuration/manage-users"],
    "integrations": ["integrations", "configuration"],
    "templates": ["templates", "model-documentation"],
    "document": ["templates", "model-documentation"],
    "inventory": ["inventory", "model-inventory"],
    "finding": ["model-validation", "findings"],
    "artifact": ["model-validation", "templates"],
    "attestation": ["attestation"],
    "regulation": ["templates/customize-virtual-document-validator", "model-validation"],
    "risk": ["model-validation/manage-validation-guidelines"],
    "authentication": ["configuration/managing-your-organization"],
    "organization": ["configuration/managing-your-organization"],
    "profile": ["configuration/manage-your-profile", "configuration/personalizing-validmind"],
    "analytics": ["reporting", "monitoring"],
    "dashboard": ["configuration/customize-your-dashboard"],
}


@dataclass
class DocRef:
    path: str  # URL path like /guide/foo/bar.html
    anchor: str | None = None

    @property
    def key(self) -> str:
        return f"{self.path}#{self.anchor}" if self.anchor else self.path


@dataclass
class ProductRoute:
    path: str
    label: str
    group: str | None = None
    primary_docs: list[DocRef] = field(default_factory=list)
    related_docs: list[DocRef] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def find_repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".git").is_dir():
            return parent
    return current.parent.parent.parent


def html_path_to_qmd(site_dir: Path, doc_path: str) -> Path | None:
    """Map /guide/foo/bar.html -> site/guide/foo/bar.qmd"""
    path = doc_path.strip()
    if not path.startswith("/"):
        path = "/" + path
    if path.endswith(".html"):
        path = path[:-5]
    rel = path.lstrip("/") + ".qmd"
    candidate = site_dir / rel
    return candidate if candidate.is_file() else None


def extract_headings(qmd_path: Path, max_level: int = 3) -> list[str]:
    text = qmd_path.read_text(encoding="utf-8")
    headings: list[str] = []
    for match in HEADING_PATTERN.finditer(text):
        level = len(match.group(1))
        if level > max_level:
            continue
        title = match.group(2).strip()
        title = re.sub(r"\{[^}]*\}", "", title)
        title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
        title = re.sub(r"\s+", " ", title).strip()
        if title:
            headings.append(title)
    return headings[:12]


def parse_doc_refs_from_text(text: str) -> list[DocRef]:
    refs: list[DocRef] = []
    seen: set[str] = set()

    def add(path: str, anchor: str | None) -> None:
        if not path.endswith(".html"):
            path = path.rstrip("/") + ".html"
        path = resolve_doc_path(path)
        ref = DocRef(path=path, anchor=anchor)
        if ref.key not in seen:
            seen.add(ref.key)
            refs.append(ref)

    for pattern in (HELP_LINK_PATTERN, DOCUMENTATION_LINK_PATTERN, LINK_PROP_PATTERN):
        for m in pattern.finditer(text):
            add(m.group(1), m.group(2))

    for m in DOCS_URL_PATTERN.finditer(text):
        add(m.group(1), m.group(2))

    return refs


def resolve_doc_path(path: str) -> str:
    return DOC_PATH_ALIASES.get(path, path)


def parse_settings_index(frontend_root: Path) -> list[ProductRoute]:
    settings_file = frontend_root / "src/pages/Settings/index.tsx"
    if not settings_file.is_file():
        return []

    content = settings_file.read_text(encoding="utf-8")
    routes: list[ProductRoute] = []
    seen_paths: set[str] = set()

    group_positions = [
        (m.start(), m.group(1))
        for m in SETTING_GROUP_TITLE_PATTERN.finditer(content)
    ]

    def group_for_position(pos: int) -> str | None:
        title = None
        for gpos, gtitle in group_positions:
            if gpos <= pos:
                title = gtitle
            else:
                break
        return title

    for link_match in SETTING_LINK_PATTERN.finditer(content):
        title = link_match.group(1).strip()
        path = link_match.group(2).strip()
        if not path.startswith("/settings") or path in seen_paths:
            continue
        seen_paths.add(path)
        pos = link_match.start()
        # Group-level helpLink appears before SettingLinks in the same group.
        window_start = max(0, pos - 1200)
        window = content[window_start:pos]
        group_help = parse_doc_refs_from_text(window)
        route = ProductRoute(
            path=path,
            label=title,
            group=group_for_position(pos),
        )
        if group_help:
            route.primary_docs.extend(group_help)
        routes.append(route)

    return routes


def file_to_route_hint(file_path: Path) -> str | None:
    """Infer product route from frontend page index files only."""
    if file_path.name != "index.tsx":
        return None
    parts = file_path.parts
    if "pages" not in parts or "components" in parts:
        return None
    idx = parts.index("pages")
    rest = parts[idx + 1 :]
    if not rest:
        return None
    if rest[0] == "Settings":
        if len(rest) == 1:
            return "/settings"
        # Settings/Workflows/index.tsx -> /settings/workflows
        slug = rest[1].replace("_", "-")
        # CamelCase to kebab
        slug = re.sub(r"(?<!^)(?=[A-Z])", "-", rest[1]).lower()
        return f"/settings/{slug}"
    page = rest[0]
    kebab = re.sub(r"(?<!^)(?=[A-Z])", "-", page).lower()
    if kebab == "model-inventory" and len(rest) > 1:
        return None
    if len(rest) > 1:
        return None
    return f"/{kebab}"


def scan_frontend_doc_links(frontend_root: Path) -> dict[str, list[DocRef]]:
    """Map approximate product route -> doc refs from source files."""
    by_route: dict[str, list[DocRef]] = {}
    src = frontend_root / "src"
    if not src.is_dir():
        return by_route

    for path in list(src.rglob("*.tsx")) + list(src.rglob("*.ts")):
        if "node_modules" in path.parts or ".test." in path.name:
            continue
        if path.name != "index.tsx" and "Settings" not in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        refs = parse_doc_refs_from_text(text)
        if not refs:
            continue
        route_hint = file_to_route_hint(path)
        if route_hint:
            existing = by_route.setdefault(route_hint, [])
            seen = {r.key for r in existing}
            for ref in refs:
                if ref.key not in seen:
                    seen.add(ref.key)
                    existing.append(ref)
    return by_route


def parse_sidebar_nav(frontend_root: Path) -> list[ProductRoute]:
    sidebar_file = frontend_root / "src/components/Sidebar/index.tsx"
    if not sidebar_file.is_file():
        return []
    content = sidebar_file.read_text(encoding="utf-8")
    routes: list[ProductRoute] = []
    # Match menu item objects with path and label
    blocks = re.split(r"\{\s*key:\s*['\"]", content)
    for block in blocks[1:]:
        path_m = re.search(r"path:\s*['\"]([^'\"]+)['\"]", block)
        if not path_m:
            continue
        path = path_m.group(1)
        if not path or path == "":
            continue
        label_m = re.search(r"label:\s*(?:copy\(['\"]([^'\"]+)['\"]\)|['\"]([^'\"]+)['\"])", block)
        label = (label_m.group(1) or label_m.group(2) or path) if label_m else path
        doc_m = DOCUMENTATION_LINK_PATTERN.search(block)
        route = ProductRoute(path=path, label=label, group="Main navigation")
        if doc_m:
            route.primary_docs.append(DocRef(path=doc_m.group(1), anchor=doc_m.group(2)))
        routes.append(route)
    return routes


def collect_all_doc_qmd_paths(site_dir: Path) -> list[str]:
    """Return URL-style paths for all guide-related qmd files."""
    paths: list[str] = []
    for qmd in site_dir.rglob("*.qmd"):
        rel = qmd.relative_to(site_dir).as_posix()
        if rel.startswith(("internal/", "tests/", "notebooks/", "llm/")):
            continue
        url = "/" + rel[:-4] + ".html"
        paths.append(url)
    return paths


def is_user_facing_doc(path: str) -> bool:
    if "/_source/" in path:
        return False
    if any(part.startswith("_") for part in path.split("/") if part):
        return False
    return path.startswith(RELATED_DOC_PREFIXES)


def suggest_related_docs(route: ProductRoute, all_doc_paths: list[str]) -> list[DocRef]:
    """Suggest related documentation based on route/title keywords."""
    haystack = f"{route.path} {route.label} {route.group or ''}".lower()
    segments: set[str] = set()
    for keyword, doc_segments in RELATED_DOC_KEYWORDS.items():
        if keyword in haystack:
            segments.update(doc_segments)

    primary_paths = {d.path for d in route.primary_docs}
    related: list[DocRef] = []
    for doc_path in all_doc_paths:
        if doc_path in primary_paths or not is_user_facing_doc(doc_path):
            continue
        inner = doc_path.lower()
        if any(seg in inner for seg in segments):
            related.append(DocRef(path=doc_path))
    return related[:6]


def merge_routes(
    settings: list[ProductRoute],
    nav: list[ProductRoute],
    file_links: dict[str, list[DocRef]],
) -> dict[str, ProductRoute]:
    by_path: dict[str, ProductRoute] = {}

    def get_or_add(route: ProductRoute) -> ProductRoute:
        if route.path not in by_path:
            by_path[route.path] = route
        else:
            existing = by_path[route.path]
            if route.label and existing.label == route.path:
                existing.label = route.label
            if route.group and not existing.group:
                existing.group = route.group
        return by_path[route.path]

    settings_paths: set[str] = set()
    for route in settings:
        merged = get_or_add(route)
        settings_paths.add(route.path)
    for route in nav:
        get_or_add(route)

    for path, refs in file_links.items():
        if path in settings_paths:
            route = by_path[path]
            seen = {d.key for d in route.primary_docs}
            for ref in refs:
                if ref.key not in seen:
                    seen.add(ref.key)
                    route.primary_docs.append(ref)
            continue
        if path not in by_path:
            by_path[path] = ProductRoute(path=path, label=path, group="Main navigation")
        route = by_path[path]
        seen = {d.key for d in route.primary_docs}
        for ref in refs:
            if ref.key not in seen:
                seen.add(ref.key)
                route.primary_docs.append(ref)

    return by_path


def format_doc_line(
    ref: DocRef, site_dir: Path, llm_output_dir: Path | None
) -> str:
    qmd = html_path_to_qmd(site_dir, ref.path)
    anchor_suffix = f" (section: #{ref.anchor})" if ref.anchor else ""
    line = f"- `{ref.path}`{anchor_suffix}"
    if qmd:
        headings = extract_headings(qmd)
        if headings:
            line += f"\n  - Sections: {'; '.join(headings[:8])}"
        if llm_output_dir:
            rel_md = qmd.relative_to(site_dir).with_suffix(".md").as_posix()
            md_file = llm_output_dir / rel_md
            if not md_file.is_file():
                line += "\n  - Note: not yet in `_llm-output` (run `make render-llm`)"
    else:
        line += "\n  - Note: no matching `.qmd` source found"
    return line


def render_markdown(
    routes: dict[str, ProductRoute],
    site_dir: Path,
    all_doc_paths: list[str],
    llm_output_dir: Path | None,
) -> str:
    lines = [
        "# ValidMind product-to-documentation map",
        "",
        "> Auto-generated. Maps in-product routes to documentation URLs and key sections.",
        "> For how documentation is organized by topic, see `AGENTS.md` and",
        "> [Using the documentation](/about/contributing/using-the-documentation.html).",
        "",
    ]

    settings_routes = sorted(
        (r for r in routes.values() if r.path.startswith("/settings")),
        key=lambda r: r.path,
    )
    other_routes = sorted(
        (r for r in routes.values() if not r.path.startswith("/settings")),
        key=lambda r: r.path,
    )

    def render_section(title: str, section_routes: list[ProductRoute]) -> None:
        if not section_routes:
            return
        lines.append(f"## {title}")
        lines.append("")
        current_group: str | None = None
        for route in section_routes:
            if title == "Settings" and route.group and route.group != current_group:
                current_group = route.group
                lines.append(f"### {current_group}")
                lines.append("")
            lines.append(f"#### `{route.path}` — {route.label}")
            lines.append("")
            if not route.primary_docs:
                related = suggest_related_docs(route, all_doc_paths)
                if related:
                    route.related_docs = related
                    route.notes.append(
                        "No direct help link in frontend; related docs inferred from keywords."
                    )
                else:
                    route.notes.append(
                        "No direct help link; content may be covered under scattered guide sections."
                    )
            if route.primary_docs:
                lines.append("**Docs (primary):**")
                lines.append("")
                for ref in route.primary_docs:
                    lines.append(format_doc_line(ref, site_dir, llm_output_dir))
                lines.append("")
            related = route.related_docs or suggest_related_docs(route, all_doc_paths)
            # Exclude primary from related
            primary_keys = {d.path for d in route.primary_docs}
            related = [r for r in related if r.path not in primary_keys]
            if related:
                lines.append("**Docs (related):**")
                lines.append("")
                for ref in related[:6]:
                    lines.append(format_doc_line(ref, site_dir, llm_output_dir))
                lines.append("")
            for note in route.notes:
                lines.append(f"- *{note}*")
            if route.notes:
                lines.append("")

    render_section("Settings", settings_routes)
    render_section("Main application", other_routes)

    lines.append("## Documentation index (human-oriented)")
    lines.append("")
    lines.append(
        "See `AGENTS.md` and `about/contributing/using-the-documentation.md` in the "
        "LLM corpus for guides organized by feature area (Configuration, Workflows, "
        "Inventory, etc.)."
    )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate chatbot product-to-docs map")
    parser.add_argument(
        "--frontend-root",
        type=Path,
        default=None,
        help="Path to validmind/frontend (default: <repo>/../frontend)",
    )
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=None,
        help="Path to documentation site/ (default: <repo>/site)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output markdown path (default: site/llm/chatbot-product-map.md)",
    )
    parser.add_argument(
        "--json-output",
        type=Path,
        default=None,
        help="Optional JSON output path",
    )
    args = parser.parse_args()

    repo_root = find_repo_root()
    site_dir = (args.site_dir or repo_root / "site").resolve()
    frontend_root = (args.frontend_root or repo_root / "frontend").resolve()
    if not frontend_root.is_dir():
        frontend_root = (repo_root.parent / "frontend").resolve()
    output_path = (args.output or site_dir / "llm/chatbot-product-map.md").resolve()
    llm_output = site_dir / "llm/_llm-output"

    if not frontend_root.is_dir():
        raise SystemExit(f"Frontend root not found: {frontend_root}")

    settings = parse_settings_index(frontend_root)
    nav = parse_sidebar_nav(frontend_root)
    file_links = scan_frontend_doc_links(frontend_root)
    routes = merge_routes(settings, nav, file_links)
    all_doc_paths = collect_all_doc_qmd_paths(site_dir)

    md = render_markdown(routes, site_dir, all_doc_paths, llm_output if llm_output.is_dir() else None)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md, encoding="utf-8")
    print(f"Wrote {output_path} ({len(routes)} routes)")

    if args.json_output:
        payload = {
            path: {
                "label": r.label,
                "group": r.group,
                "primary_docs": [{"path": d.path, "anchor": d.anchor} for d in r.primary_docs],
                "related_docs": [{"path": d.path, "anchor": d.anchor} for d in r.related_docs],
                "notes": r.notes,
            }
            for path, r in sorted(routes.items())
        }
        args.json_output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Wrote {args.json_output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

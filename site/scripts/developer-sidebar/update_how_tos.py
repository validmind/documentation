# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Refer to the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""
Update developer/_sidebar.yaml and developer/how-to/feature-overview.qmd
so that each subdirectory of notebooks/how_to/ (excluding tests/) is listed
explicitly in alphabetical order, with fixed capitalization where needed.

Run from the site/ directory, e.g.:
    cd site && python scripts/developer-sidebar/update_how_tos.py
"""

import os
import re
from pathlib import Path


# Display title for directories that need fixed capitalization (e.g. acronyms)
SPECIAL_TITLES = {
    "data_and_datasets": "Data and datasets",
    "tests": "Testing",
}

# Subdirectories to exclude from the sidebar only (tests has its own
# dedicated section in the sidebar already).
SIDEBAR_EXCLUDED_DIRS = {"tests"}

# Directories whose notebooks live in nested subdirectories and need a
# recursive glob (**/*.ipynb) instead of a flat one (*.ipynb).
RECURSIVE_GLOB_DIRS = {"tests"}


def dir_to_title(dirname: str) -> str:
    """Convert directory name to display title (sentence-style capitalization)."""
    if dirname in SPECIAL_TITLES:
        return SPECIAL_TITLES[dirname]
    return dirname.replace("_", " ").capitalize()


def dir_to_listing_id(dirname: str) -> str:
    """Convert a directory name to a listing id (hyphens instead of underscores)."""
    return dirname.replace("_", "-")


def update_sidebar(base: Path, subdirs: list) -> None:
    """Update developer/_sidebar.yaml with how-to subdirectories."""
    sidebar_path = base / "developer" / "_sidebar.yaml"

    if not sidebar_path.is_file():
        raise SystemExit(f"Sidebar file not found: {sidebar_path}")

    # Build the new contents block (YAML). Use "section" so Quarto renders
    # expandable accordion items; "text" alone does not expand.
    lines = [
        "          contents:",
    ]
    for d in subdirs:
        title = dir_to_title(d)
        lines.append(f'            - section: "{title}"')
        lines.append(f'              contents: "notebooks/how_to/{d}/**/*.ipynb"')

    new_block = "\n".join(lines)

    text = sidebar_path.read_text()

    # Try to find and replace an existing expanded contents block under
    # "Use library features" (re-run case).
    pattern = re.compile(
        r'(        - text: "Use library features"\n'
        r"          file: developer/how-to/feature-overview\.qmd\n)"
        r"          contents:\n"
        r'(            - (?:text|section): "[^"]+"\n'
        r'              contents: "notebooks/how_to/[^"]+\*\*(?:/\*\.ipynb)?"\n)*',
        re.MULTILINE,
    )
    match = pattern.search(text)
    if match:
        # Replace existing contents block, keeping the header lines.
        text = (
            text[: match.start()]
            + match.group(1)
            + new_block
            + "\n"
            + text[match.end() :]
        )
    else:
        # First run: insert contents block right after the file: line.
        insert_pattern = re.compile(
            r'(        - text: "Use library features"\n'
            r"          file: developer/how-to/feature-overview\.qmd\n)",
            re.MULTILINE,
        )
        insert_match = insert_pattern.search(text)
        if not insert_match:
            raise SystemExit(
                'Could not find "Use library features" entry in sidebar. '
                "Has the sidebar format changed?"
            )
        text = (
            text[: insert_match.end()]
            + new_block
            + "\n"
            + text[insert_match.end() :]
        )

    sidebar_path.write_text(text)
    print(f"Updated {sidebar_path} with {len(subdirs)} how-to directories.")


def _split_frontmatter(text: str):
    """Split a .qmd file into (frontmatter_lines, body) at the closing ---."""
    lines = text.split("\n")
    # First line must be ---
    if not lines or lines[0].strip() != "---":
        raise SystemExit("File does not start with YAML front matter (---).")
    # Find the closing ---
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            frontmatter = lines[: i + 1]  # includes both --- delimiters
            body = "\n".join(lines[i + 1 :])
            return frontmatter, body
    raise SystemExit("Could not find closing --- for YAML front matter.")


def update_feature_overview(base: Path, subdirs: list) -> None:
    """Update feature-overview.qmd with listings and panel tabset
    for each how-to subdirectory."""
    page_path = base / "developer" / "how-to" / "feature-overview.qmd"

    if not page_path.is_file():
        raise SystemExit(f"Feature overview page not found: {page_path}")

    text = page_path.read_text()

    # --- Build new listing YAML lines ---
    listing_lines = ["listing:"]
    for d in subdirs:
        listing_id = dir_to_listing_id(d)
        glob = "**/*.ipynb" if d in RECURSIVE_GLOB_DIRS else "*.ipynb"
        listing_lines.append(f"  - id: {listing_id}")
        listing_lines.append(f"    type: grid")
        listing_lines.append(f"    grid-columns: 2")
        listing_lines.append(f'    image-placeholder: "jupyter-logo-rectangle.svg"')
        listing_lines.append(f"    max-description-length: 350")
        listing_lines.append(f'    image-height: "100%"')
        listing_lines.append(f"    fields: [title, description, reading-time]")
        listing_lines.append(f'    contents: "../../notebooks/how_to/{d}/{glob}"')

    # --- Update YAML front matter ---
    frontmatter, body = _split_frontmatter(text)

    # Remove any existing listing: block from the front matter
    fm_text = "\n".join(frontmatter)
    fm_text = re.sub(r"\nlisting:\n(?:[ ].*\n)*", "\n", fm_text)

    # Re-split so we can insert the listing block before the closing ---
    fm_lines = fm_text.split("\n")
    # The last element should be ---
    closing = fm_lines.pop()  # remove closing ---
    fm_lines.extend(listing_lines)
    fm_lines.append(closing)

    # --- Build new panel-tabset block ---
    tabset_lines = ["## How-to guides by topic", "", ":::{.panel-tabset}", ""]
    for d in subdirs:
        listing_id = dir_to_listing_id(d)
        title = dir_to_title(d)
        tabset_lines.append(f"## {title}")
        tabset_lines.append("")
        tabset_lines.append(f":::{{#{listing_id}}}")
        tabset_lines.append(":::")
        tabset_lines.append("")
    tabset_lines.append(":::")
    tabset_lines.append("")

    new_tabset = "\n".join(tabset_lines)

    # Replace everything from "## How-to guides by topic" to end of body.
    feature_pattern = re.compile(
        r"## How-to guides by topic\n?.*", re.DOTALL
    )
    if feature_pattern.search(body):
        body = feature_pattern.sub(new_tabset, body)
    else:
        # Heading not found; append the tabset at the end
        body = body.rstrip("\n") + "\n\n" + new_tabset

    # --- Reassemble and write ---
    result = "\n".join(fm_lines) + "\n" + body
    page_path.write_text(result)
    print(f"Updated {page_path} with {len(subdirs)} how-to listings.")


def main() -> None:
    # Run from site/ or repo root
    cwd = Path.cwd()
    if (cwd / "notebooks" / "how_to").is_dir():
        base = cwd
    elif (cwd / "site" / "notebooks" / "how_to").is_dir():
        base = cwd / "site"
    else:
        raise SystemExit(
            "Run from site/ or repo root "
            "(e.g. cd site && python scripts/developer-sidebar/update_how_tos.py)"
        )
    how_to = base / "notebooks" / "how_to"

    all_subdirs = sorted(
        d for d in os.listdir(how_to) if (how_to / d).is_dir()
    )

    # Sidebar excludes tests (it has its own dedicated section).
    sidebar_subdirs = [d for d in all_subdirs if d not in SIDEBAR_EXCLUDED_DIRS]

    # Feature overview includes all dirs, with tests listed first.
    overview_subdirs = [d for d in all_subdirs if d in SIDEBAR_EXCLUDED_DIRS] + [
        d for d in all_subdirs if d not in SIDEBAR_EXCLUDED_DIRS
    ]

    update_sidebar(base, sidebar_subdirs)
    update_feature_overview(base, overview_subdirs)


if __name__ == "__main__":
    main()

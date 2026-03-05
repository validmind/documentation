# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Refer to the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""
Update developer/_sidebar.yaml and developer/samples-jupyter-notebooks.qmd
so that each subdirectory of notebooks/use_cases/ is listed explicitly
in alphabetical order, with fixed capitalization for NLP and LLM.

Run from the site/ directory, e.g.:
    cd site && python scripts/developer-sidebar/update_use_cases.py
"""

import os
import re
from pathlib import Path


# Display title for directories that need fixed capitalization (e.g. acronyms)
SPECIAL_TITLES = {
    "nlp_and_llm": "NLP and LLM",
}


def dir_to_title(dirname: str) -> str:
    """Convert directory name to sidebar display title (sentence-style capitalization)."""
    if dirname in SPECIAL_TITLES:
        return SPECIAL_TITLES[dirname]
    return dirname.replace("_", " ").capitalize()


def dir_to_listing_id(dirname: str) -> str:
    """Convert a directory name to a listing id (hyphens instead of underscores)."""
    return dirname.replace("_", "-")


def _has_notebooks(directory: Path) -> bool:
    """Check if a directory directly contains .ipynb files."""
    return any(
        f.endswith(".ipynb")
        for f in os.listdir(directory)
        if (directory / f).is_file()
    )


def _has_notebooks_recursive(directory: Path) -> bool:
    """Check if a directory or any of its descendants contains .ipynb files."""
    for _root, _dirs, files in os.walk(directory):
        if any(f.endswith(".ipynb") for f in files):
            return True
    return False


def _build_section_yaml(
    use_cases_base: Path, rel_path: str, dirname: str, indent: int
) -> list[str]:
    """Build YAML lines for a use-case section, nesting subdirectories.

    If the directory has subdirectories that contain notebooks, each one
    becomes a nested ``section`` (recursively).  Subdirectories without any
    notebooks are ignored.  Top-level notebooks within the directory are
    included via a non-recursive glob (``*.ipynb``).  Leaf directories use a
    recursive glob (``**/*.ipynb``) for simplicity.
    """
    full_path = use_cases_base / rel_path
    subdirs = sorted(
        d
        for d in os.listdir(full_path)
        if (full_path / d).is_dir() and _has_notebooks_recursive(full_path / d)
    )

    prefix = " " * indent
    title = dir_to_title(dirname)
    lines = [f'{prefix}- section: "{title}"']

    if not subdirs:
        # Leaf directory — simple recursive glob.
        lines.append(f'{prefix}  contents: "notebooks/use_cases/{rel_path}/**/*.ipynb"')
    else:
        # Has subdirectories — build an explicit contents list.
        lines.append(f"{prefix}  contents:")

        # List top-level notebooks explicitly (bare glob strings in a YAML
        # list are not resolved by Quarto).
        for nb in sorted(
            f for f in os.listdir(full_path)
            if f.endswith(".ipynb") and (full_path / f).is_file()
        ):
            lines.append(f"{prefix}    - notebooks/use_cases/{rel_path}/{nb}")

        # Recurse into each subdirectory.
        for subdir in subdirs:
            sub_rel = f"{rel_path}/{subdir}"
            lines.extend(
                _build_section_yaml(use_cases_base, sub_rel, subdir, indent + 4)
            )

    return lines


def update_sidebar(base: Path, subdirs: list) -> None:
    """Update developer/_sidebar.yaml with use case subdirectories."""
    sidebar_path = base / "developer" / "_sidebar.yaml"

    if not sidebar_path.is_file():
        raise SystemExit(f"Sidebar file not found: {sidebar_path}")

    use_cases_base = base / "notebooks" / "use_cases"

    # Build the new contents block (YAML). Use "section" so Quarto renders
    # expandable accordion items; "text" alone does not expand.
    lines = ["          contents:"]
    for d in subdirs:
        lines.extend(_build_section_yaml(use_cases_base, d, d, 12))

    new_block = "\n".join(lines)

    text = sidebar_path.read_text()
    # Replace either the single wildcard or an existing expanded block.
    # Accept both the old "code_samples" and the new "use_cases" paths so the
    # script works on first migration as well as on subsequent re-runs.
    old_single_use_cases = '          contents: "notebooks/use_cases/**"'
    old_single_code_samples = '          contents: "notebooks/code_samples/**"'
    if old_single_use_cases in text:
        text = text.replace(old_single_use_cases, new_block, 1)
    elif old_single_code_samples in text:
        text = text.replace(old_single_code_samples, new_block, 1)
    else:
        # Find the contents block and replace it (multi-line).  Match the
        # header lines then consume all indented content lines (12+ spaces).
        pattern = re.compile(
            r'(        - text: "(?:Code samples|Use cases)"\n'
            r"          file: developer/samples-jupyter-notebooks\.qmd\n)"
            r"          contents:\n"
            r"(?:[ ]{12,}[^\n]*\n)*",
            re.MULTILINE,
        )
        match = pattern.search(text)
        if not match:
            raise SystemExit(
                "Could not find Code samples / Use cases contents block in sidebar. "
                "Has the sidebar format changed?"
            )
        text = text[: match.start()] + match.group(1) + new_block + "\n" + text[match.end() :]
    sidebar_path.write_text(text)
    print(f"Updated {sidebar_path} with {len(subdirs)} use case directories.")


def update_notebooks_page(base: Path, subdirs: list) -> None:
    """Update samples-jupyter-notebooks.qmd with listings and panel tabset
    for each use case subdirectory."""
    page_path = base / "developer" / "samples-jupyter-notebooks.qmd"

    if not page_path.is_file():
        raise SystemExit(f"Notebooks page not found: {page_path}")

    text = page_path.read_text()

    # --- Build new listing YAML block ---
    listing_lines = ["listing:"]
    for d in subdirs:
        listing_id = dir_to_listing_id(d)
        listing_lines.append(f"  - id: {listing_id}")
        listing_lines.append(f'    type: grid')
        listing_lines.append(f'    grid-columns: 2')
        listing_lines.append(f'    image-placeholder: "jupyter-logo-rectangle.svg"')
        listing_lines.append(f'    max-description-length: 350')
        listing_lines.append(f'    image-height: "100%"')
        listing_lines.append(f'    fields: [title, description, reading-time]')
        listing_lines.append(f'    contents: "../notebooks/use_cases/{d}/*.ipynb"')

    new_listing_block = "\n".join(listing_lines) + "\n"

    # Replace the listing block in the YAML frontmatter.
    # Match "listing:" at the start of a line and all following indented lines.
    listing_pattern = re.compile(
        r'^listing:\n(?:[ ].*\n)*',
        re.MULTILINE,
    )
    text = listing_pattern.sub(new_listing_block, text, count=1)

    # --- Build new panel-tabset block ---
    tabset_lines = ["## By use case", "", ":::{.panel-tabset}", ""]
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

    # Replace everything from "## By use case" to end of file.
    use_case_pattern = re.compile(r'^## By use case\n.*', re.MULTILINE | re.DOTALL)
    text = use_case_pattern.sub(new_tabset, text)

    page_path.write_text(text)
    print(f"Updated {page_path} with {len(subdirs)} use case listings.")


def main() -> None:
    # Run from site/ or repo root
    cwd = Path.cwd()
    if (cwd / "notebooks" / "use_cases").is_dir():
        base = cwd
    elif (cwd / "site" / "notebooks" / "use_cases").is_dir():
        base = cwd / "site"
    else:
        raise SystemExit(
            "Run from site/ or repo root "
            "(e.g. cd site && python scripts/developer-sidebar/update_use_cases.py)"
        )
    use_cases = base / "notebooks" / "use_cases"

    subdirs = sorted(
        d for d in os.listdir(use_cases)
        if (use_cases / d).is_dir()
    )

    update_sidebar(base, subdirs)
    update_notebooks_page(base, subdirs)


if __name__ == "__main__":
    main()

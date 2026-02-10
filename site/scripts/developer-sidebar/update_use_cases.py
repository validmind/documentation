# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Refer to the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""
Update developer/_sidebar.yaml so the Use cases entry lists each
subdirectory of notebooks/use_cases/ explicitly (with wildcards),
in alphabetical order, with fixed capitalization for NLP and LLM.

Run from the site/ directory, e.g.:
    cd site && python scripts/developer-sidebar/update_use_cases.py
"""

import os
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


def main() -> None:
    # Run from site/ or repo root
    cwd = Path.cwd()
    if (cwd / "notebooks" / "use_cases").is_dir():
        base = cwd
    elif (cwd / "site" / "notebooks" / "use_cases").is_dir():
        base = cwd / "site"
    else:
        raise SystemExit("Run from site/ or repo root (e.g. cd site && python scripts/developer-sidebar/update_use_cases.py)")
    use_cases = base / "notebooks" / "use_cases"
    sidebar_path = base / "developer" / "_sidebar.yaml"

    if not use_cases.is_dir():
        raise SystemExit(f"Directory not found: {use_cases}")
    if not sidebar_path.is_file():
        raise SystemExit(f"Sidebar file not found: {sidebar_path}")

    subdirs = sorted(
        d for d in os.listdir(use_cases)
        if (use_cases / d).is_dir()
    )

    # Build the new contents block (YAML). Use "section" so Quarto renders
    # expandable accordion items; "text" alone does not expand.
    lines = [
        '          contents:',
    ]
    for d in subdirs:
        title = dir_to_title(d)
        lines.append(f'            - section: "{title}"')
        lines.append(f'              contents: "notebooks/use_cases/{d}/**"')

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
        # Find the contents block and replace it (multi-line).
        # Match either "Code samples" or "Use cases" as the heading text,
        # and either code_samples or use_cases in the notebook paths.
        import re
        pattern = re.compile(
            r'(        - text: "(?:Code samples|Use cases)"\n'
            r'          file: developer/samples-jupyter-notebooks\.qmd\n)'
            r'          contents:\n'
            r'(            - (?:text|section): "[^"]+"\n'
            r'              contents: "notebooks/(?:code_samples|use_cases)/[^"]+\*\*"\n)*',
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


if __name__ == "__main__":
    main()

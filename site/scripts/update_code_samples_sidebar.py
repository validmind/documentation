# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Refer to the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""
Update developer/_sidebar.yaml so the Code samples entry lists each
subdirectory of notebooks/code_samples/ explicitly (with wildcards),
in alphabetical order, with fixed capitalization for NLP and LLM.

Run from the site/ directory, e.g.:
    cd site && python scripts/update_code_samples_sidebar.py
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
    if (cwd / "notebooks" / "code_samples").is_dir():
        base = cwd
    elif (cwd / "site" / "notebooks" / "code_samples").is_dir():
        base = cwd / "site"
    else:
        raise SystemExit("Run from site/ or repo root (e.g. cd site && python scripts/update_code_samples_sidebar.py)")
    code_samples = base / "notebooks" / "code_samples"
    sidebar_path = base / "developer" / "_sidebar.yaml"

    if not code_samples.is_dir():
        raise SystemExit(f"Directory not found: {code_samples}")
    if not sidebar_path.is_file():
        raise SystemExit(f"Sidebar file not found: {sidebar_path}")

    subdirs = sorted(
        d for d in os.listdir(code_samples)
        if (code_samples / d).is_dir()
    )

    # Build the new contents block (YAML). Use "section" so Quarto renders
    # expandable accordion items; "text" alone does not expand.
    lines = [
        '          contents:',
    ]
    for d in subdirs:
        title = dir_to_title(d)
        lines.append(f'            - section: "{title}"')
        lines.append(f'              contents: "notebooks/code_samples/{d}/**"')

    new_block = "\n".join(lines)

    text = sidebar_path.read_text()
    # Replace either the single wildcard or an existing expanded block
    old_single = '          contents: "notebooks/code_samples/**"'
    if old_single in text:
        text = text.replace(old_single, new_block, 1)
    else:
        # Find the code_samples contents block and replace it (multi-line)
        import re
        # Match from "          contents:" through all following lines that are
        # "            - ..." or "              contents: ..." for code_samples
        pattern = re.compile(
            r'(        - text: "Code samples"\n'
            r'          file: developer/samples-jupyter-notebooks\.qmd\n)'
            r'          contents:\n'
            r'(            - (?:text|section): "[^"]+"\n'
            r'              contents: "notebooks/code_samples/[^"]+\*\*"\n)*',
            re.MULTILINE,
        )
        match = pattern.search(text)
        if not match:
            raise SystemExit(
                "Could not find Code samples contents block in sidebar. "
                "Has the sidebar format changed?"
            )
        text = text[: match.start()] + match.group(1) + new_block + "\n" + text[match.end() :]
    sidebar_path.write_text(text)
    print(f"Updated {sidebar_path} with {len(subdirs)} code sample directories.")


if __name__ == "__main__":
    main()

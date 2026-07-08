#!/usr/bin/env python3
# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Refer to the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""
Generate template schema documentation from backend JSON Schema.

Uses json-schema-for-humans to generate HTML documentation from the
template schema used to validate YAML documentation templates.

Usage:
    pip install json-schema-for-humans
    python scripts/generate_template_schema_docs.py

    # Or with custom backend path:
    BACKEND_ROOT=/path/to/backend python scripts/generate_template_schema_docs.py

Requirements:
    - Backend repo must be cloned (default: ../backend/, or set BACKEND_ROOT)
    - json-schema-for-humans package installed
"""
import os
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
BACKEND_ROOT = Path(os.environ.get("BACKEND_ROOT", REPO_ROOT.parent / "backend"))

SCHEMA_FILE = BACKEND_ROOT / "src/backend/templates/documentation/model_documentation/mdd_template_schema_v5_ui.json"
TARGET_FILE = REPO_ROOT / "site/guide/templates/_template-schema-generated.qmd"
EMBED_SCRIPT = "/guide/templates/schema_doc-embed.js"

# Minimum expected file size in bytes (sanity check for valid output)
MIN_OUTPUT_SIZE = 40000


def strip_global_assets(html_content: str) -> str:
    """Remove CSS/JS that pollutes the Quarto page or is replaced by embed script."""
    patterns = [
        r'<link[^>]*href="https://stackpath\.bootstrapcdn\.com/bootstrap/[^"]*"[^>]*>',
        r'<link[^>]*href="https://fonts\.googleapis\.com/css\?family=Overpass[^"]*"[^>]*>',
        r'<script[^>]*src="https://use\.fontawesome\.com/[^"]*"[^>]*></script>',
        r'<link[^>]*href="schema_doc\.css"[^>]*>',
        r'<script[^>]*src="https://code\.jquery\.com/jquery[^"]*"[^>]*></script>',
        r'<script[^>]*src="https://stackpath\.bootstrapcdn\.com/bootstrap/[^"]*"[^>]*></script>',
        r'<script[^>]*src="schema_doc\.min\.js"[^>]*></script>',
        r'\s*<title>[^<]*</title>\s*',
        r'<h1>[^<]*</h1>',
    ]
    for pattern in patterns:
        html_content = re.sub(pattern, '', html_content)
    return re.sub(r'\n{3,}', '\n\n', html_content)


def scope_collapse_selectors(html_content: str) -> str:
    """Scope Expand/Collapse all buttons to the schema wrapper."""
    return html_content.replace(
        'data-target=".collapse:not(.show)"',
        'data-target=".template-schema-docs .collapse:not(.show)"',
    ).replace(
        'data-target=".collapse.show"',
        'data-target=".template-schema-docs .collapse.show"',
    )


def extract_body_inner(html_content: str) -> str:
    """Extract inner HTML from the generated document body."""
    body_match = re.search(r'<body[^>]*>(.*)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if not body_match:
        raise ValueError("Generated HTML does not contain a <body> element")
    return body_match.group(1).strip()


def build_fragment(body_inner: str) -> str:
    """Wrap schema markup in a scoped container and attach the embed script."""
    body_inner = scope_collapse_selectors(body_inner)
    # Drop legacy wrapper if a previous generator pass already added it.
    if body_inner.startswith('<div class="template-schema-docs">'):
        body_inner = re.sub(
            r'^<div class="template-schema-docs">\s*',
            '',
            body_inner,
            count=1,
        )
        if body_inner.endswith('</div>'):
            body_inner = body_inner[:-6].rstrip()

    return (
        f'<div class="template-schema-docs">\n'
        f'{body_inner}\n'
        f'</div>\n'
        f'<script src="{EMBED_SCRIPT}"></script>'
    )


def main():
    # Verify schema file exists
    if not SCHEMA_FILE.exists():
        print(f"Error: Schema file not found: {SCHEMA_FILE}")
        print("Make sure the backend repo is cloned at ../backend/ or set BACKEND_ROOT")
        sys.exit(1)

    # Check if json-schema-for-humans is installed
    try:
        subprocess.run(
            ["generate-schema-doc", "--help"],
            capture_output=True,
            check=True
        )
    except FileNotFoundError:
        print("Error: json-schema-for-humans not installed")
        print("Install with: pip install json-schema-for-humans")
        sys.exit(1)

    # Generate HTML documentation
    print(f"Generating schema documentation from {SCHEMA_FILE}")

    temp_output = TARGET_FILE.with_suffix(".tmp.html")

    subprocess.run([
        "generate-schema-doc",
        "--config", "expand_buttons=true",
        str(SCHEMA_FILE),
        str(temp_output)
    ], check=True)

    with open(temp_output, "r") as f:
        html_content = f.read()

    html_content = strip_global_assets(html_content)
    body_inner = extract_body_inner(html_content)
    fragment = build_fragment(body_inner).strip()

    output_content = f"""<!-- Copyright © 2023-2026 ValidMind Inc. All rights reserved.
Refer to the LICENSE file in the root of this repository for details.
SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

This file is auto-generated by scripts/generate_template_schema_docs.py
Do not edit directly. Re-run the script to update.

Source: {SCHEMA_FILE.relative_to(BACKEND_ROOT.parent)}
-->

```{{=html}}
{fragment}
```
"""

    if len(output_content) < MIN_OUTPUT_SIZE:
        print(f"Error: Generated output is too small ({len(output_content)} bytes)")
        print("This likely indicates a generation failure.")
        temp_output.unlink(missing_ok=True)
        sys.exit(1)

    if 'class="template-schema-docs"' not in fragment:
        print("Error: Generated output does not contain template-schema-docs wrapper")
        temp_output.unlink(missing_ok=True)
        sys.exit(1)

    TARGET_FILE.write_text(output_content)
    temp_output.unlink()

    print(f"Generated template schema documentation: {TARGET_FILE}")
    print(f"Output size: {len(output_content)} bytes")


if __name__ == "__main__":
    main()

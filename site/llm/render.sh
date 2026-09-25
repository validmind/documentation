#!/usr/bin/env bash
# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Renders site .qmd files to plain Markdown for LLM / LanceDB ingestion.
#
# Usage: cd site && bash llm/render.sh
#
# This swaps in a minimal _quarto.yml (no sidebars, navbar, etc.),
# renders to GFM, then post-processes to strip HTML and clean up formatting.

set -euo pipefail

SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$SITE_DIR"

cleanup() {
  echo "Restoring _quarto.yml ..."
  cp "$QUARTO_BACKUP" _quarto.yml
  rm -f "$QUARTO_BACKUP"
}
# Restore the exact working copy, including uncommitted changes.
QUARTO_BACKUP=$(mktemp)
cp _quarto.yml "$QUARTO_BACKUP"
trap cleanup EXIT

# Replace _quarto.yml for this render.

cat > _quarto.yml << 'EOF'
project:
  type: default
  output-dir: llm/_llm-output
  render:
    - "**/*.qmd"
    - "!notebooks/"
    - "!404.qmd"
    - "!about/contributing/validmind-community.qmd"
    - "!about/contributing/style-guide/"
    - "!about/deployment/"
    - "!about/fine-print/"
    - "!llm/"
    - "!internal/"
    - "!tests/"
    - "!training/training-templates/"

format:
  gfm:
    toc: false
    number-sections: false
    wrap: none

execute:
  enabled: false
EOF

echo "=== Rendering site to GFM markdown ==="
uv run --with pyyaml python ../scripts/render_docs.py --site . --to gfm

# AGENTS.md lives at the repo root so IDE/agent tooling finds it there, but it
# must also reach the LLM output so the docs chatbot can ingest it.
echo ""
echo "=== Generating chatbot product map ==="
python3 scripts/generate_chatbot_product_map.py

echo ""
echo "=== Copying AGENTS.md from repo root into LLM output ==="
cp ../AGENTS.md llm/_llm-output/AGENTS.md

echo ""
echo "=== Copying chatbot product map into LLM output ==="
cp llm/chatbot-product-map.md llm/_llm-output/chatbot-product-map.md

echo ""
echo "=== Post-processing markdown files ==="
bash llm/clean.sh

echo ""
echo "Done. Output in site/llm/_llm-output/"

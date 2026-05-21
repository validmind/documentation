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
  git checkout -- _quarto.yml 2>/dev/null || cp llm/_quarto-backup.yml _quarto.yml
  rm -f llm/_quarto-backup.yml
}
trap cleanup EXIT

# Backup and replace _quarto.yml
cp _quarto.yml llm/_quarto-backup.yml

cat > _quarto.yml << 'EOF'
project:
  type: default
  output-dir: llm/_llm-output
  render:
    - "**/*.qmd"
    - "!notebooks/"
    - "!404.qmd"
    - "!about/contributing/"
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
quarto render --to gfm

echo ""
echo "=== Post-processing markdown files ==="
bash llm/clean.sh

echo ""
echo "Done. Output in site/llm/_llm-output/"

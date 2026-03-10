#!/usr/bin/env bash
# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Post-processes rendered GFM markdown for LLM / LanceDB ingestion.
# Strips HTML tags, cleans up callouts, removes artifacts.
#
# Usage: bash llm/clean.sh

set -euo pipefail

SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$SITE_DIR/llm/_llm-output"

if [ ! -d "$OUT_DIR" ]; then
  echo "Error: $OUT_DIR does not exist. Run render.sh first."
  exit 1
fi

count=0
while IFS= read -r -d '' f; do
  count=$((count + 1))

  # 1. Strip HTML div/span wrappers but keep their text content
  #    e.g. <span class="bubble"> Developer</span> → Developer
  #    e.g. <div class="attn"> ... </div> → ...
  sed -i -E \
    -e 's/<span[^>]*>//g' \
    -e 's/<\/span>//g' \
    -e 's/<div[^>]*>//g' \
    -e 's/<\/div>//g' \
    -e 's/<img[^>]*\/?>/ /g' \
    "$f"

  # 2. Clean up Quarto callout artifacts
  #    > [!NONE] → (remove, it's a Quarto artifact)
  #    > [!WARNING] etc. are valid GFM alerts, keep those
  sed -i -E \
    -e '/^\s*> \[!NONE\]\s*$/d' \
    "$f"

  # 3. Remove leftover fenced div markers (::: with optional classes or trailing -->)
  sed -i -E \
    -e '/^:{3,}\s*(\{[^}]*\})?\s*(-->)?\s*$/d' \
    "$f"

  # 4. Strip unresolved {{< include ... >}} shortcodes
  sed -i -E \
    -e '/\{\{< include [^>]+ >\}\}/d' \
    "$f"

  # 5. Clean up leftover HTML comments (single-line and multi-line)
  perl -i -0pe 's/<!--.*?-->//gs' "$f"

  # 6. Strip HTML entities that leaked through
  sed -i -E \
    -e 's/&#[0-9]+;//g' \
    "$f"

  # 7. Collapse 3+ consecutive blank lines into 2
  perl -i -0pe 's/\n{3,}/\n\n/g' "$f"

done < <(find "$OUT_DIR" -name '*.md' -print0)

echo "Cleaned $count markdown files in $OUT_DIR"

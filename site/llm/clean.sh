#!/usr/bin/env bash
# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# Post-processes rendered GFM markdown for LLM ingestion.
# Uses Pandoc for reliable HTML stripping, plus minimal text cleanup.
#
# Usage: bash llm/clean.sh

set -euo pipefail

SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$SITE_DIR/llm/_llm-output"
FILTER="$SITE_DIR/llm/strip-html.lua"

if [ ! -d "$OUT_DIR" ]; then
  echo "Error: $OUT_DIR does not exist. Run render.sh first."
  exit 1
fi

# Process a single file
process_file() {
  local f="$1"
  local filter="$2"
  
  # Pandoc pass: strip HTML, unwrap divs, normalize whitespace
  pandoc -f gfm+fenced_divs -t gfm \
    --strip-comments \
    --lua-filter="$filter" \
    "$f" -o "$f"
  
  # Minimal text cleanup for Quarto-specific artifacts
  perl -i -pe '
    s/^>\s*\[!NONE\]\s*$//;
    s/\{\{<\s*include\s+[^>]+\s*>\}\}//g;
  ' "$f"
}
export -f process_file

# Determine number of parallel jobs (use available CPUs, max 8)
JOBS=$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)
JOBS=$((JOBS > 8 ? 8 : JOBS))

echo "Cleaning markdown files with $JOBS parallel jobs..."

# Process files in parallel
find "$OUT_DIR" -name '*.md' -print0 | \
  xargs -0 -P "$JOBS" -n 1 bash -c 'process_file "$1" "'"$FILTER"'"' _

count=$(find "$OUT_DIR" -name '*.md' | wc -l | tr -d ' ')
echo "Cleaned $count markdown files in $OUT_DIR"

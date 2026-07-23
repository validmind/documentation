#!/usr/bin/env bash

set -euo pipefail

if [[ "$#" -eq 0 ]]; then
  echo "Usage: render-pages.sh <site-relative-page.qmd> [...]" >&2
  exit 2
fi

repository_root="$(git rev-parse --show-toplevel)"
site_root="${repository_root}/site"

for requested_page in "$@"; do
  page="${requested_page#site/}"
  if [[ ! -f "${site_root}/${page}" ]]; then
    echo "Page not found: ${requested_page}" >&2
    exit 2
  fi

  echo "Rendering ${page}"
  (
    cd "${site_root}"
    quarto render "${page}" --profile development
  )
done

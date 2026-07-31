#!/usr/bin/env python3
# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

"""Merge Quarto indexes from a partial render into full-site indexes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def merge_items(
    base: list[dict[str, Any]], partial: list[dict[str, Any]], key: str
) -> list[dict[str, Any]]:
    """Return base items with partial items replacing entries with the same key."""
    merged: dict[str, dict[str, Any]] = {}
    for item in [*base, *partial]:
        value = item.get(key)
        if not isinstance(value, str) or not value:
            raise ValueError(f"Every index item must have a non-empty {key!r}")
        merged[value] = item
    return list(merged.values())


def merge_file(base_path: Path, partial_path: Path, key: str) -> None:
    base = json.loads(base_path.read_text())
    partial = json.loads(partial_path.read_text())
    if not isinstance(base, list) or not isinstance(partial, list):
        raise ValueError("Quarto indexes must contain JSON arrays")
    partial_path.write_text(
        json.dumps(merge_items(base, partial, key), separators=(",", ":"))
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-search", type=Path, required=True)
    parser.add_argument("--partial-search", type=Path, required=True)
    parser.add_argument("--base-listings", type=Path, required=True)
    parser.add_argument("--partial-listings", type=Path, required=True)
    args = parser.parse_args()

    merge_file(args.base_search, args.partial_search, "objectID")
    merge_file(args.base_listings, args.partial_listings, "listing")


if __name__ == "__main__":
    main()

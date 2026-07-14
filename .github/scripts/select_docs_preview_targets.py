#!/usr/bin/env python3
# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

"""Select pages that are safe to render incrementally for a PR preview."""

from __future__ import annotations

import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


PAGE_SUFFIXES = {".qmd", ".md", ".ipynb"}
ASSET_SUFFIXES = {".avif", ".gif", ".jpeg", ".jpg", ".pdf", ".png", ".svg", ".webp"}
UNSAFE_TOP_LEVEL = {
    "_extensions",
    "_freeze",
    "_source",
    "environments",
    "llm",
    "scripts",
}


@dataclass(frozen=True)
class Selection:
    targets: tuple[str, ...] = ()
    assets: tuple[str, ...] = ()
    fallback_reason: str | None = None

    @property
    def is_targeted(self) -> bool:
        return self.fallback_reason is None


def select(changes: list[tuple[str, tuple[str, ...]]]) -> Selection:
    targets: set[str] = set()
    assets: set[str] = set()

    for status, paths in changes:
        if status not in {"A", "M"} or len(paths) != 1:
            return Selection(fallback_reason=f"{status} change requires a full render")

        path = PurePosixPath(paths[0])
        if not path.parts or path.parts[0] != "site" or len(path.parts) < 2:
            return Selection(fallback_reason=f"{path} is outside targetable site content")

        relative = PurePosixPath(*path.parts[1:])
        if relative.parts[0] in UNSAFE_TOP_LEVEL:
            return Selection(fallback_reason=f"{path} can affect generated or global content")
        if any(part.startswith("_") for part in relative.parts):
            return Selection(fallback_reason=f"{path} is Quarto metadata or shared content")

        suffix = relative.suffix.lower()
        if suffix in PAGE_SUFFIXES:
            targets.add(relative.as_posix())
        elif suffix in ASSET_SUFFIXES:
            assets.add(relative.as_posix())
        else:
            return Selection(fallback_reason=f"{path} is not a targetable page or asset")

    if not targets:
        return Selection(fallback_reason="no changed renderable pages were found")

    return Selection(tuple(sorted(targets)), tuple(sorted(assets)))


def parse_name_status(output: str) -> list[tuple[str, tuple[str, ...]]]:
    changes: list[tuple[str, tuple[str, ...]]] = []
    for line in output.splitlines():
        fields = line.split("\t")
        if len(fields) < 2:
            raise ValueError(f"Unexpected git diff line: {line!r}")
        changes.append((fields[0][0], tuple(fields[1:])))
    return changes


def git_changes(base: str, head: str) -> list[tuple[str, tuple[str, ...]]]:
    result = subprocess.run(
        ["git", "diff", "--name-status", "--find-renames", f"{base}...{head}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return parse_name_status(result.stdout)


def write_lines(path: Path, values: tuple[str, ...]) -> None:
    path.write_text("".join(f"{value}\n" for value in values))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--targets", type=Path, required=True)
    parser.add_argument("--assets", type=Path, required=True)
    args = parser.parse_args()

    selection = select(git_changes(args.base, args.head))
    if not selection.is_targeted:
        print(f"Full render required: {selection.fallback_reason}")
        return 3

    write_lines(args.targets, selection.targets)
    write_lines(args.assets, selection.assets)
    print("Targeted render pages:")
    print("\n".join(selection.targets))
    if selection.assets:
        print("Targeted preview assets:")
        print("\n".join(selection.assets))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

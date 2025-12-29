# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

"""
This script adds a standard ValidMind copyright
block to all .qmd, .yml, and .yaml files in the documentation repository.

How to use:
    python site/scripts/copyright_qmd_files.py
"""

import os
import re
import fnmatch
from pathlib import Path


def find_repo_root():
    """Find the repository root by looking for .gitignore file."""
    current = Path(__file__).resolve()
    # Start from the scripts directory, go up to find repo root
    for parent in current.parents:
        gitignore_path = parent / ".gitignore"
        if gitignore_path.exists():
            return parent
    # Fallback: assume we're in site/scripts, so repo root is ../..
    return current.parent.parent.parent


def read_gitignore(repo_root):
    """Read .gitignore file and return list of patterns."""
    gitignore_path = repo_root / ".gitignore"
    patterns = []
    if gitignore_path.exists():
        with open(gitignore_path, "r") as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith("#"):
                    patterns.append(line)
    return patterns


def should_ignore(path, gitignore_patterns, repo_root):
    """Check if a path should be ignored based on .gitignore patterns."""
    # Convert to relative path from repo root
    try:
        rel_path = path.relative_to(repo_root)
    except ValueError:
        # Path is not under repo root
        return True
    
    rel_path_str = str(rel_path).replace("\\", "/")
    path_parts = rel_path.parts
    
    # Check each pattern
    for pattern in gitignore_patterns:
        # Handle directory patterns (ending with /)
        if pattern.endswith("/"):
            pattern = pattern[:-1]
            # Check if any parent directory matches
            for i in range(len(path_parts)):
                check_path = "/".join(path_parts[:i+1])
                if fnmatch.fnmatch(check_path, pattern) or fnmatch.fnmatch(check_path, pattern + "/*"):
                    return True
        else:
            # Check full path and filename
            if fnmatch.fnmatch(rel_path_str, pattern) or fnmatch.fnmatch(path.name, pattern):
                return True
            # Check if any parent directory matches
            for i in range(len(path_parts)):
                check_path = "/".join(path_parts[:i+1])
                if fnmatch.fnmatch(check_path, pattern):
                    return True
    
    return False


def copyright_qmd_file(file_path, copyright):
    """Add copyright to a .qmd file in the frontmatter."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if file has frontmatter (starts with ---)
    if not content.strip().startswith("---"):
        # No frontmatter, add it at the beginning
        new_content = f"---\n{copyright}---\n\n{content}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return
    
    # Find the frontmatter block
    lines = content.splitlines(keepends=True)
    
    # Find opening ---
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            start_idx = i
            break
    
    if start_idx is None:
        # Malformed, add frontmatter at the beginning
        new_content = f"---\n{copyright}---\n\n{content}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return
    
    # Find closing ---
    end_idx = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    
    if end_idx is None:
        # Malformed frontmatter, add copyright after opening ---
        copyright_lines = copyright.splitlines(keepends=True)
        lines.insert(start_idx + 1, "".join(copyright_lines))
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        return
    
    # Check if copyright already exists in frontmatter
    frontmatter_content = "".join(lines[start_idx:end_idx+1])
    if "# Copyright ©" in frontmatter_content and "# SPDX-License-Identifier:" in frontmatter_content:
        # Copyright exists, check if we need to update it
        # Find the copyright block
        copyright_start = None
        copyright_end = None
        for i in range(start_idx + 1, end_idx):
            if lines[i].strip().startswith("# Copyright"):
                copyright_start = i
            elif copyright_start is not None and lines[i].strip().startswith("# SPDX-License-Identifier:"):
                copyright_end = i
                break
        
        if copyright_start is not None and copyright_end is not None:
            # Replace existing copyright
            copyright_lines = copyright.splitlines(keepends=True)
            new_lines = lines[:copyright_start] + ["".join(copyright_lines)] + lines[copyright_end+1:]
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            return
    
    # Add copyright after opening ---
    copyright_lines = copyright.splitlines(keepends=True)
    lines.insert(start_idx + 1, "".join(copyright_lines))
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def copyright_yaml_file(file_path, copyright):
    """Add copyright to a .yml or .yaml file at the top."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Check if copyright already exists at the start
    copyright_lines = copyright.strip().splitlines()
    if len(lines) >= len(copyright_lines):
        # Check if first lines match copyright
        matches = True
        for i, copyright_line in enumerate(copyright_lines):
            if i >= len(lines):
                matches = False
                break
            if copyright_line not in lines[i]:
                matches = False
                break
        
        if matches:
            # Check if we need to update (copyright might be different)
            actual_copyright = "".join(lines[:len(copyright_lines)]).rstrip()
            expected_copyright = copyright.rstrip()
            if actual_copyright == expected_copyright:
                # Already correct, no update needed
                return
            else:
                # Need to replace existing copyright
                new_lines = copyright.splitlines(keepends=True) + lines[len(copyright_lines):]
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                return
    
    # Check if there's a copyright block that needs updating (might be in different position)
    copyright_start = None
    copyright_end = None
    for i, line in enumerate(lines):
        if line.strip().startswith("# Copyright"):
            copyright_start = i
        elif copyright_start is not None and line.strip().startswith("# SPDX-License-Identifier:"):
            copyright_end = i
            break
    
    if copyright_start is not None and copyright_end is not None:
        # Replace existing copyright block
        copyright_lines_new = copyright.splitlines(keepends=True)
        new_lines = lines[:copyright_start] + copyright_lines_new + lines[copyright_end+1:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        return
    
    # Add copyright at the beginning
    new_content = copyright + "".join(lines)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    # Get repository root
    repo_root = find_repo_root()
    script_dir = Path(__file__).parent
    
    # Read copyright text
    copyright_path = script_dir / "copyright.txt"
    with open(copyright_path, "r", encoding="utf-8") as f:
        copyright = f.read()
    
    # Ensure copyright ends with newline for proper insertion
    if not copyright.endswith("\n"):
        copyright += "\n"
    
    # Read .gitignore patterns
    gitignore_patterns = read_gitignore(repo_root)
    
    # Directories to scan
    site_dir = repo_root / "site"
    internal_dir = repo_root / "internal"
    
    directories_to_scan = []
    if site_dir.exists():
        directories_to_scan.append(site_dir)
    if internal_dir.exists():
        directories_to_scan.append(internal_dir)
    
    # Process files
    for directory in directories_to_scan:
        for root, dirs, files in os.walk(directory):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not should_ignore(Path(root) / d, gitignore_patterns, repo_root)]
            
            for file in files:
                file_path = Path(root) / file
                
                # Check if file should be ignored
                if should_ignore(file_path, gitignore_patterns, repo_root):
                    continue
                
                # Process .qmd files
                if file.endswith(".qmd"):
                    try:
                        copyright_qmd_file(file_path, copyright)
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
                
                # Process .yml and .yaml files
                elif file.endswith((".yml", ".yaml")):
                    try:
                        copyright_yaml_file(file_path, copyright)
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    main()


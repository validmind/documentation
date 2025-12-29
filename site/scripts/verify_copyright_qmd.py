# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

"""
This script verifies that all .qmd, .yml, and .yaml files under the
documentation repository have the ValidMind copyright block.

How to use:
    python site/scripts/verify_copyright_qmd.py
"""

import os
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


def verify_qmd_file(file_path, copyright):
    """Verify that a .qmd file has the copyright header in frontmatter."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if file has frontmatter (starts with ---)
    if not content.strip().startswith("---"):
        return False
    
    # Find the frontmatter block
    lines = content.splitlines()
    
    # Find opening ---
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            start_idx = i
            break
    
    if start_idx is None:
        return False
    
    # Find closing ---
    end_idx = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    
    if end_idx is None:
        return False
    
    # Check frontmatter for copyright
    frontmatter_lines = lines[start_idx+1:end_idx]
    frontmatter_content = "\n".join(frontmatter_lines)
    
    # Check if copyright header exists
    copyright_lines = copyright.strip().splitlines()
    if len(copyright_lines) < 3:
        return False
    
    # Check for copyright header components
    has_copyright = any("# Copyright ©" in line for line in frontmatter_lines)
    has_license_ref = any("# See the LICENSE file" in line for line in frontmatter_lines)
    has_spdx = any("# SPDX-License-Identifier:" in line for line in frontmatter_lines)
    
    return has_copyright and has_license_ref and has_spdx


def verify_yaml_file(file_path, copyright):
    """Verify that a .yml or .yaml file has the copyright header at the top."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if file starts with copyright
    copyright_lines = copyright.strip().splitlines()
    if len(copyright_lines) < 3:
        return False
    
    content_lines = content.splitlines()
    if len(content_lines) < len(copyright_lines):
        return False
    
    # Check if first lines match copyright header exactly
    for i, copyright_line in enumerate(copyright_lines):
        if i >= len(content_lines):
            return False
        # Check if the line contains the copyright text (allowing for whitespace differences)
        if copyright_line.strip() not in content_lines[i]:
            return False
    
    # Also verify we have the key components
    first_lines_content = "\n".join(content_lines[:len(copyright_lines)])
    has_copyright = "# Copyright ©" in first_lines_content
    has_license_ref = "# See the LICENSE file" in first_lines_content
    has_spdx = "# SPDX-License-Identifier:" in first_lines_content
    
    return has_copyright and has_license_ref and has_spdx


def main():
    # Get repository root
    repo_root = find_repo_root()
    script_dir = Path(__file__).parent
    
    # Read copyright text
    copyright_path = script_dir / "copyright.txt"
    with open(copyright_path, "r", encoding="utf-8") as f:
        copyright = f.read()
    
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
    
    # Invalid files
    errors = []
    
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
                        if not verify_qmd_file(file_path, copyright):
                            errors.append(str(file_path))
                    except Exception as e:
                        errors.append(f"{file_path} (error: {e})")
                
                # Process .yml and .yaml files
                elif file.endswith((".yml", ".yaml")):
                    try:
                        if not verify_yaml_file(file_path, copyright):
                            errors.append(str(file_path))
                    except Exception as e:
                        errors.append(f"{file_path} (error: {e})")
    
    if errors:
        print("\n".join(errors))
        print("\nPlease fix the errors above by running `make copyright`")
        exit(1)


if __name__ == "__main__":
    main()


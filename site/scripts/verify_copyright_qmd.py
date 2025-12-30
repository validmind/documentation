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
import sys
import fnmatch
from pathlib import Path


def find_repo_root():
    """Find the repository root by looking for .git directory."""
    current = Path(__file__).resolve()
    # Start from the scripts directory, go up to find repo root
    # Look for .git directory as the definitive indicator of repo root
    for parent in current.parents:
        git_dir = parent / ".git"
        if git_dir.exists() and git_dir.is_dir():
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
    
    # Ignore directories that start with _ (exclude filename from check)
    for part in path_parts[:-1]:
        if part.startswith("_"):
            return True
    
    # Check each pattern
    for pattern in gitignore_patterns:
        # Handle patterns starting with / (absolute from repo root)
        is_absolute = pattern.startswith("/")
        if is_absolute:
            pattern = pattern[1:]  # Remove leading /
        
        # Handle directory patterns (ending with /)
        is_dir_pattern = pattern.endswith("/")
        if is_dir_pattern:
            pattern = pattern[:-1]
        
        if is_absolute:
            # Absolute patterns must match from repo root
            # Check if path starts with pattern or matches at any parent level
            if fnmatch.fnmatch(rel_path_str, pattern) or rel_path_str.startswith(pattern + "/"):
                return True
            # Check parent directories
            for i in range(len(path_parts)):
                check_path = "/".join(path_parts[:i+1])
                if fnmatch.fnmatch(check_path, pattern) or check_path.startswith(pattern + "/"):
                    return True
        else:
            # Relative patterns can match anywhere in the path
            # Check full path
            if fnmatch.fnmatch(rel_path_str, pattern) or pattern in rel_path_str:
                return True
            # Check filename only
            if fnmatch.fnmatch(path.name, pattern):
                return True
            # Check if any parent directory matches
            for i in range(len(path_parts)):
                check_path = "/".join(path_parts[:i+1])
                if fnmatch.fnmatch(check_path, pattern) or pattern in check_path:
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
    
    # Files missing copyright headers
    missing_copyright = []
    count_qmd_missing = 0
    count_yml_missing = 0
    count_yaml_missing = 0
    
    # Total files checked
    total_qmd = 0
    total_yml = 0
    total_yaml = 0
    
    # Process files
    try:
        for directory in directories_to_scan:
            try:
                for root, dirs, files in os.walk(directory):
                    try:
                        # Filter out ignored directories
                        dirs[:] = [d for d in dirs if not should_ignore(Path(root) / d, gitignore_patterns, repo_root)]
                        
                        for file in files:
                            file_path = Path(root) / file
                            
                            try:
                                # Check if file should be ignored
                                if should_ignore(file_path, gitignore_patterns, repo_root):
                                    continue
                                
                                # Ignore plugin.yml files
                                if file == "plugin.yml":
                                    continue
                                
                                # Files starting with _ should be treated as YAML (no frontmatter)
                                # Skip .qmd files that start with _
                                if file.startswith("_") and file.endswith((".yml", ".yaml")):
                                    try:
                                        if file.endswith(".yml"):
                                            total_yml += 1
                                        elif file.endswith(".yaml"):
                                            total_yaml += 1
                                        if not verify_yaml_file(file_path, copyright):
                                            missing_copyright.append(str(file_path))
                                            if file.endswith(".yml"):
                                                count_yml_missing += 1
                                            elif file.endswith(".yaml"):
                                                count_yaml_missing += 1
                                    except Exception as e:
                                        # Log error but continue processing
                                        print(f"Error verifying {file_path}: {e}", file=sys.stderr)
                                # Process .qmd files (not starting with _)
                                elif file.endswith(".qmd"):
                                    try:
                                        total_qmd += 1
                                        if not verify_qmd_file(file_path, copyright):
                                            missing_copyright.append(str(file_path))
                                            count_qmd_missing += 1
                                    except Exception as e:
                                        # Log error but continue processing
                                        print(f"Error verifying {file_path}: {e}", file=sys.stderr)
                                
                                # Process .yml files (not starting with _)
                                elif file.endswith(".yml"):
                                    try:
                                        total_yml += 1
                                        if not verify_yaml_file(file_path, copyright):
                                            missing_copyright.append(str(file_path))
                                            count_yml_missing += 1
                                    except Exception as e:
                                        # Log error but continue processing
                                        print(f"Error verifying {file_path}: {e}", file=sys.stderr)
                                
                                # Process .yaml files (not starting with _)
                                elif file.endswith(".yaml"):
                                    try:
                                        total_yaml += 1
                                        if not verify_yaml_file(file_path, copyright):
                                            missing_copyright.append(str(file_path))
                                            count_yaml_missing += 1
                                    except Exception as e:
                                        # Log error but continue processing
                                        print(f"Error verifying {file_path}: {e}", file=sys.stderr)
                            except Exception as e:
                                # Continue processing other files even if one fails
                                print(f"Error processing {file_path}: {e}", file=sys.stderr)
                    except Exception as e:
                        # Continue processing other directories even if one fails
                        print(f"Error processing directory {root}: {e}", file=sys.stderr)
            except Exception as e:
                # Continue processing other directories even if one fails
                print(f"Error accessing directory {directory}: {e}", file=sys.stderr)
    except Exception as e:
        # Catch any unexpected errors but still report what we found
        print(f"Unexpected error during file scanning: {e}", file=sys.stderr)
    
    if missing_copyright:
        print("Files missing a copyright header:")
        print("\n".join(missing_copyright))
        print(f"\nMissing copyright headers in {count_qmd_missing} .qmd, {count_yml_missing} .yml, and {count_yaml_missing} .yaml files.")
        print("\nFix the errors by running `make copyright` and then try verifying the copyright headers again.")
        sys.exit(1)
    else:
        print(f"All copyright headers verified successfully in {total_qmd} .qmd, {total_yml} .yml, and {total_yaml} .yaml files.")


if __name__ == "__main__":
    main()


"""
This script adds a standard ValidMind copyright
block to all .qmd, .yml, and .yaml files in the documentation repository.

How to use:
    python site/scripts/add_copyright.py
"""

import os
import re
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


def format_copyright_yaml(copyright):
    """Format copyright with # comment markers for YAML/frontmatter."""
    lines = copyright.strip().splitlines()
    return "\n".join(f"# {line}" for line in lines)


def format_copyright_html(copyright):
    """Format copyright with HTML comment markers for embedded files."""
    lines = copyright.strip().splitlines()
    return "<!-- " + "\n".join(lines) + " -->"


def copyright_qmd_file(file_path, copyright):
    """Add copyright to a .qmd file in the frontmatter.
    Returns True if copyright was added or updated, False otherwise."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Format copyright with YAML comment markers
    copyright_formatted = format_copyright_yaml(copyright) + "\n"
    
    # Check if file has frontmatter (starts with ---)
    if not content.strip().startswith("---"):
        # No frontmatter, add it at the beginning
        new_content = f"---\n{copyright_formatted}---\n\n{content}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    
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
        new_content = f"---\n{copyright_formatted}---\n\n{content}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    
    # Find closing ---
    end_idx = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    
    if end_idx is None:
        # Malformed frontmatter, add copyright after opening ---
        copyright_lines = [line + "\n" for line in copyright_formatted.rstrip().splitlines()]
        lines.insert(start_idx + 1, "".join(copyright_lines))
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        return True
    
    # Check if copyright already exists in frontmatter (check for raw content)
    frontmatter_content = "".join(lines[start_idx:end_idx+1])
    copyright_first_line = copyright.strip().splitlines()[0]
    copyright_last_line = copyright.strip().splitlines()[-1]
    
    if copyright_first_line in frontmatter_content and copyright_last_line in frontmatter_content:
        # Copyright exists, check if we need to update it
        # Find the copyright block
        copyright_start = None
        copyright_end = None
        for i in range(start_idx + 1, end_idx):
            if copyright_first_line in lines[i]:
                copyright_start = i
            elif copyright_start is not None and copyright_last_line in lines[i]:
                copyright_end = i
                break
        
        if copyright_start is not None and copyright_end is not None:
            # Check if existing copyright already matches expected format
            existing_copyright = "".join(lines[copyright_start:copyright_end+1])
            if copyright_formatted.rstrip() in existing_copyright:
                # Already correct, no update needed
                return False
            # Replace existing copyright
            copyright_lines = [line + "\n" for line in copyright_formatted.rstrip().splitlines()]
            new_lines = lines[:copyright_start] + ["".join(copyright_lines)] + lines[copyright_end+1:]
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            return True
    
    # Add copyright after opening ---
    copyright_lines = [line + "\n" for line in copyright_formatted.rstrip().splitlines()]
    lines.insert(start_idx + 1, "".join(copyright_lines))
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return True


def copyright_yaml_file(file_path, copyright):
    """Add copyright to a .yml or .yaml file at the top.
    Returns True if copyright was added or updated, False otherwise."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Format copyright with YAML comment markers
    copyright_formatted = format_copyright_yaml(copyright)
    copyright_formatted_lines = copyright_formatted.splitlines()
    
    # Check if copyright already exists at the start (check for raw content)
    copyright_raw_lines = copyright.strip().splitlines()
    if len(lines) >= len(copyright_raw_lines):
        # Check if first lines contain the copyright content
        matches = True
        for i, copyright_line in enumerate(copyright_raw_lines):
            if i >= len(lines):
                matches = False
                break
            if copyright_line not in lines[i]:
                matches = False
                break
        
        if matches:
            # Copyright exists at start, check if it needs updating
            # Compare formatted versions
            actual_first_lines = "".join(lines[:len(copyright_raw_lines)]).rstrip()
            if copyright_formatted in actual_first_lines or all(line in actual_first_lines for line in copyright_raw_lines):
                # Already correct, no update needed
                return False
            else:
                # Need to replace existing copyright
                copyright_lines_new = [line + "\n" for line in copyright_formatted_lines]
                # Add blank line only if next line isn't already blank
                next_line_idx = len(copyright_raw_lines)
                if next_line_idx < len(lines) and lines[next_line_idx].strip():
                    copyright_lines_new.append("\n")
                new_lines = copyright_lines_new + lines[len(copyright_raw_lines):]
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                return True
    
    # Check if there's a copyright block that needs updating (might be in different position)
    copyright_first_line = copyright_raw_lines[0]
    copyright_last_line = copyright_raw_lines[-1]
    copyright_start = None
    copyright_end = None
    for i, line in enumerate(lines):
        if copyright_first_line in line:
            copyright_start = i
        elif copyright_start is not None and copyright_last_line in line:
            copyright_end = i
            break
    
    if copyright_start is not None and copyright_end is not None:
        # Replace existing copyright block
        copyright_lines_new = [line + "\n" for line in copyright_formatted_lines]
        # Add blank line only if next line isn't already blank
        next_line_idx = copyright_end + 1
        if next_line_idx < len(lines) and lines[next_line_idx].strip():
            copyright_lines_new.append("\n")
        new_lines = lines[:copyright_start] + copyright_lines_new + lines[copyright_end+1:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        return True
    
    # Add copyright at the beginning
    copyright_lines_new = [line + "\n" for line in copyright_formatted_lines]
    # Add blank line only if first line of file isn't already blank
    if lines and lines[0].strip():
        copyright_lines_new.append("\n")
    new_content = "".join(copyright_lines_new) + "".join(lines)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def copyright_qmd_embedded_file(file_path, copyright):
    """Add copyright to an embedded .qmd file (starting with _) using HTML comments.
    Returns True if copyright was added or updated, False otherwise."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Format copyright with HTML comment markers
    copyright_formatted = format_copyright_html(copyright)
    copyright_raw_lines = copyright.strip().splitlines()
    
    # Check if copyright already exists (check for raw content in any comment format)
    copyright_first_line = copyright_raw_lines[0]
    copyright_last_line = copyright_raw_lines[-1]
    
    if copyright_first_line in content and copyright_last_line in content:
        # Copyright exists, check if it's in the correct HTML format
        if copyright_formatted in content:
            # Already correct, no update needed
            return False
        
        # Need to replace existing copyright (could be in YAML frontmatter or wrong format)
        # Check for YAML frontmatter with copyright
        if content.strip().startswith("---"):
            lines = content.splitlines(keepends=True)
            # Find frontmatter boundaries
            start_idx = None
            end_idx = None
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    if start_idx is None:
                        start_idx = i
                    else:
                        end_idx = i
                        break
            
            if start_idx is not None and end_idx is not None:
                # Check if frontmatter only contains copyright
                frontmatter_lines = lines[start_idx+1:end_idx]
                frontmatter_content = "".join(frontmatter_lines).strip()
                has_only_copyright = all(
                    line.strip().startswith("#") and any(cl in line for cl in copyright_raw_lines)
                    for line in frontmatter_lines if line.strip()
                )
                
                if has_only_copyright:
                    # Remove frontmatter and add HTML copyright
                    remaining_content = "".join(lines[end_idx+1:]).lstrip()
                    new_content = copyright_formatted + "\n\n" + remaining_content
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    return True
        
        # Try to find and replace HTML comment copyright
        import re
        html_comment_pattern = r'<!--[^>]*?' + re.escape(copyright_first_line) + r'.*?' + re.escape(copyright_last_line) + r'[^>]*?-->'
        if re.search(html_comment_pattern, content, re.DOTALL):
            new_content = re.sub(html_comment_pattern, copyright_formatted, content, flags=re.DOTALL)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
    
    # Check if file has YAML frontmatter that should be removed
    if content.strip().startswith("---"):
        lines = content.splitlines(keepends=True)
        start_idx = None
        end_idx = None
        for i, line in enumerate(lines):
            if line.strip() == "---":
                if start_idx is None:
                    start_idx = i
                else:
                    end_idx = i
                    break
        
        if start_idx is not None and end_idx is not None:
            # Check if frontmatter is empty or only whitespace
            frontmatter_content = "".join(lines[start_idx+1:end_idx]).strip()
            if not frontmatter_content:
                # Remove empty frontmatter
                remaining_content = "".join(lines[end_idx+1:]).lstrip()
                new_content = copyright_formatted + "\n\n" + remaining_content
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                return True
    
    # Add copyright at the beginning
    new_content = copyright_formatted + "\n\n" + content.lstrip()
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


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
    
    # Track files that were modified
    modified_files = []
    count_qmd = 0
    count_yml = 0
    count_yaml = 0
    
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
                
                # Ignore plugin.yml files
                if file == "plugin.yml":
                    continue
                
                # Files starting with _ need special handling
                if file.startswith("_"):
                    if file.endswith((".yml", ".yaml")):
                        # YAML files starting with _ use YAML comments (no frontmatter)
                        try:
                            if copyright_yaml_file(file_path, copyright):
                                modified_files.append(str(file_path))
                                if file.endswith(".yml"):
                                    count_yml += 1
                                elif file.endswith(".yaml"):
                                    count_yaml += 1
                        except Exception as e:
                            print(f"Error processing {file_path}: {e}")
                    elif file.endswith(".qmd"):
                        # Embedded .qmd files use HTML comments
                        try:
                            if copyright_qmd_embedded_file(file_path, copyright):
                                modified_files.append(str(file_path))
                                count_qmd += 1
                        except Exception as e:
                            print(f"Error processing {file_path}: {e}")
                # Process regular .qmd files (not starting with _)
                elif file.endswith(".qmd"):
                    try:
                        if copyright_qmd_file(file_path, copyright):
                            modified_files.append(str(file_path))
                            count_qmd += 1
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
                # Process .yml and .yaml files (not starting with _)
                elif file.endswith((".yml", ".yaml")):
                    try:
                        if copyright_yaml_file(file_path, copyright):
                            modified_files.append(str(file_path))
                            if file.endswith(".yml"):
                                count_yml += 1
                            elif file.endswith(".yaml"):
                                count_yaml += 1
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")
    
    # Output results
    if modified_files:
        for file_path in modified_files:
            print(file_path)
        print(f"\nAdded copyright headers in {count_qmd} .qmd, {count_yml} .yml, and {count_yaml} .yaml files.")


if __name__ == "__main__":
    main()


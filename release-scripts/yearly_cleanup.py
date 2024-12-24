from datetime import datetime
import os
import re
import shutil

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def get_year():
    """
    Asks the user for the year to be compiled.

    Returns:
        str: The year entered.
    """
    # Default year is the current year minus 1 
    default_year = str(datetime.now().year - 1)

    # Prompt the user for input
    year = input(
        f"Enter the year you want to compile (leave empty for default [{default_year}]): "
    ) or default_year

    print(f"Rounding up releases for: {year}\n")
    return year

def create_year_folder(year):
    """
    Creates a new directory in ../site/releases/ with the given year as the name.

    Args:
        year (str): The name of the directory to create.

    Returns:
        str: The path to the new yearly directory.
    """
    releases_dir = f"../site/releases/"
    yearly_path = f"../site/releases/{year}/"

    os.makedirs(releases_dir, exist_ok=True)

    if os.path.exists(yearly_path):
        print(f"The directory '{yearly_path}' already exists.")
    else:
        os.makedirs(yearly_path)
        print(f"Created folder: {yearly_path}\n")
    
    return yearly_path

release_folders = []

def get_yearly_releases(year):
    """
    Finds subdirectories in ../site/releases/ that begin with the specified year.

    Args:
        year (str): The year prefix to search for in subdirectory names.

    Returns:
        list: A list of matching subdirectory names, sorted alphabetically.
    """
    global release_folders 
    releases_dir = "../site/releases/"

    if not os.path.exists(releases_dir):
        print(f"'{releases_dir}' does not exist.")
        release_folders = []  
        return release_folders

    subdirs = [d for d in os.listdir(releases_dir) if os.path.isdir(os.path.join(releases_dir, d))]
    matching_subdirs = [os.path.join(releases_dir, d) for d in subdirs if d.startswith(f"{year}-")]

    if matching_subdirs:
        print(f"Found {len(matching_subdirs)} release folders for year {year}:")
    else:
        print(f"No release folders found for year {year}.")

    release_folders = sorted(matching_subdirs)
    return release_folders

def move_yearly_releases(yearly_path, release_folders):
    """
    Moves all subdirectories and files within them from the release_folders list 
    into the yearly_path directory.

    Args:
        yearly_path (str): The destination directory.
        release_folders (list): A list of subdirectories to move.

    Returns:
        None
    """
    if not release_folders:
        print("No release folders to move.")
        return

    for folder in release_folders:
        destination = os.path.join(yearly_path, os.path.basename(folder))

        try:
            if os.path.exists(destination):
                print(f"Skipping: '{destination}' already exists.")
            else:
                shutil.move(folder, destination)
                print(f"Moved: '{folder}' to '{destination}'")
        except Exception as e:
            print(f"Failed to move '{folder}' to '{destination}': {e}")

def copy_template(yearly_path, year):
    """
    Copies the template file `../internal/templates/yearly-releases.qmd` to the
    specified directory, renames it, and returns the path of the newly created file.

    Args:
        yearly_path (str): The path to the year's folder in the releases directory.
        year (str): The year to include in the file name.

    Returns:
        str: The path to the newly created yearly release file.
    """
    template_path = "../internal/templates/yearly-releases.qmd"
    destination_file = f"{yearly_path}{year}-releases.qmd"

    try:
        # Check if the template exists
        if not os.path.exists(template_path):
            print(f"Template file '{template_path}' does not exist.")
            return None

        # Copy the template to the destination
        shutil.copy(template_path, destination_file)
        print(f"Copied ../internal/templates/yearly-releases.qmd template to: '{destination_file}'")

        return destination_file

    except Exception as e:
        print(f"Failed to copy the template: {e}")
        return None
    
def update_template(destination_file, year):
    """
    Updates specific lines in the destination file to replace '0000' with the given year.

    Args:
        destination_file (str): The path to the file to be updated.
        year (str): The year to replace '0000' with in the lines.

    Returns:
        bool: True if the file was updated successfully, False otherwise.
    """
    if not os.path.exists(destination_file):
        print(f"File '{destination_file}' does not exist.")
        return False

    try:
        # Read the file content
        with open(destination_file, 'r') as file:
            content = file.readlines()

        # Track updated lines
        edited_lines = []

        # Update the lines
        updated_content = []
        for i, line in enumerate(content):
            if line.strip() == "# TITLE-MARKER":
                if i + 1 < len(content):
                    content[i + 1] = content[i + 1].replace("0000", year)
                    edited_lines.append(i + 2)

            if line.strip() == "# LISTING-MARKER":
                if i + 1 < len(content):
                    content[i + 1] = content[i + 1].replace("0000", year)
                    edited_lines.append(i + 2)

            if line.strip() == "<!-- EMBED-MARKER -->":
                if i + 1 < len(content):
                    content[i + 1] = content[i + 1].replace("0000", year)
                    edited_lines.append(i + 2)

            updated_content.append(content[i])

        # Write the updated content back to the file
        with open(destination_file, 'w') as file:
            file.writelines(updated_content)

        print(f"Updated '{destination_file}' with the year {year}.\nEdited lines: {edited_lines}.")
        return True

    except Exception as e:
        print(f"Failed to update '{destination_file}': {e}")
        return False
    
release_listings = []
    
def get_release_listings(yearly_path):
    """
    Returns moved releases to add to the yearly release listing.

    Args:
        yearly_path (str): The path to the year folder to search within.

    Returns:
        list: A list of matching subdirectory names, with '/release-notes.qmd' appended to each, sorted by the date in the folder names in descending order.
    """
    global release_listings 
    listing_dir = f"{yearly_path}"

    if not os.path.exists(listing_dir):
        print(f"'{listing_dir}' does not exist.")
        release_listings = []  
        return release_listings

    subdirs = [d for d in os.listdir(listing_dir) if os.path.isdir(os.path.join(listing_dir, d))]

    if subdirs:
        try:
            # Sort subdirs by parsing the date in the folder names
            subdirs = sorted(
                subdirs,
                key=lambda d: datetime.strptime(d, "%Y-%b-%d"),
                reverse=True
            )
        except ValueError:
            print("Some folder names do not match the expected date format (YYYY-MMM-DD). Skipping sorting.")

        # Append '/release-notes.qmd' to each folder name
        subdirs = [os.path.join(d, 'release-notes.qmd') for d in subdirs]
        print(f"Found {len(subdirs)} release notes in {yearly_path}:")
        for note in subdirs:
            print(note)
    else:
        print(f"No folders found in {yearly_path}.")

    release_listings = subdirs
    return release_listings

def update_listing(destination_file, release_listings):
    """
    Updates the destination file by appending the contents of release_listings under the
    '# RELEASE-FILES-MARKER' line.

    Args:
        destination_file (str): The path to the file to be updated.
        release_listings (list of str): List of release listing file paths to append.

    Returns:
        bool: True if the file was updated successfully, False otherwise.
    """
    if not os.path.exists(destination_file):
        print(f"File '{destination_file}' does not exist.")
        return False

    try:
        # Read the file content
        with open(destination_file, 'r') as file:
            content = file.readlines()

        # Track updated lines
        edited_lines = []

        # Update the lines
        updated_content = []
        release_marker_found = False
        for i, line in enumerate(content):
            updated_content.append(line)

            if line.strip() == "# RELEASE-FILES-MARKER":
                release_marker_found = True
                insertion_index = len(updated_content)

                for listing in release_listings:
                    new_line = f"        - {listing}\n"
                    updated_content.append(new_line)
                    edited_lines.append(insertion_index)
                    insertion_index += 1

        if not release_marker_found:
            print("# RELEASE-FILES-MARKER not found in the file.")
            return False

        # Write the updated content back to the file
        with open(destination_file, 'w') as file:
            file.writelines(updated_content)

        print(f"Updated '{destination_file}' with release listings.\nAdded lines: {edited_lines}.")
        return True

    except Exception as e:
        print(f"Failed to update '{destination_file}': {e}")
        return False
    
def update_quarto_yaml(year):
    """Updates the _quarto.yml file to include the new yearly release folder.

    Params:
        year - the year to be used for the folder.
    
    Modifies:
        _quarto.yml file
    """
    yaml_filename = "../site/_quarto.yml"
    temp_yaml_filename = "../site/_quarto_temp.yml"

    # Copy the original YAML file to a temporary file
    shutil.copyfile(yaml_filename, temp_yaml_filename)

    with open(temp_yaml_filename, 'r') as file:
        lines = file.readlines()

    # Use the year from the parameter
    release_file = f"releases/{year}/{year}-releases.qmd"

    with open(yaml_filename, 'w') as file:
        between_markers = False
        modified_lines = []

        for i, line in enumerate(lines):
            if line.strip() == "# MAKE-RELEASE-NOTES-EMBED-MARKER":
                file.write(line)
                file.write(f"        - file: {release_file}\n")
                file.write("          contents:\n")
                between_markers = True
                continue

            if line.strip() == "# CURRENT-YEAR-END-MARKER":
                between_markers = False

            if between_markers:
                modified_lines.append(i + 1)
                file.write("  " + line)  # Add additional indent to lines between markers
            else:
                file.write(line)

        print(f"Modified lines: {modified_lines}")

    # Remove the temporary file
    os.remove(temp_yaml_filename)

    print(f"Added {year} releases folder to the sidebar in _quarto.yml")

def move_year_marker():
    """Updates the _quarto.yml file to relocate the CURRENT-YEAR-END-MARKER.

    Modifies:
        _quarto.yml file
    """
    yaml_filename = "../site/_quarto.yml"
    temp_yaml_filename = "../site/_quarto_temp.yml"

    # Copy the original YAML file to a temporary file
    shutil.copyfile(yaml_filename, temp_yaml_filename)

    with open(temp_yaml_filename, 'r') as file:
        lines = file.readlines()

    modified_lines = {
        "deleted_line": None,
        "inserted_line": None
    }

    with open(yaml_filename, 'w') as file:
        marker_deleted = False

        for line_number, line in enumerate(lines, start=1):
            if line.strip() == "# CURRENT-YEAR-END-MARKER":
                marker_deleted = True
                modified_lines["deleted_line"] = line_number
                continue  # Skip writing this line to effectively delete it

            file.write(line)

            if not marker_deleted and line.strip() == "# MAKE-RELEASE-NOTES-EMBED-MARKER":
                # Insert marker immediately after the specific line
                file.write("        # CURRENT-YEAR-END-MARKER\n")
                modified_lines["inserted_line"] = line_number + 1

    # Remove the temporary file
    os.remove(temp_yaml_filename)

    print(f"Relocated CURRENT-YEAR-END-MARKER in _quarto.yml from line {modified_lines['deleted_line']} to line {modified_lines['inserted_line']}.")

def update_paths(year):
    """
    Replaces occurrences of `releases/{year}-` with `releases/{year}/{year}-` in .qmd and .yml files.

    Args:
        year (str): Year to replace in the text.
    """
    site_dir = f"../site/"
    original_text = f"releases/{year}-"
    new_text = f"releases/{year}/{year}-"

    # List to track modified files
    modified_files = []

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(site_dir):
        for file in files:
            if file.endswith(".qmd") or file.endswith(".yml"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.readlines()

                # Track lines updated
                updated_lines = []

                # Replace the text
                updated_content = []
                for line_num, line in enumerate(content, start=1):
                    updated_line = re.sub(original_text.format(year=year), new_text.format(year=year), line)
                    updated_content.append(updated_line)
                    if line != updated_line:
                        updated_lines.append((line_num, line.strip(), updated_line.strip()))

                # Write back to the file only if changes were made
                if updated_lines:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.writelines(updated_content)
                    modified_files.append((file_path, updated_lines))

    # Print modified files and lines line by line
    for file_path, updates in modified_files:
        print(f"Updated: {file_path}")
        for line_num, before, after in updates:
            print(f"  Line {line_num}:\n    Before: {before}\n    After: {after}")

def search_links(yearly_path):
    """
    Searches for files in a specified directory and looks for a specific text in them.
    Prints the file path, line number, and the line containing the text.
    Also provides a summary of the number of matching files and lines found.

    Parameters:
    - yearly_path (str): The base directory to search in.
    """
    search_dir = f"{yearly_path}"
    search_text = "../"
    matching_files = 0
    total_lines_found = 0

    for root, _, files in os.walk(search_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_has_match = False
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, start=1):
                        if search_text in line:
                            total_lines_found += 1
                            if not file_has_match:
                                file_has_match = True
                                matching_files += 1
                            print(f"File: {file_path}, Line {line_number}: {line.strip()}")
            except (UnicodeDecodeError, FileNotFoundError):
                # Skip files that cannot be opened or read
                continue

    print(f"\nSearch completed: {matching_files} files matched, {total_lines_found} matching lines found.")

def main():
    year = get_year()

    release_folders = []
    get_yearly_releases(year)
    
    yearly_path = create_year_folder(year)
    move_yearly_releases(yearly_path, release_folders)

    yearly_release = copy_template(yearly_path, year)

    if yearly_release:
        update_template(yearly_release, year)


if __name__ == "__main__":
    main()
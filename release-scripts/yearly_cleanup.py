import subprocess
import json
import shutil
import numpy as np
import datetime
import openai
from dotenv import dotenv_values
from collections import defaultdict

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

    print(f"Creating folder for year: {year}\n")
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
        print(f"Copied template to: '{destination_file}'")

        print(f"Yearly release file created:")
        return destination_file

    except Exception as e:
        print(f"Failed to copy the template: {e}")
        return None

def main():
    year = get_year()

    release_folders = []
    get_yearly_releases(year)
    
    yearly_path = create_year_folder(year)
    move_yearly_releases(yearly_path, release_folders)

if __name__ == "__main__":
    main()
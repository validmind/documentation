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
        print(f"Created folder: {yearly_path}")
    
    return yearly_path

release_folders = []

def get_yearly_releases(year):
    """
    Finds subdirectories in ../site/releases/ that begin with the specified year.

    Args:
        year (str): The year prefix to search for in subdirectory names.

    Returns:
        list: A list of matching subdirectory names.
    """
    global release_folders 
    releases_dir = "../site/releases/"

    if not os.path.exists(releases_dir):
        print(f"'{releases_dir}' does not exist.")
        release_folders = []  
        return release_folders

    subdirs = [d for d in os.listdir(releases_dir) if os.path.isdir(os.path.join(releases_dir, d))]
    matching_subdirs = [d for d in subdirs if d.startswith(f"{year}-")]

    if matching_subdirs:
        print(f"Found release folders for year {year}:")
        for folder in matching_subdirs:
            print(f"- {folder}")
    else:
        print(f"No release folders found for year {year}.")

    release_folders = matching_subdirs
    return release_folders

def main():
    year = get_year()
    create_year_folder(year)

if __name__ == "__main__":
    main()
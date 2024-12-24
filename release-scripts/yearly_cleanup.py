import subprocess
import json
import re
import shutil
import numpy as np
import datetime
import openai
from dotenv import dotenv_values
from collections import defaultdict

from datetime import datetime
import os

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

    print(f"Year inputted:")
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

def main():
    get_year()

if __name__ == "__main__":
    main()
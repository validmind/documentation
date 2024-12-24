import subprocess
import json
import re
import shutil
import numpy as np
import datetime
import openai
from dotenv import dotenv_values
import os
from collections import defaultdict

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
        f"Enter the location of your .env file (leave empty for default [{default_year}]): "
    ) or default_year

    print(f"Year inputted: {year}\n")
    return year


def main():
    get_year()

if __name__ == "__main__":
    main()
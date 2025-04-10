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
from IPython import get_ipython
from collections import Counter
import sys

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

class PR:
    def __init__(self, repo_name=None, pr_number=None, title=None, body=None, url=None, labels=None):
        self.repo_name = repo_name
        self.pr_number = pr_number
        self.url = url
        self.data_json = None
        
        self.title = title
        self.cleaned_title = None
        self.pr_body = None
        self.labels = labels if labels is not None else []

        self.generated_lines = None
        self.edited_text = None
        
        self.pr_auto_summary = None
        self.pr_interpreted_summary = None
        self.pr_details = None # final form

    def load_data_json(self):
        """Loads the JSON data from a PR to self.data_json, sets to None if any labels are 'internal'

        Modifies:
            self.data_json
        """
        print(f"Storing data from PR #{self.pr_number} of {self.repo_name} ...\n")
        cmd = ['gh', 'pr', 'view', self.pr_number, '--json', 'title,body,url,labels', '--repo', self.repo_name]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()

        output_clean = ansi_escape.sub('', output)

        try:
            self.data_json = json.loads(output_clean)
        except json.JSONDecodeError:
            print(f"ERROR: Unable to parse PR data for PR number {self.pr_number} in repository {self.repo_name}")
            return None
        
        if any(label['name'] == 'internal' for label in self.data_json['labels']):
            self.data_json = None  # Ignore PRs with the 'internal' label
        
    def extract_external_release_notes(self):
        """Turns the JSON body into lines (str) that are ready for ChatGPT
        
        Modifies: 
            self.pr_body - Contains JSON body
            self.generated_lines - Converted string ready for ChatGPT
        """
        self.pr_body = self.data_json['body']
        match = re.search(r"## External Release Notes(.+)", self.pr_body, re.DOTALL)
        if match:
            extracted_text = match.group(1).strip()
            # Process each line to add an extra '#' if the line starts with three or more '#'
            self.generated_lines = '\n'.join(''.join(['#', line]) if line.lstrip().startswith('###') else line for line in extracted_text.split('\n'))  
            return True
        else:
            return None
        
    def extract_pr_summary_comment(self):
        """Takes the github bot's comment containing an auto-generated summary of the PR.

        Modifies:
            self.pr_auto_summary
        """
        # Run the GitHub CLI command and capture the output
        cmd = f'gh pr view {self.pr_number} --repo {self.repo_name} --comments'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            
            # Extract the content under '# PR Summary' from comments by github-actions
            lines = output.splitlines()
            capture = False
            summary_content = []

            for line in lines:
                if "github-actions" in line:
                    capture = False
                if "# PR Summary" in line:
                    capture = True
                    continue
                if capture:
                    if "## Test Suggestions" in line:
                        break
                    summary_content.append(line)

            # Join and print the captured summary content
            summary = "\n".join(summary_content).strip()
            if summary:
                self.pr_auto_summary = summary
            else:
                print(f"No PR summary found for #{self.pr_number} from {self.repo_name}\n")
        else:
            print(f"Failed to fetch comments: {result.stderr}")

    def convert_summary_to_release_notes(self, editing_instructions):
        """Takes the PR summary and gets ChatGPT to turn them into a release notes format.

        Modifies: self.pr_interpreted_summary
        """
        if self.pr_auto_summary:
            original_text = self.pr_auto_summary

            client = openai.OpenAI() 

            print(f"Processing PR summary #{self.pr_number} from {self.repo_name} ...\n")

            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system", 
                            "content": editing_instructions
                        },
                        {
                            "role": "user", 
                            "content": original_text
                        }
                        ],
                    max_tokens=4096,  # Adjust the token limit as needed
                    frequency_penalty=0.5,  # Modify repetition tendencies
                    presence_penalty=0.5  # Encourage diversity in responses
                )
                self.pr_interpreted_summary = "\n \nGenerated PR summary: \n \n"
                self.pr_interpreted_summary += response.choices[0].message.content
                self.edited_text += self.pr_interpreted_summary

            except Exception as e:
                print(f"\nFailed to edit text with OpenAI: {str(e)}")
                print(f"\n{original_text}\n")

    def edit_text_with_openai(self, isTitle, editing_instructions):
        """Uses OpenAI/ChatGPT to edit our text from self.generated_lines using a prompt (editing_instructions)

        Modifies:
            self.edited_text if isTitle = False
            self.cleaned_title if isTitle = True

        Raises:
            Exception: When our call to OpenAI fails 
        """
        if isTitle:
            original_text = "\n".join(self.title)
        else:
            original_text = "\n".join(self.generated_lines)

        client = openai.OpenAI() 

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system", 
                        "content": editing_instructions
                    },
                    {
                        "role": "user", 
                        "content": original_text
                    }
                    ],
                max_tokens=4096,  # Adjust the token limit as needed
                frequency_penalty=0.5,  # Modify repetition tendencies
                presence_penalty=0.5  # Encourage diversity in responses
            )
            if isTitle:
                self.cleaned_title = response.choices[0].message.content
            else:
                self.edited_text = response.choices[0].message.content

        except Exception as e:
            print(f"\nFailed to edit text with OpenAI: {str(e)}")
            print(f"\n{original_text}\n")

    def clean_title(self, editing_instructions):
        """Cleans title by fixing capitalization and removing special character. Edits with ChatGPT

        Modifies:
            self.cleaned_title
        """
        # Remove text in square brackets, process '/' character, and trim the title
        title = re.sub(r"\[.*?\]", "", self.title)
        print(f"After trimming: {title}\n") #@@@@@@
        parts = title.split('/')
        if len(parts) > 1:
            title = parts[-1].strip()  # Get the part after the last '/'
            if title and title[0].islower():
                title = title[0].upper() + title[1:]  # Capitalize the first letter if it's lowercase

        title = title.strip()
        print(f"After stripping: {title}\n") #@@@@@

        # Edit the pull request title with ChatGPT
        # print(f"ORIGINAL TITLE: {title}")
        # temp = self.generated_lines
        # self.generated_lines = title
        # print(self.generated_lines)
        self.title = title
        
        self.edit_text_with_openai(True, editing_instructions)

        title = self.cleaned_title.rstrip('.')
        self.cleaned_title = title
        print(f"After ChatGPT: {self.cleaned_title}\n") #@@@@@


class ReleaseURL:
    def __init__(self, url):
        self.url = url
        self.repo_name = None # backend
        self.tag_name = None # v.2.0.23
        self.data_json = None
        self.prs = []

    def extract_repo_name(self):
        """Extracts and returns the repository name from the URL."""
        match = re.search(r"github\.com/(.+)/releases/tag/", self.url)
        if not match:
            print(f"ERROR: Invalid URL format '{self.url}'")
            return None
        return match.group(1)

    def set_repo_and_tag_name(self):
        """Sets the repo name (documentation/backend/...) and the release tag from the GitHub URL.

        Modifies:
            self.repo_name
            self.tag_name
        """
        match = re.search(r"github\.com/(.+)/releases/tag/(.+)$", self.url)
        if not match:
            print(f"ERROR: Invalid URL format '{self.url}'")
            return

        self.repo_name, self.tag_name = match.groups()

    def extract_prs(self):
        """Extracts PRs from the release URL.

        Modifies:
            self.prs
            self.data_json
        """
        print(f"Extracting PRs from {self.url} ...\n")
        cmd_release = ['gh', 'api', f'repos/{self.repo_name}/releases/tags/{self.tag_name}']
        result_release = subprocess.run(cmd_release, capture_output=True, text=True)
        output_release = result_release.stdout.strip()

        output_release_clean = ansi_escape.sub('', output_release) # to clean up notebook output

        try:
            self.data_json = json.loads(output_release_clean)
        except json.JSONDecodeError:
            print(f"ERROR: Unable to parse release data for URL '{self.url}'")      
        
        if 'body' in self.data_json:
            body = self.data_json['body']
            pr_numbers = re.findall(r"https://github\.com/.+/pull/(\d+)", body)

            for pr_number in pr_numbers: # initialize PR objects using pr_numbers and add to list of PRs
                curr_PR = PR(self.repo_name, pr_number)
                self.prs.append(curr_PR)
                print(f"PR #{pr_number} retrieved.\n")

        else:
            print(f"ERROR: No body found in release data for URL '{self.url}'")

    def populate_pr_data(self):
        """Helper method. Calls JSON loader on each PR in a URL.
        """
        for pr in self.prs:
            pr.load_data_json()

def get_env_location():
    """
    Asks the user for the location of their .env file.

    Returns:
        str: The provided location or a default value (../.env).
    """
    # Default location of the .env file
    default_env_location = "../.env"

    # Prompt the user for input
    env_location = input(
        f"Enter the location of your .env file (leave empty for default [{default_env_location}]): "
    ) or default_env_location

    print(f"Using .env file location: {env_location}\n")
    return env_location

def setup_openai_api(env_location):
    """
    Loads .env file from the specified location and retrieves the OpenAI API key.

    Args:
        env_location (str): The location of the .env file.

    Raises:
        FileNotFoundError: If the .env file is not found at the specified location.
        KeyError: If the OPENAI_API_KEY is not present in the .env file.
    """
    # Load environment variables from the provided location without affecting os.environ
    config = dotenv_values(env_location)
    if not config:
        raise FileNotFoundError(f".env file not found or is empty at {env_location}")

    # Check for the required key
    api_key = config.get('OPENAI_API_KEY')
    if not api_key:
        raise KeyError(
            f"OPENAI_API_KEY is not set in the .env file at {env_location}"
            "Please ensure the .env file contains this key"
        )

    # Set the API key for the OpenAI library
    print(f"Detected OpenAI API Key in {env_location}")  # Optional debug message
    openai.api_key = api_key

label_to_category = {
    "highlight": "## Release highlights",
    "enhancement": "## Enhancements",
    "breaking-change": "## Breaking changes",
    "deprecation": "## Deprecations",
    "bug": "## Bug fixes",
    "documentation": "## Documentation"
}

categories = { 
    "highlight": [],
    "enhancement": [],
    "breaking-change": [],
    "deprecation": [],
    "bug": [],
    "documentation": []
}

def display_list(array):
    """
    Lists an array in a numbered list. Used to check the `label_hierarchy`.
    """
    print("Set category hierarchy:\n")
    for i, item in enumerate(array, start=1):
        print(f"{i}. {item}")

release_components = {} 

def collect_github_urls(): 
    """Collects release URLs from user.

    Returns:
        List[ReleaseURL]: A list of ReleaseURL objects

    Exits:
        If the user presses enter and no URLs were entered
    """
    urls = []
    seen_urls = set()  # Track unique URLs
    while True:
        url = input("Enter a full GitHub release URL (leave empty to finish): ")
        if not url:
            if not urls:  # Check if no URLs have been added yet
                print("ERROR: You must specify at least one full GitHub release URL")
                exit(1)  # Exit the script with an error code
            break
        if url in seen_urls:
            print(f"ERROR: Duplicate URL '{url}' not added\n")
        else:
            urls.append(ReleaseURL(url))
            seen_urls.add(url)
            print(f"{url} added\n")
    return urls

def count_repos(urls):
    """Counts occurrences of each repository in the given URLs.

    Args:
        urls (List[ReleaseURL]): A list of ReleaseURL objects

    Prints:
        Repository counts in the format 'repo_name: count'
    """
    print("RELEASE TAGS ADDED BY REPO:\n")
    repo_names = [url.extract_repo_name() for url in urls if url.extract_repo_name()]
    
    counts = Counter(repo_names)
    for repo, count in counts.items():
        print(f"{repo}: {count}")

def get_release_date():
    """Sets a release date
    Returns: datetime
        3 business days from today if input is empty
        inputed date if input is not empty and a valid date

    Raises:
        ValueError: When input is not the correct format
    """
    today = datetime.datetime.now().date()
    np_today = np.datetime64(today, 'D')

    # Calculate 3 business days from today. 'forward' means move to the next business day if today is not one.
    three_business_days = np.busday_offset(np_today, 3, roll='forward')
    three_business_days = three_business_days.astype('datetime64[D]').astype(datetime.date)
    default_date = three_business_days.strftime("%B %d, %Y")

    date_input = input(f"Enter the release date (Month Day, Year) (leave empty for default date [{default_date}]): ") or default_date
    try:
        validated_date = datetime.datetime.strptime(date_input, "%B %d, %Y")
        print(f"Release date: {validated_date}\n")
        return validated_date
    except ValueError:
        print("Invalid date format, please try again using the format Month Day, Year (e.g., January 1, 2020)")
        return get_release_date()
    

def input_version():
    """Prompts the user to enter a version number in one of the formats:
    00.00.00, 00.00.0, or 00.00

    Returns:
        str: The validated version string.
    """
    import re
    version_pattern = re.compile(r"^\d{2}\.\d{2}(\.\d{1,2})?$")

    while True:
        version_input = input("Enter the version number (format: 00.00.00, 00.00.0, or 00.00): ")
        if version_pattern.match(version_input):
            print(f"Unified version: {version_input}\n")
            return version_input
        else:
            print("Invalid version format. Please use one of the following: 00.00.00, 00.00.0, or 00.00")
    
def create_release_folder(formatted_release_date):
    """
    Creates a directory for the release notes based on the provided release date
    and returns the output file path.

    Args:
        formatted_release_date (str): The formatted release date string.

    Returns:
        str: The path to the release notes file, or exits the script if the user chooses not to overwrite.
    """
    # Parse the input date
    parsed_date = datetime.datetime.strptime(formatted_release_date, "%Y-%b-%d")
    year = parsed_date.year
    formatted_date = parsed_date.strftime("%Y-%b-%d").lower()  # e.g., "2025-jan-17"
    directory_path = f"../site/releases/{year}/{formatted_date}/"
    output_file = f"{directory_path}release-notes.qmd"

    # Check if the directory and file already exist
    if os.path.exists(directory_path) and os.path.exists(output_file):
        response = input(f"The file {output_file} already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
        if response != "yes":
            print("Release generation canceled, exiting")
            sys.exit(1)  # Exit the script early

    # Create directory and output file
    os.makedirs(directory_path, exist_ok=True)
    print(f"{output_file} will be created or overwritten")

    return output_file, year

def create_release_qmd(output_file, original_release_date, release_date_iso, unified_version):
    """
    Writes metadata to a file with a title set to the original release date,
    and includes the release date in ISO format as the date field.

    Args:
        output_file (str): The path to the file to write.
        original_release_date (str): The title to include in the metadata.
        release_date_iso (str): The date in YYYY-MM-DD format for metadata.
    """

    unified_version = f"Unified version `{input_version()}`"

    print(f"- {original_release_date} added to {output_file} as title")
    print(f"  {release_date_iso} added to {output_file} as date")
    print(f"  {unified_version} added to {output_file} as subtitle")
    with open(output_file, "w") as file:
        file.write(f"---\n")
        file.write(f"title: \"{original_release_date}\"\n")
        file.write(f"date: {release_date_iso}\n")
        file.write(f"subtitle: {unified_version}\n")
        file.write(f"---\n\n")

    try:
        subprocess.run(["code", output_file], check=True)
    except Exception as e:
        print(f"Error opening the file in VS Code: {e}")

def update_release_components(release_components, categories):
    """
    Updates a dictionary of release components with the given categories.

    Parameters:
        release_components (dict): The dictionary to update.
        categories (dict): The categories to add to the release components.

    Returns:
        dict: The updated release components dictionary.
    """
    release_components.update(categories)
    if get_ipython():  # Check if running in Jupyter Notebook
        print(f"Set up {len(release_components)} components:")
    else:
        print(f"Set up {len(release_components)} components:\n" + "\n".join(release_components))
    return release_components

def set_names(github_urls):
    """
    Iterates over a list of URL objects, calling the `set_repo_and_tag_name` method on each.

    Parameters:
        github_urls (list): A list of objects, each having the method `set_repo_and_tag_name`.

    Returns:
        None
    """
    # Mapping of repo names to headers
    repo_to_header = {
        "validmind/frontend": "FRONTEND",
        "validmind/documentation": "DOCUMENTATION",
        "validmind/validmind-library": "VALIDMIND LIBRARY",
    }

    print("Assigning repo and tag names ...\n")

    # Group URLs by repo name for better formatting
    grouped_urls = {}
    for url_obj in github_urls:
        url_obj.set_repo_and_tag_name()
        if url_obj.repo_name not in grouped_urls:
            grouped_urls[url_obj.repo_name] = []
        grouped_urls[url_obj.repo_name].append(url_obj)

    # Print output in the desired format
    for repo_name, urls in grouped_urls.items():
        header = repo_to_header.get(repo_name, repo_name.upper())
        print(f"{header}:\n")
        for url_obj in urls:
            print(f"URL: {url_obj.url}\n Repo name: {url_obj.repo_name}\n Tag name: {url_obj.tag_name}\n")

def extract_urls(github_urls):
    """
    Extracts pull request (PR) objects from a list of GitHub URLs.

    Args:
        github_urls (iterable): An iterable containing GitHub URL objects that 
                               have an `extract_prs` method.

    Returns:
        None: The `extract_prs` method modifies the URL objects in-place.
    """
    for url in github_urls:
        url.extract_prs()
        print()

def populate_data(urls):
    """
    Populates pull request data for a list of URLs.

    Args:
        urls (iterable): An iterable of objects with a `populate_pr_data` method.
    """
    for url in urls:
        url.populate_pr_data()
        print()

def edit_release_notes(github_urls, editing_instructions_body):
    """
    Processes a list of GitHub URLs to extract and edit release notes for pull requests.

    Args:
        github_urls (list): List of GitHub URL objects containing pull requests.
        editing_instructions_body (str): Instructions for editing the text with OpenAI.

    Returns:
        None
    """
    for url in github_urls:
        for pr in url.prs:
            if pr.data_json:
                print(f"Editing content of PR #{pr.pr_number} from {pr.repo_name} ...\n") 
                if pr.extract_external_release_notes():
                    pr.edit_text_with_openai(False, editing_instructions_body)
        print()

def auto_summary(github_urls, summary_instructions):
    """
    Processes GitHub PRs by fetching comments, extracting summaries, and converting 
    summaries to release notes based on given instructions.

    Args:
        github_urls (list): A list of GitHub URLs, each containing PR data.
        summary_instructions (str): Instructions for converting summaries to release notes.
    """
    for url in github_urls:
        for pr in url.prs:
            if pr.data_json:
                print(f"Fetching GitHub comment from PR #{pr.pr_number} of {pr.repo_name}...\n")
                pr.extract_pr_summary_comment()
                pr.convert_summary_to_release_notes(summary_instructions)
        print()

def edit_titles(github_urls, editing_instructions_title):
    """
    Updates the titles of pull requests (PRs) based on provided JSON data and cleaning instructions.

    Parameters:
        github_urls (list): A list of GitHub URLs, each containing PRs to process.
        editing_instructions_title (str): Instructions for cleaning PR titles.

    Returns:
        None
    """
    for url in github_urls:
        for pr in url.prs:
            if pr.data_json:
                print(f"Editing title for PR #{pr.pr_number} in {pr.repo_name}...\n")
                pr.title = pr.data_json['title']
                pr.clean_title(editing_instructions_title)
                print()
        print()

def set_labels(github_urls):
    """
    Processes a list of GitHub URLs and extracts pull request labels, printing them.

    Args:
        github_urls (list): A list of GitHub URL objects, each containing pull requests (prs).
    """
    print(f"Attaching labels to PRs ...\n\n")
    for url in github_urls:
        for pr in url.prs:
            if pr.data_json:
                pr.labels = [label['name'] for label in pr.data_json['labels']]
                print(f"PR #{pr.pr_number} from {pr.repo_name}: {pr.labels}\n")
        print()

def assign_details(github_urls):
    """
    Processes a list of GitHub URLs and extracts details for PRs with data in `data_json`.

    Args:
        github_urls (list): A list of objects representing GitHub URLs, each containing PRs.

    Returns:
        None
    """
    print(f"Compiling PR data ...\n\n")
    for url in github_urls:
        for pr in url.prs:
            if pr.data_json:
                pr.pr_details = {
                    'pr_number': pr.pr_number,
                    'title': pr.cleaned_title,
                    'full_title': pr.data_json['title'],
                    'url': pr.data_json['url'],
                    'labels': ", ".join(pr.labels),
                    'notes': pr.edited_text
                }
                print(f"PR #{pr.pr_number} from {pr.repo_name} compiled.\n")
        print()

def assemble_release(github_urls, label_hierarchy):
    """
    Assigns PRs from a list of GitHub release URLs to release components based on their labels.

    Parameters:
        github_urls (list): A list of GitHub URL objects, each containing PRs.
        label_hierarchy (list): A prioritized list of labels to determine component assignment.

    Returns:
        dict: A dictionary where keys are labels from the hierarchy (or 'other') and values are lists of PR details.
    """
    # Initialize release_components as a defaultdict with lists
    release_components = defaultdict(list)

    # Process PRs and assign them to components based on label hierarchy
    unassigned_prs = []  # Track PRs that do not match any label in the hierarchy

    for url in github_urls:
        for pr in url.prs:
            if pr.data_json:
                print(f"Assembling PR #{pr.pr_number} from {pr.repo_name} for release notes...\n")
                assigned = False
                for priority_label in label_hierarchy:
                    if priority_label in pr.labels:
                        release_components[priority_label].append(pr.pr_details)
                        assigned = True
                        break
                if not assigned:
                    unassigned_prs.append(pr.pr_details)
        print()

    # Add unassigned PRs to the 'other' category
    release_components['other'].extend(unassigned_prs)

    # Convert defaultdict to a regular dict and ensure 'other' is at the end
    result = {label: release_components[label] for label in label_hierarchy if label in release_components}
    if 'other' in release_components:
        result['other'] = release_components['other']

    return result

def release_output(output_file, release_components, label_to_category):
    """
    Appends release notes to the specified file.

    Args:
        output_file (str): Path to the file to append.
        release_components (dict): Release notes categorized by labels.
        label_to_category (dict): Mapping of labels to formatted categories.

    Returns:
        None
    """
    try:
        with open(output_file, "a") as file:
            write_file(file, release_components, label_to_category)
            print(f"Assembled release notes added to {file.name}\n")
    except Exception as e:
        print(f"Failed to write to {output_file}: {e}")

def upgrade_info(output_file):
    """
    Appends the upgrade information single-source to the end of the new release notes.

    Args:
        output_file (str): Path to the file to append.

    Returns:
        None
    """
    include_directive = "\n\n{{< include /releases/_how-to-upgrade.qmd >}}\n"

    try:
        with open(output_file, "a") as file:
            file.write(include_directive)
            print(f"Include _how-to-upgrade.qmd added to {file.name}")
    except Exception as e:
        print(f"Failed to include _how-to-upgrade.qmd to {output_file}: {e}")

# def update_quarto_yaml(release_date, year):
#     """Updates the _quarto.yml file to include the release notes file so it can be accessed on the website.

#     Params:
#         release_date - release notes use the release date as the file name.
    
#     Modifies:
#         _quarto.yml file
#     """
#     yaml_filename = "../site/_quarto.yml"

#     # Format the release date for insertion into the YAML file
#     formatted_release_date = release_date.strftime("%Y-%b-%d").lower()
#     target_line = f'        - releases/{year}/{formatted_release_date}/release-notes.qmd\n'

#     # Check if the target line already exists in the YAML file
#     with open(yaml_filename, 'r') as file:
#         if target_line in file.readlines():
#             print(f"Release notes for {formatted_release_date} already exist in {yaml_filename}, skipping update")
#             return

#     temp_yaml_filename = "../site/_quarto_temp.yml"

#     # Copy the original YAML file to a temporary file
#     shutil.copyfile(yaml_filename, temp_yaml_filename)

#     with open(temp_yaml_filename, 'r') as file:
#         lines = file.readlines()

#     with open(yaml_filename, 'w') as file:
#         add_release_content = False
#         insert_index = -1

#         for i, line in enumerate(lines):
#             file.write(line)
#             if line.strip() == "# MAKE-RELEASE-NOTES-EMBED-MARKER":
#                 add_release_content = True
#                 insert_index = i

#             if add_release_content and i == insert_index:
#                 file.write(target_line)
#                 add_release_content = False

#     # Remove the temporary file
#     os.remove(temp_yaml_filename)
    
#     print(f"Added new release notes to _quarto.yml, line {insert_index + 2}")

def update_release_sidebar(release_date, year):
    """Updates the releases _sidebar.yaml file to include the new yearly release folder.

    Params:
        year - the year to be used for the folder.
    
    Modifies:
        ~/site/releases/_sidebar.yaml file
    """
    yaml_filename = "../site/releases/_sidebar.yaml"
    temp_yaml_filename = "../site/releases/_sidebar_temp.yaml"

    # Format the release date for insertion into the YAML file
    formatted_release_date = release_date.strftime("%Y-%b-%d").lower()
    target_line = f'        - releases/{year}/{formatted_release_date}/release-notes.qmd\n'

    # Check if the target line already exists in the YAML file
    with open(yaml_filename, 'r') as file:
        if target_line in file.readlines():
            print(f"Release notes for {formatted_release_date} already exist in {yaml_filename}, skipping update")
            return

    # Copy the original YAML file to a temporary file
    shutil.copyfile(yaml_filename, temp_yaml_filename)

    with open(temp_yaml_filename, 'r') as file:
        lines = file.readlines()

    with open(yaml_filename, 'w') as file:
        add_release_content = False
        insert_index = -1

        for i, line in enumerate(lines):
            file.write(line)
            if line.strip() == "# MAKE-RELEASE-NOTES-EMBED-MARKER":
                add_release_content = True
                insert_index = i

            if add_release_content and i == insert_index:
                file.write(target_line)
                add_release_content = False

    # Remove the temporary file
    os.remove(temp_yaml_filename)
    
    print(f"Added new release notes to releases _sidebar.yaml, line {insert_index + 2}")

def update_index_qmd(release_date, year):
    """Updates the index.qmd file to include the new releases in `Latest Releases` and removes the oldest release from the list.

    Params:
        release_date - release notes use the release date as the file name.
    
    Modifies:
        index.qmd file
    """

    index_filename = "../site/index.qmd"

    # Format the release date for checking and insertion into the QMD file
    formatted_release_date = release_date.strftime("%Y-%b-%d").lower()
    new_release_entry = f'      - /releases/{year}/{formatted_release_date}/release-notes.qmd\n'

    # Check if the release note already exists
    with open(index_filename, 'r') as file:
        if new_release_entry in file.read():
            print(f"Release notes for {formatted_release_date} already exist. Skipping update.")
            return

    temp_index_filename = "../site/index_temp.qmd"

    # Copy the original QMD file to a temporary file
    shutil.copyfile(index_filename, temp_index_filename)

    with open(temp_index_filename, 'r') as file:
        lines = file.readlines()

    with open(index_filename, 'w') as file:
        add_release_content = False
        insert_index = -1

        for i, line in enumerate(lines):
            file.write(line)
            if line.strip() == "# MAKE-RELEASE-NOTES-LATEST-MARKER":
                add_release_content = True
                insert_index = i

            if add_release_content and i == insert_index:
                file.write(new_release_entry)
                add_release_content = False

    # Remove the temporary file
    os.remove(temp_index_filename)
    
    print(f"Added new release notes to index.qmd, line {insert_index + 2}\n")

    removed_line = None  # To store the line that gets removed

    with open(index_filename, 'r') as file:
        updated_lines = file.readlines()

    with open(index_filename, 'w') as file:
        for i, line in enumerate(updated_lines):
            # Identify the marker line
            if line.strip() == "# MAKE-RELEASE-NOTES-OLDEST-MARKER":
                # Check if the line above exists and starts with a list indicator "-"
                if i > 0 and updated_lines[i - 1].strip().startswith("-"):
                    # Store the line being removed
                    removed_line = updated_lines[i - 1].strip()
                    # Write all lines up to the one before the line to remove
                    file.writelines(updated_lines[:i - 1])
                    # Write the marker and subsequent lines
                    file.writelines(updated_lines[i:])
                    break
        else:
            # If no marker is found, rewrite the file as is
            file.writelines(updated_lines)

    print(f"Removed the oldest release notes entry: '{removed_line}'")

def write_file(file, release_components, label_to_category):
    """Writes each component of the release notes into a file
    Args:
        file - desired file path
        release_components
        label_to_category

    Modifies: 
        file
    """
    for label, release_component in release_components.items():
        if release_component:  # Only write heading if there are PRs
            output_lines = [f"{label_to_category.get(label, '## Other')}\n\n"]
            last_line_was_blank = False

            for pr in release_component:
                pr_lines = [
                    f"<!---\nPR #{pr['pr_number']}: {pr['full_title']}\n",
                    f"URL: {pr['url']}\n",
                    f"Labels: {pr['labels']}\n",
                    f"--->\n### {pr['title']}\n\n"
                ]
                
                if pr['notes']:
                    pr_lines.append(f"{pr['notes']}\n\n")
                
                for line in pr_lines:
                    if line.strip() == "":
                        if last_line_was_blank:
                            continue
                        last_line_was_blank = True
                    else:
                        last_line_was_blank = False
                    output_lines.append(line)

            # Write processed lines to file
            file.writelines(output_lines)

def main():
    """
    Calls all the same functions as the generate-release-notes.ipynb when you run make release-notes.
    """
    try:
        env_location = get_env_location()
        setup_openai_api(env_location)
        print()

        label_hierarchy = ["highlight", "enhancement", "breaking-change", "deprecation", "bug", "documentation"]
        display_list(label_hierarchy)
        print()

        release_components = {}

        github_urls = collect_github_urls()
        count_repos(github_urls)
        print()

        release_datetime = get_release_date()
        formatted_release_date = release_datetime.strftime("%Y-%b-%d").lower()
        original_release_date = release_datetime.strftime("%B %-d, %Y")
        print()

        # Handle potential failure in create_release_folder
        output_file, year = create_release_folder(formatted_release_date)
        if not output_file:  # Ensure the function returns something valid
            raise RuntimeError("Failed to create release folder.")
        print()

        create_release_qmd(output_file, original_release_date, release_datetime.strftime("%Y-%m-%d"))
        print()

        update_release_components(release_components, categories)
        print()

        set_names(github_urls)
        print()

        extract_urls(github_urls)
        print()

        populate_data(github_urls)
        print()

        editing_instructions_body = """
            Please edit the provided technical content according to the following guidelines:
            ... (truncated for brevity)
        """
        edit_release_notes(github_urls, editing_instructions_body)
        print()

        summary_instructions = """
            Please turn this PR Summary into a summary for release notes, according to the following guidelines:
            ... (truncated for brevity)
        """
        auto_summary(github_urls, summary_instructions)
        print()

        editing_instructions_title = """
            Please edit the provided technical content according to the following guidelines:
            ... (truncated for brevity)
        """
        edit_titles(github_urls, editing_instructions_title)
        print()

        set_labels(github_urls)
        print()

        assign_details(github_urls)
        print()

        release_components = assemble_release(github_urls, label_hierarchy)
        print()

        release_output(output_file, release_components, label_to_category)
        upgrade_info(output_file)
        print()

        # update_quarto_yaml(release_datetime, year)
        # print()

        update_release_sidebar(release_datetime, year)
        print()

        update_index_qmd(release_datetime, year)
        print()

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)  # Exit with an error code for failures


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)  # Explicitly exit with success
    except Exception as e:
        print(f"Unhandled error: {e}", file=sys.stderr)
        sys.exit(1)  # Exit with an error code for unhandled exceptions
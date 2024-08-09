import requests
import subprocess
import json
import re
import shutil
import numpy as np
import datetime
import openai
from dotenv import load_dotenv
import os

class PR:
    def __init__(self, repo_name=None, pr_number=None, title=None, body=None, url=None, labels=None):
        self.repo_name = repo_name
        self.pr_number = pr_number
        self.title = title
        self.body = body 
        self.url = url
        self.labels = labels if labels is not None else []
        self.cleaned_title = None
        # self.release_notes = None
        self.data_json = None
        self.pr_body = None
        self.generated_lines = None
        self.edited_text = None
        self.pr_details = None

    def load_data_json(self):
        """Loads the JSON data from a PR to self.data_json, sets to None if any labels are 'internal'

        Modifies:
            self.data_json
        """
        cmd = ['gh', 'pr', 'view', self.pr_number, '--json', 'title,body,url,labels', '--repo', self.repo_name]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()
        try:
            self.data_json = json.loads(output)
        except json.JSONDecodeError:
            print(f"Error: Unable to parse PR data for PR number {self.pr_number} in repository {self.repo_name}.")
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

    def edit_text_with_openai(self, isTitle):
        """Uses OpenAI/ChatGPT to edit our text from self.generated_lines using a prompt (editing_instructions)
        Make editing_instructions global for notebook?

        Modifies:
            self.edited_text

        Raises:
            Exception: When our call to OpenAI fails 
        """
        if isTitle:
            original_text = "\n".join(self.title)
        else:
            original_text = "\n".join(self.generated_lines)

        client = openai.OpenAI() 

        editing_instructions = """
        Please edit the provided technical content according to the following guidelines:

        - Use simple and neutral language in the active voice.
        - Address users directly in the second person with "you".
        - Use present tense by avoiding the use of "will".
        - Apply sentence-style capitalization to text
        - Always capitalize the first letter of text on each line.
        - Rewrite sentences that are longer than 25 words as multiple sentences.
        - Only split text across multiple lines if the text contains more than three sentences.
        - Avoid handwaving references to "it" or "this" by including the text referred to. 
        - Treat short text of less than ten words without a period at the end as a heading. 
        - Enclose any words joined by underscores in backticks (`) if they aren't already.
        - Remove exclamation marks from text.
        - Remove quotes around non-code words.
        - Remove the text "feat:" from the output
        - Maintain existing punctuation at the end of sentences.
        - Maintain all original hyperlinks for reference.
        - Preserve all comments in the format <!--- COMMENT ---> as they appear in the text.
        """

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

    def clean_title(self):
        """Cleans title by fixing capitalization and removing special character. Edits with ChatGPT

        Modifies:
            self.cleaned_title
        """
        # Remove text in square brackets, process '/' character, and trim the title
        title = re.sub(r"\[.*?\]", "", self.title)
        print(title) #@@@@@@
        parts = title.split('/')
        if len(parts) > 1:
            title = parts[-1].strip()  # Get the part after the last '/'
            if title and title[0].islower():
                title = title[0].upper() + title[1:]  # Capitalize the first letter if it's lowercase

        title = title.strip()
        print(title) #@@@@@

        # Edit the pull request title with ChatGPT
        # print(f"ORIGINAL TITLE: {title}")
        # temp = self.generated_lines
        # self.generated_lines = title
        # print(self.generated_lines)
        self.title = title
        self.edit_text_with_openai(True)
        # self.generated_lines = temp
        print(self.cleaned_title) #@@@@@
        title = self.cleaned_title.rstrip('.')
        self.cleaned_title = title


class ReleaseURL:
    def __init__(self, url):
        self.url = url
        self.repo_name = None # backend
        self.tag_name = None # v.2.0.23
        self.data_json = None
        self.prs = []

    def set_repo_and_tag_name(self):
        """Sets the repo name (documentation/backend/...) and the release tag from the GitHub URL.

        Modifies:
            self.repo_name
            self.tag_name
        """
        match = re.search(r"github\.com/(.+)/releases/tag/(.+)$", self.url)
        if not match:
            print(f"Error: Invalid URL format '{self.url}'.")
      
        self.repo_name, self.tag_name = match.groups()

    def extract_prs(self):
        """Extracts PRs from the release URL.

        Modifies:
            self.prs
        """
        cmd_release = ['gh', 'api', f'repos/{self.repo_name}/releases/tags/{self.tag_name}']
        result_release = subprocess.run(cmd_release, capture_output=True, text=True)
        output_release = result_release.stdout.strip()
        try:
            self.data_json = json.loads(output_release)
        except json.JSONDecodeError:
            print(f"Error: Unable to parse release data for URL '{self.release_url}'.")
        
        if 'body' in self.data_json:
            body = self.data_json['body']
            pr_numbers = re.findall(r"https://github\.com/.+/pull/(\d+)", body)

            for pr_number in pr_numbers: # initialize PR objects using pr_numbers and add to list of PRs
                curr_PR = PR(self.repo_name, pr_number)
                self.prs.append(curr_PR)

        else:
            print(f"Error: No body found in release data for URL '{self.release_url}'.")

    def populate_pr_data(self):
        for pr in self.prs:
            pr.load_data_json()

            


def setup_openai_api():
    """Loads .env file and updates the OpenAI API key. 
    
    Replace '../.env' with the relative path to your .env file.

    Modifies:
        openai.api_key
    """
    # Load environment variables
    load_dotenv('../.env') # in the script, update to match the correct path

    # Get the OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise EnvironmentError("OpenAI API key is not set in .env file.")

    # Set the API key for the OpenAI library
    openai.api_key = api_key

def collect_github_urls(): 
    """Collects release URLs from user.

    Returns:
        List[ReleaseURL]: A list of ReleaseURL objects

    Exits:
        If the user presses enter and no URLs were entered
    """
    urls = []
    while True:
        url = input("Enter a full GitHub release URL (leave empty to finish): ")
        if not url:
            if not urls:  # Check if no URLs have been added yet
                print("Error: You must specify at least one full GitHub release URL.")
                exit(1)  # Exit the script with an error code
            break
        urls.append(ReleaseURL(url))
    return urls 


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
        return validated_date
    except ValueError:
        print("Invalid date format. Please try again using the format Month Day, Year (e.g., January 1, 2020).")
        return get_release_date()

def update_quarto_yaml(release_date):
    """Updates the _quarto.yml file to include the release notes file so it can be accessed on the website.

    Params:
        release_date - release notes use the release date as the file name.
    
    Modifies:
        _quarto.yml file
    """
    yaml_filename = "_quarto.yml"
    temp_yaml_filename = "_quarto_temp.yml"

    # Copy the original YAML file to a temporary file
    shutil.copyfile(yaml_filename, temp_yaml_filename)

    with open(temp_yaml_filename, 'r') as file:
        lines = file.readlines()

    # Format the release date for insertion into the YAML file
    formatted_release_date = release_date.strftime("%Y-%b-%d").lower()

    with open(yaml_filename, 'w') as file:
        add_release_content = False
        insert_index = -1

        for i, line in enumerate(lines):
            file.write(line)
            if line.strip() == "# MAKE-RELEASE-NOTES-EMBED-MARKER":
                add_release_content = True
                insert_index = i

            if add_release_content and i == insert_index:
                file.write(f'        - releases/{formatted_release_date}/release-notes.qmd\n')
                add_release_content = False

    # Remove the temporary file
    os.remove(temp_yaml_filename)
    
    print(f"Added release notes to _quarto.yml, line {insert_index + 2}")

def write_prs_to_file(file, release_components, label_to_category):
    """Writes each component of the release notes into a file
    Args:
        file (desired file path)
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
    # Set up the OpenAI API key from the .env file
    setup_openai_api()

    label_to_category = {
        "highlight": "## Release highlights",
        "enhancement": "## Enhancements",
        "deprecation": "## Deprecations",
        "bug": "## Bug fixes",
        "documentation": "## Documentation"
    }
    categories = { 
        "highlight": [],
        "enhancement": [],
        "deprecation": [],
        "bug": [],
        "documentation": []
    }
    label_hierarchy = ["highlight", "deprecation", "bug", "enhancement", "documentation"]

    github_urls = collect_github_urls() # the only big global variable
    
    release_datetime = get_release_date()
    formatted_release_date = release_datetime.strftime("%Y-%b-%d").lower()
    original_release_date = release_datetime.strftime("%B %-d, %Y")

    directory_path = f"releases/{formatted_release_date}/"
    os.makedirs(directory_path, exist_ok=True)
    output_file = f"{directory_path}release-notes.qmd"

    print("Generating & editing release notes ...")

    with open(output_file, "w") as file:
        file.write(f"---\ntitle: \"{original_release_date}\"\n---\n\n")

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    iterate through github urls
    in each url, iterate through each pr
    assign stuff from pr data into pr details
    append pr details to the release components, placement depends on priority
    """
    # Define label to category mapping and other structures
    # for url in github_urls:
    #     repo_name, pr_numbers = get_pr_numbers_from_url(url)
    #     for pr_number in pr_numbers:
    #         pr_data = get_pr_data(repo_name, pr_number) 
    #         print(f"  Processing {repo_name}/#{pr_number} ...")
    #         if pr_data: 
    #             release_notes = extract_external_release_notes(pr_data['body']) # 1 & 2 (edit step)
    #             cleaned_title = clean_title(pr_data['title']) # 3
    #             labels = [label['name'] for label in pr_data['labels']] # 4
    #             pr_details = { # 5
    #                 'pr_number': pr_number,
    #                 'title': cleaned_title,
    #                 'full_title': pr_data['title'],
    #                 'url': pr_data['url'],
    #                 'labels': ", ".join(labels),
    #                 'notes': release_notes
    #             }

    #             assigned = False # 6
    #             for priority_label in label_hierarchy:
    #                 if priority_label in labels:
    #                     categories[priority_label].append(pr_details)
    #                     assigned = True
    #                     break
    #             if not assigned:
    #                 categories.setdefault('other', []).append(pr_details)

    # new one starts here
    release_components = dict()
    release_components.update(categories)

    for url in github_urls:
        url.set_repo_and_tag_name() 

    for url in github_urls:
        url.extract_prs() # initializes PR objects into a list for each URL

    for url in github_urls:
        url.populate_pr_data() # loads json file into object

    for url in github_urls:
        for pr in url.prs:
            if pr.data_json: 
                if pr.extract_external_release_notes(): pr.edit_text_with_openai(False)

    for url in github_urls:
        for pr in url.prs:
            if pr.data_json: 
                pr.title = pr.data_json['title']
                pr.clean_title()

    for url in github_urls:
        for pr in url.prs:
            if pr.data_json: pr.labels = [label['name'] for label in pr.data_json['labels']]

    for url in github_urls:
        for pr in url.prs:
            if pr.data_json: pr.pr_details = {
                'pr_number': pr.pr_number,
                'title': pr.cleaned_title,
                'full_title': pr.data_json['title'],
                'url': pr.data_json['url'],
                'labels': ", ".join(pr.labels),
                'notes': pr.edited_text
            }

    for url in github_urls:
        for pr in url.prs:
            if pr.data_json:
                assigned = False 
                for priority_label in label_hierarchy:
                    if priority_label in pr.labels:
                        release_components[priority_label].append(pr.pr_details)
                        assigned = True
                        break
                if not assigned:
                    release_components.setdefault('other', []).append(pr.pr_details)

    


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Write categorized PRs to the file
    with open(output_file, "a") as file:
        write_prs_to_file(file, release_components, label_to_category)

    update_quarto_yaml(release_datetime)

    # After completing all tasks, print git status to show output files
    try:
        result = subprocess.run(["git", "status", "--short"], check=True, text=True, capture_output=True)
        lines = result.stdout.split('\n')
        print("Files to commit:")
        for line in lines:
            if line.startswith((' M', '??', 'A ')):
                print(line)
    except subprocess.CalledProcessError as e:
        print("Failed to run git status:", e)

if __name__ == "__main__":
    main()

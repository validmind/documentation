import os
import requests
import subprocess
import json
import re
import shutil
import numpy as np
import datetime

def collect_github_urls():
    urls = []
    while True:
        url = input("Enter a full GitHub release URL (leave empty to finish): ")
        if not url:
            if not urls:  # Check if no URLs have been added yet
                print("Error: You must specify at least one full GitHub release URL.")
                exit(1)  # Exit the script with an error code
            break
        urls.append(url)
    return urls

def get_pr_numbers_from_url(release_url):
    match = re.search(r"github\.com/(.+)/releases/tag/(.+)$", release_url)
    if not match:
        print(f"Error: Invalid URL format '{release_url}'.")
        return [], []
    
    repo_name, tag_name = match.groups()
    cmd_release = ['gh', 'api', f'repos/{repo_name}/releases/tags/{tag_name}']
    result_release = subprocess.run(cmd_release, capture_output=True, text=True)
    output_release = result_release.stdout.strip()
    try:
        release_data = json.loads(output_release)
    except json.JSONDecodeError:
        print(f"Error: Unable to parse release data for URL '{release_url}'.")
        return repo_name, []
    
    if 'body' in release_data:
        body = release_data['body']
        pr_numbers = re.findall(r"https://github\.com/.+/pull/(\d+)", body)
        return repo_name, set(pr_numbers)
    else:
        print(f"Error: No body found in release data for URL '{release_url}'.")
        return repo_name, []

def get_pr_data(repo_name, pr_number):
    cmd = ['gh', 'pr', 'view', pr_number, '--json', 'title,body,url,labels', '--repo', repo_name]
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    try:
        pr_data = json.loads(output)
    except json.JSONDecodeError:
        print(f"Error: Unable to parse PR data for PR number {pr_number} in repository {repo_name}.")
        return None
    
    if any(label['name'] == 'internal' for label in pr_data['labels']):
        return None  # Ignore PRs with the 'internal' label
    return pr_data

def extract_external_release_notes(pr_body):
    match = re.search(r"## External Release Notes(.+)", pr_body, re.DOTALL)
    if match:
        extracted_text = match.group(1).strip()
        # Process each line to add an extra '#' if the line starts with three or more '#'
        modified_text = '\n'.join(''.join(['#', line]) if line.lstrip().startswith('###') else line for line in extracted_text.split('\n'))
        return modified_text
    return None

def clean_title(title):
    # Remove text in square brackets, process '/' character, and trim the title
    title = re.sub(r"\[.*?\]", "", title)
    parts = title.split('/')
    if len(parts) > 1:
        title = parts[-1].strip()  # Get the part after the last '/'
        if title and title[0].islower():
            title = title[0].upper() + title[1:]  # Capitalize the first letter if it's lowercase
    return title.strip()

def get_release_date():
    today = datetime.datetime.now().date()
    np_today = np.datetime64(today, 'D')

    # Calculate 3 business days from today. 'forward' means move to the next business day if today is not one.
    three_business_days = np.busday_offset(np_today, 3, roll='forward')
    three_business_days = three_business_days.astype('datetime64[D]').astype(datetime.date)
    default_date = three_business_days.strftime("%B %d, %Y")

    date_input = input(f"Enter the release date (Month Day, Year) [{default_date}]: ") or default_date
    try:
        validated_date = datetime.datetime.strptime(date_input, "%B %d, %Y")
        return validated_date
    except ValueError:
        print("Invalid date format. Please try again using the format Month Day, Year (e.g., January 1, 2020).")
        return get_release_date()

def update_quarto_yaml(output_file, release_date):
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

def write_prs_to_file(file, categories, label_to_category):
    for label, pr_list in categories.items():
        if pr_list:  # Only write heading if there are PRs
            output_lines = [f"{label_to_category.get(label, '## Other')}\n\n"]
            last_line_was_blank = False

            for pr in pr_list:
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

    github_urls = collect_github_urls()
    
    release_datetime = get_release_date()
    formatted_release_date = release_datetime.strftime("%Y-%b-%d").lower()
    original_release_date = release_datetime.strftime("%B %-d, %Y")

    directory_path = f"releases/{formatted_release_date}/"
    os.makedirs(directory_path, exist_ok=True)
    output_file = f"{directory_path}release-notes.qmd"

    print("Generating release notes...")

    with open(output_file, "w") as file:
        file.write(f"---\ntitle: \"{original_release_date}\"\n---\n\n")
    
    # Define label to category mapping and other structures
    for url in github_urls:
        repo_name, pr_numbers = get_pr_numbers_from_url(url)
        if pr_numbers:
            for pr_number in pr_numbers:
                pr_data = get_pr_data(repo_name, pr_number)
                if pr_data:
                    release_notes = extract_external_release_notes(pr_data['body'])
                    cleaned_title = clean_title(pr_data['title'])
                    labels = [label['name'] for label in pr_data['labels']]
                    pr_details = {
                        'pr_number': pr_number,
                        'title': cleaned_title,
                        'full_title': pr_data['title'],
                        'url': pr_data['url'],
                        'labels': ", ".join(labels),
                        'notes': release_notes
                    }

                    assigned = False
                    for priority_label in label_hierarchy:
                        if priority_label in labels:
                            categories[priority_label].append(pr_details)
                            assigned = True
                            break
                    if not assigned:
                        categories.setdefault('other', []).append(pr_details)

    # Write categorized PRs to the file
    with open(output_file, "a") as file:
        write_prs_to_file(file, categories, label_to_category)

    update_quarto_yaml(output_file, release_datetime)

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

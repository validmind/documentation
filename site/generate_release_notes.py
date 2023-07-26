import os
import re
import shutil
import subprocess
import json
from datetime import datetime

# Get the list of PR numbers for a specified release from Github from the documentation repo
def get_documentation_pr_numbers(tag_name_documentation):
    cmd_release = ['gh', 'api', f'repos/validmind/documentation/releases/tags/{tag_name_documentation}']
    result_release = subprocess.run(cmd_release, capture_output=True, text=True)
    output_release = result_release.stdout.strip()
    release_data = json.loads(output_release)

# Extract a list of PR numbers in this release
    if 'body' in release_data:
        body = release_data['body']
        documentation_pr_numbers = re.findall(r"https://github.com/validmind/documentation/pull/(\d+)", body)
        # Remove duplicates
        documentation_pr_numbers = set(documentation_pr_numbers)
        return documentation_pr_numbers
    else:
        print(f"Error: Unable to fetch pull request numbers for the release with tag '{tag_name_documentation}'.")
        exit()

# Get the list of PR numbers for a specified release from Github from the validmind-python repo
def get_python_pr_numbers(tag_name_python):
    cmd_release = ['gh', 'api', f'repos/validmind/validmind-python/releases/tags/{tag_name_python}']
    result_release = subprocess.run(cmd_release, capture_output=True, text=True)
    output_release = result_release.stdout.strip()
    release_data = json.loads(output_release)

    # Extract a list of PR numbers in this release
    if 'body' in release_data:
        body = release_data['body']
        python_pr_numbers = re.findall(r"https://github.com/validmind/validmind-python/pull/(\d+)", body)
        # Remove duplicates
        python_pr_numbers = set(python_pr_numbers)
        return python_pr_numbers
    else:
        print(f"Error: Unable to fetch pull request numbers for the release with tag '{tag_name_python}' in validmind-python.")
        exit()

# Get the list of PR numbers for a specified release from Github from the frontend repo
def get_frontend_pr_numbers(tag_name_frontend):
    cmd_release = ['gh', 'api', f'repos/validmind/frontend/releases/tags/{tag_name_frontend}']
    result_release = subprocess.run(cmd_release, capture_output=True, text=True)
    output_release = result_release.stdout.strip()
    release_data = json.loads(output_release)

    # Extract a list of PR numbers in this release
    if 'body' in release_data:
        body = release_data['body']
        frontend_pr_numbers = re.findall(r"https://github.com/validmind/frontend/pull/(\d+)", body)
        # Remove duplicates
        frontend_pr_numbers = set(frontend_pr_numbers)
        return frontend_pr_numbers
    else:
        print(f"Error: Unable to fetch pull request numbers for the release with tag '{tag_name_python}' in frontend.")
        exit()

# Get the PR title and body using the list of PR numbers from the documentation repo
def get_documentation_pr_data(documentation_pull_request_number):
    cmd = ['gh', 'pr', 'view', str(documentation_pull_request_number), '--json', 'title,number,body,labels']
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    documentation_pr_data = json.loads(output)
    documentation_labels = documentation_pr_data.get('labels', [])
    return documentation_pr_data, documentation_labels

# Get the PR title and body using the list of PR numbers from the validmind-python repo
def get_python_pr_data(python_pull_request_number):
    cmd = ['gh', 'pr', '--repo', 'github.com/validmind/validmind-python', 'view', str(python_pull_request_number), '--json', 'title,number,body,labels']
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    python_pr_data = json.loads(output)
    python_labels = python_pr_data.get('labels', [])
    return python_pr_data, python_labels

# Get the PR title and body using the list of PR numbers from the frontend repo
def get_frontend_pr_data(frontend_pull_request_number):
    cmd = ['gh', 'pr', '--repo', 'github.com/validmind/frontend', 'view', str(frontend_pull_request_number), '--json', 'title,number,body,labels']
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    frontend_pr_data = json.loads(output)
    frontend_labels = frontend_pr_data.get('labels', [])
    return frontend_pr_data, frontend_labels

# Extract the section of the PR root comment after '## External Release Notes' from the full PR body in the txt file
def extract_external_release_notes(pr_body):
    match = re.search(r"## External Release Notes(.+)", pr_body, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

# Adds PRs labeled 'highlight' to the release highlights template file. PRs from documentation are written under '## Release Highlights', validmind-python under
# 'ValidMind Developer Framework', and frontend under 'ValidMind Platform UI'
def update_release_highlights_template(template_filepath, documentation_highlight_pull_requests, python_highlight_pull_requests, frontend_highlight_pull_requests):
   
    with open(template_filepath, 'r') as file:
        template_content = file.read()

    documentation_release_notes = ""
    python_release_notes = ""
    frontend_release_notes = ""

    for pr in documentation_highlight_pull_requests:
        title = pr['title']
        external_notes = extract_external_release_notes(pr['body'])
        if external_notes:
            documentation_release_notes += f"- **{title}**\n\n{external_notes}\n\n"

    for pr in python_highlight_pull_requests:
        title = pr['title']
        external_notes = extract_external_release_notes(pr['body'])
        if external_notes:
            python_release_notes += f"- **{title}**\n\n{external_notes}\n\n"

    for pr in frontend_highlight_pull_requests:
        title = pr['title']
        external_notes = extract_external_release_notes(pr['body'])
        if external_notes:
            frontend_release_notes += f"- **{title}**\n\n{external_notes}\n\n"

    # Update the section for PRs from the documentation repo
    template_content = re.sub(r"(?<=## Release highlights\n\n).*?(?=\n..)", documentation_release_notes, template_content, flags=re.DOTALL)

    # Add the section for PRs from the validmind-python repo
    template_content = re.sub(r"(?<=### ValidMind Developer Framework \(version number\)\n\n).*?(?=\n..)", python_release_notes, template_content, flags=re.DOTALL)

    # Add the section for PRs from the validmind-python repo
    template_content = re.sub(r"(?<=### ValidMind Platform UI\n\n).*?(?=\n..)", frontend_release_notes, template_content, flags=re.DOTALL)

    template_content = template_content.replace("Release date", release_date)
    template_content = template_content.replace("version number", tag_name_python)

    with open(template_filepath, 'w') as file:
        file.write(template_content)

# Checks in a PR has the 'internal' label, and if not, writes the PR information to the relevant qmd files
def write_documentation_prs_to_qmd_files(pr_number, documentation_highlight_pull_requests):
    pr_data, labels = get_documentation_pr_data(pr_number)
    if labels:
        skip_pr = False
        for label in labels:
            label_name = label['name'].lower()
            if label_name == 'internal':
                skip_pr = True
                break

        if not skip_pr:
            for label in labels:
                label_name = label['name'].lower()
                if label_name in qmd_files:
                    external_release_notes = extract_external_release_notes(pr_data['body'])
                    if external_release_notes:
                        qmd_files[label_name] += f"- **{pr_data['title']}**\n\n{external_release_notes}\n\n\n"
                # Adds the PR to the highlights list if it has the 'highlight' label
                if label_name == "highlight":
                    documentation_highlight_pull_requests.append(pr_data)
                    return documentation_highlight_pull_requests

# Checks in a PR has the 'internal' label, and if not, writes the PR information to the relevant qmd files
def write_python_prs_to_qmd_files(pr_number, python_highlight_pull_requests):
    pr_data, labels = get_python_pr_data(pr_number)
    if labels:
        skip_pr = False
        for label in labels:
            label_name = label['name'].lower()
            if label_name == 'internal':
                skip_pr = True
                break

        if not skip_pr:
            for label in labels:
                label_name = label['name'].lower()
                if label_name in qmd_files:
                    external_release_notes = extract_external_release_notes(pr_data['body'])
                    if external_release_notes:
                        qmd_files[label_name] += f"- **{pr_data['title']}**\n\n{external_release_notes}\n\n\n"
                # Adds the PR to the highlights list if it has the 'highlight' label
                if label_name == "highlight":
                    python_highlight_pull_requests.append(pr_data)
                    return python_highlight_pull_requests

# Checks in a PR has the 'internal' label, and if not, writes the PR information to the relevant qmd files
def write_frontend_prs_to_qmd_files(pr_number, frontend_highlight_pull_requests):
    pr_data, labels = get_frontend_pr_data(pr_number)
    if labels:
        skip_pr = False
        for label in labels:
            label_name = label['name'].lower()
            if label_name == 'internal':
                skip_pr = True
                break

        if not skip_pr:
            for label in labels:
                label_name = label['name'].lower()
                if label_name in qmd_files:
                    external_release_notes = extract_external_release_notes(pr_data['body'])
                    if external_release_notes:
                        qmd_files[label_name] += f"- **{pr_data['title']}**\n\n{external_release_notes}\n\n\n"
                # Adds the PR to the highlights list if it has the 'highlight' label
                if label_name == "highlight":
                    frontend_highlight_pull_requests.append(pr_data)
                    return frontend_highlight_pull_requests
                
# Creates qmd files for each label if PRs for that label exist. Scans through txt file and checks the label of each PR and if it was merged after the latest tagged commit.
# Writes the formatted PR title and body to the qmd file
def generate_qmd_files(qmd_files, release_folder, documentation_pr_numbers, python_pr_numbers, frontend_pr_numbers, release_date):

    documentation_highlight_pull_requests = []
    python_highlight_pull_requests = []
    frontend_highlight_pull_requests = []

    release_date = release_date.title()

    for pr_number in documentation_pr_numbers:
        write_documentation_prs_to_qmd_files(pr_number, documentation_highlight_pull_requests)

    for pr_number in python_pr_numbers:
        write_python_prs_to_qmd_files(pr_number, python_highlight_pull_requests)

    for pr_number in frontend_pr_numbers:
        write_frontend_prs_to_qmd_files(pr_number, frontend_highlight_pull_requests)

    # Renames the titles and headings of the qmd files
    for label, release_notes in qmd_files.items():
        if label != "highlight":
            if release_notes:
                qmd_filename = f"{label.replace(' ', '-').lower()}.qmd"
                qmd_filepath = os.path.join(release_folder, qmd_filename)
                with open(qmd_filepath, 'w') as file:
                    file.write("---\n")
                    if label == "bug":
                        file.write("title: \"Bug fixes\"\n")
                    elif label == "documentation":
                        file.write("title: \"Documentation updates\"\n")
                    elif label == "enhancement":
                        file.write("title: \"Enhancements\"\n")
                    else:
                        file.write(f"title: \"{label.capitalize()}\"\n")
                    file.write("keywords: \"release notes, model risk management, ValidMind\"\n")
                    file.write("---\n\n")
                    if label == "bug":
                        file.write(f"## Bug fixes -- {release_date}\n\n")
                    elif label == "documentation":
                        file.write(f"## Documentation updates -- {release_date}\n\n")
                    elif label == "enhancement":
                        file.write(f"## Enhancements -- {release_date}\n\n")
                    else:
                        file.write(f"## {label.capitalize()} -- {release_date}\n\n")
                    file.write(release_notes)

    # Copy the template file from the templates folder
    template_filename = "release_highlights_template.qmd"
    copied_template_filename = "highlights.qmd"
    template_filepath = os.path.join("..", "templates", template_filename)

    # Update the path for the copied template in the releases folder
    copied_template_filepath = os.path.join(release_folder, copied_template_filename)

    shutil.copyfile(template_filepath, copied_template_filepath)

    update_release_highlights_template(copied_template_filepath, documentation_highlight_pull_requests, python_highlight_pull_requests, frontend_highlight_pull_requests)

# Adds the copied release highlights file and the qmd files to the _quarto.yml file under the release date
def update_quarto_yaml(qmd_files, release_date):
    yaml_filename = "_quarto.yml"
    temp_yaml_filename = "_quarto_temp.yml"

    shutil.copyfile(yaml_filename, temp_yaml_filename)

    with open(temp_yaml_filename, 'r') as file:
        lines = file.readlines()

    release_date = release_date.title()

    with open(yaml_filename, 'w') as file:
        add_release_content = False
        insert_index = -1

        for i, line in enumerate(lines):
            file.write(line)

            if line.strip() == "- text: \"Releases\"":
                add_release_content = True
                insert_index = i + 1

            if add_release_content and i == insert_index:
                formatted_release_date = datetime.strptime(release_date, "%B %d, %Y").strftime("%Y-%b-%d").lower()
                file.write(f'            - text: "{release_date}"\n')
                file.write(f'              contents:\n')
                file.write(f'                - text: "Release Highlights"\n')
                file.write(f'                  file: releases/{formatted_release_date}/highlights.qmd\n')

                if qmd_files["enhancement"]:
                    file.write(f'                - text: "Enhancements"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/enhancement.qmd\n')

                if qmd_files["bug"]:
                    file.write(f'                - text: "Bug fixes"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/bug.qmd\n')

                if qmd_files["deprecation"]:
                    file.write(f'                - text: "Deprecations"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/deprecation.qmd\n')

                if qmd_files["documentation"]:
                    file.write(f'                - text: "Documentation updates"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/documentation.qmd\n')

                add_release_content = False

    os.remove(temp_yaml_filename)

if __name__ == '__main__':
    # Get the path of the cloned repository
    repo_path = os.path.join(os.getcwd())

    os.chdir(repo_path)  # Change the current working directory to the cloned repository path

    tag_name_documentation = input("Enter the release tag for the documentation repo: ")
    tag_name_documentation = tag_name_documentation.strip()

    tag_name_python = input("Enter the release tag for the validmind-python repo: ")
    tag_name_python = tag_name_python.strip()

    tag_name_frontend = input("Enter the release tag for the frontend repo: ")
    tag_name_frontend = tag_name_frontend.strip()

    release_date = input("Enter the release date (<month> <day>, <year>): ")
    formatted_release_date = datetime.strptime(release_date, "%B %d, %Y").strftime("%Y-%b-%d").lower()
    
    # Creates a new folder under 'releases'
    release_folder = os.path.join("releases", formatted_release_date)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    print("Extracting pull request data ...")

    documentation_pr_numbers = get_documentation_pr_numbers(tag_name_documentation)
    python_pr_numbers = get_python_pr_numbers(tag_name_python)
    frontend_pr_numbers = get_frontend_pr_numbers(tag_name_frontend)

    qmd_files = {
        "enhancement": "",
        "bug": "",
        "deprecation": "",
        "documentation": ""
    }

    os.makedirs(release_folder, exist_ok=True)

    print("Writing pull request data to QMD files ...")

    generate_qmd_files(qmd_files, release_folder, documentation_pr_numbers, python_pr_numbers, frontend_pr_numbers, release_date)

    print("Updating _quarto.yaml file ...")

    update_quarto_yaml(qmd_files, release_date)

    print("Release notes process successful.")

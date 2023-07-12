import os
import re
import shutil
import subprocess
import json
from datetime import datetime

# Get the tag name and time
def get_tag_info():
    # Get the most recent tag name
    cmd_tag_name = ['gh', 'api', 'repos/validmind/validmind-python/tags', '--jq', '.[0].name']
    result_tag_name = subprocess.run(cmd_tag_name, capture_output=True, text=True)
    tag_name = result_tag_name.stdout.strip()

    # Get the commit SHA associated with the most recent tag
    cmd_commit_sha = ['gh', 'api', f'repos/validmind/validmind-python/git/matching-refs/tags/{tag_name}', '--jq', '.[].object.sha']
    result_commit_sha = subprocess.run(cmd_commit_sha, capture_output=True, text=True)
    tag_sha = result_commit_sha.stdout.strip()

    # Get the time for the commit associated with the most recent tag
    cmd_commit_time = ['gh', 'api', f'repos/validmind/validmind-python/git/commits/{tag_sha}', '--jq', '.committer.date']
    result_commit_time = subprocess.run(cmd_commit_time, capture_output=True, text=True)
    tag_time = result_commit_time.stdout.strip()[:10] # Truncate the date

    return tag_name, tag_time

# Get the title, number, and root comment for the 30 most recent PRs
def get_merged_pull_requests():
    cmd = ['gh', 'pr', '--repo', 'validmind/validmind-python', 'list', '--state', 'merged', '--json', 'title,number,body', '--limit', '30']
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf8")
    output = result.stdout.strip()
    pr_data = json.loads(output)
    return pr_data

# Get the label(s) associated with PRs
def get_labels(pull_request_number):
    cmd = ['gh', 'pr', '--repo', 'validmind/validmind-python', 'view', str(pull_request_number), '--json', 'labels']
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    labels_data = json.loads(output)
    labels = labels_data['labels']
    return labels

# Get the time that the PRs were merged to compare to the tagged commit time
def get_merged_at(pull_request_number):
    cmd = ['gh', 'pr', '--repo', 'validmind/validmind-python', 'view', str(pull_request_number), '--json', 'mergedAt']
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf8")
    output = result.stdout.strip()
    merge_time_data = json.loads(output)
    merge_time = merge_time_data['mergedAt'][:10] # Truncate so only the date is printed
    return merge_time

# Extract the section of the PR root comment after '## External Release Notes' from the full PR body in the txt file
def extract_external_release_notes(pr_body):
    match = re.search(r"## External Release Notes(.+)", pr_body, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

# Writes in the titles and extracted comments of PRs with the 'highlight' to the release highlights template
# Adds 'highlight' PRs from the python repo to '## Release highlights'
# Adds 'highlight' PRs from the validmind-python repo to '## ValidMind Developer Framework'
# Adds 'highlight' PRs from the frontend repo to '## ValidMind Platform UI'
def update_release_highlights_template(template_filepath, pull_requests):
    with open(template_filepath, 'r') as file:
        template_content = file.read()

    release_notes = ""
    for pr in pull_requests:
        title = pr['title']
        external_notes = extract_external_release_notes(pr['body'])
        if external_notes:
            release_notes += f"- **{title}**\n\n{external_notes}\n\n"

    template_content = re.sub(r"(?<=## Release highlights\n\n).*?(?=\n###)", release_notes, template_content, flags=re.DOTALL)

    with open(template_filepath, 'w') as file:
        file.write(template_content)

# Creates qmd files for each label if PRs for that label exist. Scans through txt file and checks the label of each PR and if it was merged after the latest tagged commit.
# Writes the formatted PR title and body to the qmd file
def generate_qmd_files(qmd_files, release_folder, formatted_date, merged_pull_requests, tag_time, release_date, tag_name):
    highlight_pull_requests = []
    for pr in merged_pull_requests:
        merged_at = get_merged_at(pr['number'])
        if merged_at >= tag_time:
            labels = get_labels(pr['number'])
            if labels:
                for label in labels:
                    label_name = label['name'].lower()
                    if label_name in qmd_files:
                        # print(label_name) only recognized bug and enhancement
                        external_release_notes = extract_external_release_notes(pr['body'])
                        if external_release_notes:
                            qmd_files[label_name] += f"- **{pr['title']}**\n\n{external_release_notes}\n\n\n"
                    
                    if label_name == "highlight":
                        highlight_pull_requests.append(pr)

    release_date = release_date.title()

    # Renames the titles and headings of the qmd files
    for label, release_notes in qmd_files.items():
        print("entering loop")
        if label != "highlight":
            print("label is not higlight")
            if release_notes:
                print("there are release notes")
                qmd_filename = f"{label.replace(' ', '-').lower()}.qmd"
                qmd_filepath = os.path.join(release_folder, qmd_filename)
                with open(qmd_filepath, 'w') as file:
                    file.write("---\n")
                    print("FILEWRITE")
                    if label == "bug":
                        file.write("title: \"Bug fixes\"\n")
                    elif label == "python":
                        print("PYTHON!")
                        file.write("title: \"Python updates\"\n")
                    elif label == "enhancement":
                        file.write("title: \"Enhancements\"\n")
                    else:
                        file.write(f"title: \"{label.capitalize()}\"\n")
                    file.write("keywords: \"release notes, model risk management, ValidMind\"\n")
                    file.write("---\n\n")
                    if label == "bug":
                        file.write(f"## Bug fixes -- {release_date}\n\n")
                    elif label == "python":
                        print("PYTHON!")
                        file.write(f"## Python updates -- {release_date}\n\n")
                    elif label == "enhancement":
                        file.write(f"## Enhancements -- {release_date}\n\n")
                    else:
                        file.write(f"## {label.capitalize()} -- {release_date}\n\n")
                    file.write(release_notes)

    # Copies release_highlights_template.qmd to the releases folder and writes in content from 'highlight' label
    template_filename = "release_highlights_template.qmd"
    template_filepath = os.path.join(release_folder, f"release-notes-{formatted_date}.qmd")
    shutil.copyfile(template_filename, template_filepath)
    with open(template_filepath, 'r') as file:
        template_content = file.read()

    template_content = template_content.replace("Release date", release_date)
    template_content = template_content.replace("version number", tag_name)

    with open(template_filepath, 'w') as file:
        file.write(template_content)

    update_release_highlights_template(template_filepath, highlight_pull_requests)

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
                file.write(f'                  file: releases/{formatted_release_date}/release-notes-{formatted_release_date}.qmd\n')

                if qmd_files["enhancement"]:
                    file.write(f'                - text: "Enhancements"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/enhancement.qmd\n')

                if qmd_files["bug"]:
                    file.write(f'                - text: "Bug fixes"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/bug.qmd\n')

                if qmd_files["deprecation"]:
                    file.write(f'                - text: "Deprecations"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/deprecation.qmd\n')

                if qmd_files["python"]:
                    file.write(f'                - text: "Python updates"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/python.qmd\n')

                add_release_content = False

    os.remove(temp_yaml_filename)

if __name__ == '__main__':
    # Get the path of the cloned repository
    repo_path = os.path.join(os.getcwd())

    os.chdir(repo_path)  # Change the current working directory to the cloned repository path

    release_date = input("Enter the release date (<month> <day>, <year>): ")
    formatted_release_date = datetime.strptime(release_date, "%B %d, %Y").strftime("%Y-%b-%d").lower()
    
    # Creates a new folder under 'releases'
    release_folder = os.path.join("releases", formatted_release_date)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"pr_data.txt"
    folder_path = f"releases/{formatted_release_date}"
    file_path = f"{folder_path}/{file_name}"

    # Create the new folder if it doesn't exist
    subprocess.run(['mkdir', '-p', folder_path])

    # Gets the title, number, and body of merged PRs
    merged_pull_requests = get_merged_pull_requests()

    tag_name, tag_time = get_tag_info()
    print(f"Extracting from pull requests after release tag '{tag_name}'")

    # Writes the PR information to a txt file, including PR label and merge time
    with open(file_path, 'w', encoding="utf8") as file:
        file.write("Merged Pull Requests:\n")
        for pr in merged_pull_requests:
            file.write(f"Number: {pr['number']}\n")
            file.write(f"Title: {pr['title']}\n")
            merged_at = get_merged_at(pr['number'])
            file.write(f"Merged At: {merged_at}\n") 
            file.write("\n")
            labels = get_labels(pr['number'])
            if labels:
                file.write("Labels:\n")
                for label in labels:
                    file.write(f"- {label['name']}\n")
            file.write(f"Body: {pr['body']}\n")
            file.write("\n")

    print(f"Pull request data saved to '{file_path}'.")

    qmd_files = {
        "enhancement": "",
        "bug": "",
        "deprecation": "",
        "python": ""
    }

    os.makedirs(release_folder, exist_ok=True)

    generate_qmd_files(qmd_files, release_folder, formatted_release_date, merged_pull_requests, tag_time, release_date, tag_name)
    
    update_quarto_yaml(qmd_files, release_date)

    # Deletes the txt file once all PR data is extracted
    os.remove(file_path)
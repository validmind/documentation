import os
import re
import shutil
import subprocess
import json
from datetime import datetime

def get_tag_info():
    # Get the most recent tag name
    cmd_tag_name = ['gh', 'api', 'repos/validmind/documentation/tags', '--jq', '.[0].name']
    result_tag_name = subprocess.run(cmd_tag_name, capture_output=True, text=True)
    tag_name = result_tag_name.stdout.strip()

    # Get the commit SHA associated with the most recent tag
    cmd_commit_sha = ['gh', 'api', f'repos/validmind/documentation/git/matching-refs/tags/{tag_name}', '--jq', '.[].object.sha']
    result_commit_sha = subprocess.run(cmd_commit_sha, capture_output=True, text=True)
    tag_sha = result_commit_sha.stdout.strip()

    # Get the commit time from its SHA
    cmd_commit_time = ['gh', 'api', f'repos/validmind/documentation/git/commits/{tag_sha}', '--jq', '.committer.date']
    result_commit_time = subprocess.run(cmd_commit_time, capture_output=True, text=True)
    tag_time = result_commit_time.stdout.strip()[:10] # Truncate the date

    return tag_name, tag_time

def get_merged_pull_requests():
    cmd = ['gh', 'pr', 'list', '--state', 'merged', '--json', 'title,number,body', '--limit', '30']
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    pr_data = json.loads(output)
    return pr_data

def get_labels(pull_request_number):
    cmd = ['gh', 'pr', 'view', str(pull_request_number), '--json', 'labels']
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    labels_data = json.loads(output)
    labels = labels_data['labels']
    return labels

def get_merged_at(pull_request_number):
    cmd = ['gh', 'pr', 'view', str(pull_request_number), '--json', 'mergedAt']
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.strip()
    merge_time_data = json.loads(output)
    merge_time = merge_time_data['mergedAt'][:10] # Truncate so only the date is printed
    return merge_time

def extract_external_release_notes(pr_body):
    match = re.search(r"## External Release Notes(.+)", pr_body, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def update_release_highlights_template(template_filepath, pull_requests):
    with open(template_filepath, 'r') as file:
        template_content = file.read()

    release_notes = ""
    for pr in pull_requests:
        title = pr['title']
        external_notes = extract_external_release_notes(pr['body'])
        if external_notes:
            release_notes += f"- **{title}**\n\n{external_notes}\n\n"

    template_content = re.sub(r"(?<=## Release highlights\n\n).*?(?=\n##)", release_notes, template_content, flags=re.DOTALL)

    with open(template_filepath, 'w') as file:
        file.write(template_content)

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
                        external_release_notes = extract_external_release_notes(pr['body'])
                        if external_release_notes:
                            qmd_files[label_name] += f"- **{pr['title']}**\n\n   {external_release_notes}\n\n\n"
                    
                    if label_name == "highlight":
                        highlight_pull_requests.append(pr)

    for label, release_notes in qmd_files.items():
        if label != "highlight":
            if release_notes:
                qmd_filename = f"{label.replace(' ', '-').lower()}.qmd"
                qmd_filepath = os.path.join(release_folder, qmd_filename)
                with open(qmd_filepath, 'w') as file:
                    file.write("---\n")
                    file.write(f"title: \"{label.capitalize()}\"\n")
                    file.write("keywords: \"release notes, model risk management, ValidMind\"\n")
                    file.write("---\n\n")
                    file.write(f"## {label.capitalize()} -- {release_date}\n\n")
                    file.write(release_notes)

    # Copy and update release_highlights_template.qmd in the releases folder
    template_filename = "release_highlights_template.qmd"
    template_filepath = os.path.join(release_folder, f"release-notes-{formatted_date}.qmd")
    shutil.copyfile(template_filename, template_filepath)

    update_release_highlights_template(template_filepath, highlight_pull_requests)

def update_quarto_yaml(qmd_files, release_date):
    yaml_filename = "_quarto.yml"
    temp_yaml_filename = "_quarto_temp.yml"

    shutil.copyfile(yaml_filename, temp_yaml_filename)

    with open(temp_yaml_filename, 'r') as file:
        lines = file.readlines()

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

                if qmd_files["documentation"]:
                    file.write(f'                - text: "Documentation"\n')
                    file.write(f'                  file: releases/{formatted_release_date}/documentation.qmd\n')

                add_release_content = False

    os.remove(temp_yaml_filename)

if __name__ == '__main__':
    # Get the path of the cloned repository
    repo_path = os.path.join(os.getcwd())

    os.chdir(repo_path)  # Change the current working directory to the cloned repository path

    release_date = input("Enter the release date (<month> <day>, <year>): ")
    formatted_release_date = datetime.strptime(release_date, "%B %d, %Y").strftime("%Y-%b-%d").lower()

    release_folder = os.path.join("releases", formatted_release_date)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"pr_data.txt"
    folder_path = f"releases/{formatted_release_date}"
    file_path = f"{folder_path}/{file_name}"

    # Create the new folder if it doesn't exist
    subprocess.run(['mkdir', '-p', folder_path])

    # Get the merged pull requests
    merged_pull_requests = get_merged_pull_requests()

    tag_name, tag_time = get_tag_info()
    print(f"Extracting from pull requests after release tag '{tag_name}'")

    with open(file_path, 'w') as file:
        file.write("Merged Pull Requests:\n")
        for pr in merged_pull_requests:
            file.write(f"Number: {pr['number']}\n")
            file.write(f"Title: {pr['title']}\n")
            merged_at = get_merged_at(pr['number'])
            file.write(f"Merged At: {merged_at}\n")  # Write the merged_at data
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
        "documentation": ""
    }

    os.makedirs(release_folder, exist_ok=True)

    generate_qmd_files(qmd_files, release_folder, formatted_release_date, merged_pull_requests, tag_time, release_date, tag_name)
    
    update_quarto_yaml(qmd_files, release_date)

    os.remove(file_path)
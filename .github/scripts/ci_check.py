import os
import re
import json
import sys
from github import Github

def get_pull_request_number(pr_url):
    response = requests.get(pr_url)
    if response.status_code == 200:
        pr_number = int(re.search(r'pull/(\d+)', response.url).group(1))
        return pr_number
    else:
        raise ValueError("Failed to fetch pull request details.")

def ci_check(pr_number, access_token):
    g = Github(access_token)
    # Get repository, pull request, and labels
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    pr = repo.get_pull(pr_number)
    labels = [label.name for label in pr.labels]
    description = pr.body

    # Check for the presence of a label
    if not labels:
        print('Pull requests must include at least one label.')
        return False
        
    # Check for the presence of 'internal' label
    if 'internal' in labels:
         return True
        
    # Check for description of external change
    release_notes_pattern = r'## External Release Notes[\n\r]+(.*?)(?:\n##|\Z)'
    release_notes_match = re.search(release_notes_pattern, description, re.DOTALL)
    if release_notes_match:
        release_notes_text = release_notes_match.group(1).strip()
        if release_notes_text and release_notes_text != '<!--- REPLACE THIS COMMENT WITH YOUR DESCRIPTION --->':
            return True

    print('Pull requests must include a description in the release notes section.')
    return False

if __name__ == '__main__':
    event_path = os.environ['GITHUB_EVENT_PATH']
    with open(event_path, 'r') as f:
        event_payload = json.load(f)
        pr_number = event_payload['pull_request']['number']
    
    access_token = os.environ['GITHUB_TOKEN']

    result = ci_check(pr_number, access_token)

    if result:
        print('CI check passed.')
        exit(0)
    else:
        exit(1)
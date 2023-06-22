import os
import re
import json
import requests
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
        
    # Check for text under 'External Release Notes'
    release_notes_pattern = r'## External Release Notes(.*?)(?:(?=<!--- REPLACE THIS COMMENT WITH YOUR DESCRIPTION --->)|$)'
    release_notes_match = re.search(release_notes_pattern, description, re.DOTALL)
    if release_notes_match:
        release_notes_text = release_notes_match.group(1).strip()
        if release_notes_text and release_notes_text != '<!--- REPLACE THIS COMMENT WITH YOUR DESCRIPTION --->':
            return True

    print('Pull request must include description in Release Notes section.')
    return False

def create_check_run(repo, pr_number, conclusion, output):
    pr = repo.get_pull(pr_number)
    commit_sha = pr.head.sha

    check_run = repo.create_check_run(
        name='CI Check',
        head_sha=commit_sha,
        status='completed',
        conclusion=conclusion,
        output=output
    )

def main():
    event_path = os.environ['GITHUB_EVENT_PATH']
    with open(event_path, 'r') as f:
        event_payload = json.load(f)
        pr_number = event_payload['pull_request']['number']

    access_token = os.environ['GITHUB_TOKEN']

    result, error_message = ci_check(pr_number, access_token)

    if result:
        conclusion = 'success'
        output = {
            'title': 'CI Check Passed',
            'summary': 'The CI check passed.',
        }
    else:
        conclusion = 'failure'
        output = {
            'title': 'CI Check Failed',
            'summary': error_message,
        }

    g = Github(access_token)
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    create_check_run(repo, pr_number, conclusion, output)

    if result:
        print('CI check passed.')
        exit(0)
    else:
        print('CI check failed.')
        exit(1)

if __name__ == '__main__':
    main()

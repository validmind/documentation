from github import Github
import yaml
import os

def ci_check(pr_number, access_token):
    g = Github(access_token)

    # Get repository, pull request, and labels
    repo = g.get_repo(f'{github.repository_owner}/{github.repository}')
    pr = repo.get_pull(pr_number)
    labels = [label.name for label in pr.labels]
    description = pr.body

    # Check for the presence of a label
    if not labels:
        print('Pull request must include a label.')
        return False
        
    else:
        # Check for the presence of 'internal' label
        if 'internal' in labels:
            return True
        
        else:
            # Check for description of external change
            if '## External Release Notes' in description:
                return True
            
            else:
                print('Pull request must include description in Release Notes section.')
                return False

if __name__ == '__main__':
    github = {
        'repository_owner': os.environ['GITHUB_REPOSITORY_OWNER'],
        'repository': os.environ['GITHUB_REPOSITORY']
    }
    pr_number = os.environ['GITHUB_EVENT_PULL_REQUEST_NUMBER']
    access_token = config['access_token']

    result = ci_check(pr_number, access_token)
    if result:
        print('CI check passed.')
        exit(0)
    else:
        exit(1)

import os

def check_pull_request_description():
    file_path = os.environ['GITHUB_EVENT_PATH']
    with open(file_path, 'r') as file:
        content = file.read()
        if '## External Release Notes' not in content:
            print('ERROR: External Release Notes section is missing')
            exit(1)

def has_internal_label():
    labels_url = os.environ['PULL_REQUEST_URL'] + '/labels'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}'
    }
    response = requests.get(labels_url, headers=headers)
    labels = response.json()
    for label in labels:
        if label['name'] == 'internal':
            return True
    return False

def ci_check():
    if has_internal_label():
        return
    else:
        check_pull_request_description()

ci_check()

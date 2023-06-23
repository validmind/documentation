import os
import sys
import json

# Get the event payload from the environment variable
event_path = os.environ['GITHUB_EVENT_PATH']
with open(event_path, 'r') as f:
    event_payload = json.load(f)

# Check if the description or labels have changed
if sys.argv[1] == 'description':
    description_changed = event_payload['changes'].get('body') is not None
    print(description_changed)
elif sys.argv[1] == 'labels':
    labels_changed = event_payload['changes'].get('labels') is not None
    print(labels_changed)

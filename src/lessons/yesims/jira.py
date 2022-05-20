# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://your-domain.atlassian.com/rest/agile/1.0/board"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(
    json.dumps(
        json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
    )
)

"""
jupyter run

https://developer.atlassian.com/cloud/jira/software/rest/api-group-other-operations/#api-rest-agile-1-0-board-get

need to see board name, issue key
by 4/3

need the changelog for issues
"""

akmiles @ icloud.com

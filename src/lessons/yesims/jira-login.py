JIRA_USERNAME = "akmiles@ctpsws.com"
JIRA_TOKEN = "iX0eRSyejld3fKKC7cUQ9065"
JIRA_URL = "https://ctpsws.atlassian.net/"

import subprocess
import json

cmd = (
    f"curl -s -u {JIRA_USERNAME}:{JIRA_TOKEN} -X GET -H "
    f'"Content-Type: application/json" '
    f"{JIRA_URL}rest/agile/1.0/board/1"
)

status, output = subprocess.getstatusoutput(cmd)
board = json.loads(output)

print(board["name"])

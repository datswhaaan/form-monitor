import requests
import os
import sys
import urllib.parse

GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")
webhook = os.getenv("DISCORD_WEBHOOK")

workflow_file = "monitor.yml"
repo = os.getenv("GITHUB_REPOSITORY")
token = os.getenv("GITHUB_TOKEN")

response = requests.get(GOOGLE_FORM_URL, timeout=15)

text = response.text.lower()

closed = "no longer accepting responses" in text or "/closedform" in response.url

if closed:
  print("Form is still closed.")
  sys.exit(0)

print("FORM IS OPEN!")

requests.post(
  webhook,
  json={"content": f"Google Form is OPEN!\n{GOOGLE_FORM_URL}"},
  timeout=15,
)

requests.put(
    f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_file}/disable",
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    },
    timeout=15,
)

print("Workflow disabled.")

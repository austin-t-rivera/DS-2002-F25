#!/usr/bin/env python3

import json
import requests
import os

token = os.getenv('GITHUB_TOKEN')

url = "https://api.github.com/user/repos"
data = {"name": "another-new-repo"}

headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}
r = requests.post(url, headers=headers, data=json.dumps(data))

# # Put the response into json to parse
d = r.json()
# # Grab the html_url value:
link = d['html_url']
print.f("Your new repo has been created: {link}")

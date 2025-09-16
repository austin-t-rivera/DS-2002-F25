#!/usr/bin/env python3

import json
import requests
import os

token = os.getenv('GITHUB_TOKEN')

url = "https://api.github.com/repos/nmagee/my-new-repo"
data = {"name": "my-new-repo"}

headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}
r = requests.delete(url, headers=headers)
print(r.text)
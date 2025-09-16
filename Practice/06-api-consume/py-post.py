#!/usr/bin/env python3

import json
import requests
import os

## Setup
##
## 1. Go to https://github.com/settings/tokens and generate a new token.
##    Grant it ALL permissions to the "repo" and "gist" sections.
##    Do NOT ever commit this token to code you push back to Github.
##    Do NOT ever share this token with another person.
##
## 2. Copy the token and in your bash shell save it as an env variable (no spaces):
##    GITHUB_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
##

## Now we'll use the Github token to authenticate you to and create a
## simple gist.

token = os.getenv('GITHUB_TOKEN')

url = "https://api.github.com/gists"
data = {
    "public": True,
    "files": {
        "ds3002.py": {
            "content": "#!/bin/bash \n\nFOO='bar';\n\necho $FOO;"
        },
    }
}
headers = {'Authorization': f'token {token}'}
r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())

## Visit this URL and you can see your new gist:
print("Your new gist has been created: ")

# Put the response into json to parse
d = r.json()
# Grab the html_url value:
link = d['html_url']
print(link)

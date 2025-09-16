#!/usr/bin/env python3

import json
import requests

# Set up your data payload. This is what is POSTed to the #bot channel. The content
# may consist of plain text, markdown text, URLs, image links, etc. Feel free to test.
# All parameters available to you in this method "Execute Webhook" can be found here: 
# https://discord.com/developers/docs/resources/webhook#execute-webhook 

data = { 
    "content": "This **bot** means business!! https://i.imgur.com/AaWEBMY.jpg",
    "username": "REPLACE_WITH_YOUR_ID",
    "avatar_url": "REPLACE_WITH_CREATIVE_URL"
}

# The URL below should be treated like a password and NOT published in code. Consider
# passing it into your app as an ENV variable.
url = "https://discord.com/api/webhooks/xxxxx/yyyyy"

response = requests.post(url, json = data)
print(response)

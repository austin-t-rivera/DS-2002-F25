# Data Project 1

**Due: April 12, 2021**

Projects

1. API Chatbot
2. ETL Data Processor
3. Discord Integration


## API Chatbot

You may write this as an API with 5 endpoints OR with a single endpoint that accepts 5 different parameters. Either works. Design logic for each of those request methods to return something dynamic. Once running, your "chatbot" can be accessed using a browser, or Postman, or the command-line. Be sure to deliver all the required benchmarks.

For example: User submits their zip code and the API performs a search using that parameter to get/return something useful and informative to the user.

For external API integrations (to grab data from other APIs for your API), here are some suggestions:

- https://docs.github.com/en/rest
- https://developer.twitter.com/en/docs/twitter-api
- HUGE LIST: https://github.com/public-apis/public-apis

For your deliverable (i.e. the thing you are to turn in), I am looking for one of two options:
1. A container running Flask/FastAPI with your code, launched into AWS LightSail; or
2. Python in a Chalice app that has been published to AWS (this is for more advanced students)

Instructions for publishing a container to Lightsail:

[![](http://img.youtube.com/vi/0vn93BtjtyU/0.jpg)](http://www.youtube.com/watch?v=0vn93BtjtyU "How To - Deploy a Container to Lightsail")

You may borrow/adapt code distributed in class earlier this semester!

In addition to the container image and/or API, you should turn in the URL to a Github repository for your project.


## ETL Data Processor

You should write this as a container that can be run and tested locally. Your application should be prepared to fetch and process data based on a parameter fed into it at runtime. This can be by URL, or ID, or filename, etc. (Your choice.) The file may also be local to the container or remote via URL. (Again, your choice.) If you want to stage data in an S3 bucket for testing and grading, that's fine! Be sure to deliver all the required benchmarks.

For example: You find a series of open-source data files published to the web, and your container requires a URL for each file fed into it. From there your app fetches the file, processes and transforms it, and then returns an output file along with summary data, etc. Your application can return the file locally to the user or push it to S3, etc. afterward. The user should be given the location of the output file.

For external data sources, here are some suggestions:

- https://www.kaggle.com/datasets
- https://data.world/
- https://www.data.gov/
- https://opendata.charlottesville.org/

For your deliverable (i.e. the thing you are to turn in), I am looking for a container image and a set of instructions for how to use your tool. You should consider everything the user needs to know in order to run your container.

You may borrow/adapt code distributed in class earlier this semester!

In addition to the container image, you should turn in the URL to a Github repository for your project.


## Discord Integration

This project can be submitted as a portable container image OR as a published API. Your application should be prepared to fetch and process data based on a parameter fed into it at runtime. This parameter could theoretically be ANYTHING -- a word, a name, a zip code, the URL to an image, a map location, a year, etc. (Be creative please!) Using this value, your application should DO SOMETHING INTERESTING with remote data that relates to that value. Be sure to deliver all the required benchmarks.

For example: Users pass a birthdate into your application, which in turn finds out an interesting fact about that day in history. Perhaps it also grabs a relevant image to go along with that fact, and returns both to the #bot channel in our Discord server.

An advanced example: Users pass the URL of an image to your application, which performs some recognition and analysis on the image and returns that to Discord. (Hint: there's an [AWS service](https://console.aws.amazon.com/rekognition/) for that.)

BE CREATIVE!

**Discord Integration** - see the `discord.py` file in this folder for programmatic help with your POST method to the Discord API. The webhook URL I am giving you publishes directly to the #bot channel of our server but is also considered sensitive and should NOT be distributed with the code of your application. So you will need a method for injecting some/all of that URL into your application at runtime, using an ENV variable, etc.

```
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
```
Output to the Discord channel looks like this:
![Discord channel POST](https://nmagee.github.io/ds3002/images/bot-sample-post.png)

A walkthrough of this integration is available here:

[![](http://img.youtube.com/vi/_qkZUFYkg2E/0.jpg)](http://www.youtube.com/watch?v=_qkZUFYkg2E "How To - Work with Discord Webhooks")

For your deliverable (i.e. the thing you are to turn in), I am looking for a container image (or, for more advanced students you may publish this as an API using either FastAPI or Chalice, etc.) and a set of instructions for how to use your tool. You should consider everything the user needs to know in order to run your container.

You may borrow/adapt code distributed in class earlier this semester!

In addition to the container image (or API), you should turn in the URL to a Github repository for your project.

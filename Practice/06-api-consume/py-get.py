#!/usr/bin/env python3

import requests


#  Fetching remote HTTP resources in Python requires a library.
#  One of the most common is the `requests` library.

#  Set up the base URL for the request:
url = 'https://api.github.com/repos/nmagee/ds3002/branches'

#  Declare a variable that will contain the requests.get response:
response = requests.get(url)


#  We now have a lot of data back from the remote API:
# print(response.headers)       #   <-- the headers of the response
# print(response.status_code)   #   <-- the HTTP code of the response
# print(response.json())        #   <-- the json body of the response
# print(response.encoding)      #   <-- the text encoding of the response
# print(response.text)          #   <-- plain text of the response body


# Load the response into json
data = response.json()

# Finally, iterate over the records and print out the 'name' field:
for r in data:
  print(r['name'])

#!/bin/bash

# In order to get/fetch a remote HTTP resource, use the `curl` or `httpie`:
# Sample URL:
# https://api.github.com/repos/nmagee/ds3002/branches

# Using curl:
/usr/bin/curl -X GET https://api.github.com/repos/nmagee/ds2002/branches

# Using httpie:
http --body https://api.github.com/repos/nmagee/ds2002/branches

# ---------------------------------------------------------------------------------------
# Now you're receiving JSON! Use jq to parse/filter it:

# Filter for just the names of the branches:
http --body https://api.github.com/repos/nmagee/ds2002/branches | jq -r .[].name

# Filter for just the sha hashes of the latest commits:
http --body https://api.github.com/repos/nmagee/ds2002/branches | jq -r .[].commit.sha

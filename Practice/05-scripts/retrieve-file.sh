#!/bin/bash

curl -o http.log https://s3.amazonaws.com/ds3002-resources/logs/http.log

# cat http.log | grep -v "128.143.0.10" | wc -l

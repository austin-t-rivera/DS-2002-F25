#!/bin/bash

set -e

# 1. retrieve file
# 2. decompress
# 3. output the length - in lines
# 4. convert to csv
# 5. zip it up
# 6. send it off to s3
# 7. send an AWS sns message

file='remote-data'

echo "Attempting fetch..."
/usr/bin/curl -o $file.tar.gz https://s3.amazonaws.com/ds3002-cli/remote/$file.tar.gz || exit 1;

sleep 5
echo "Decompressing..."
/usr/bin/tar -xzvf $file.tar.gz || exit 1;

sleep 5
echo "Calculating length..."
/usr/bin/wc -l $file.tsv || exit 1;

sleep 5
echo "Converting to CSV..."
/usr/bin/tr '\t' ',' < $file.tsv > $file.csv || exit 1;

sleep 5
echo "Compressing to zip..."
/usr/bin/zip $file.zip $file.csv || exit 1;

sleep 5
echo "Shipping to S3..."
/usr/local/bin/aws s3 cp --acl public-read $file.zip s3://ds3002-resources/zips/ || exit 1;

sleep 5
echo "Send SNS message..."
/usr/local/bin/aws sns publish --topic-arn arn:aws:sns:us-east-1:440848399208:script-notification --message "$remote-data converted and published" || exit 1;
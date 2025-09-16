#!/usr/bin/env python3

import boto3

# Flips the state of your RDS instance: Start/Stop
instance = "ds3002-rds"

# Create rds client to api
rds = boto3.client("rds")

# Get current state
response = rds.describe_db_instances(
    DBInstanceIdentifier=instance
)
state = response['DBInstances'][0]['DBInstanceStatus']
status = f"Instance {instance} is: {state}"
print(status)

#!/usr/bin/env python3

import boto3

# Flips the state of your RDS instance: Start/Stop
instance = "ds3002-rds"

rds = boto3.client("rds")

# Get current state
response = rds.describe_db_instances(
    DBInstanceIdentifier=instance
)
state = response['DBInstances'][0]['DBInstanceStatus']

# Parse current state and flip it
if (state == 'available'):
  print("Stopping instance", instance)
  response = rds.stop_db_instance(
    DBInstanceIdentifier=instance
  )
elif (state == 'stopped'):
  print("Starting instance", instance)
  response = rds.start_db_instance(
    DBInstanceIdentifier=instance
  )

print("Wait approximately 10 minutes for state to change.")

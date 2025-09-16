#!/usr/bin/env python3

import os
import MySQLdb

HOST = 'ds3002-rds.cqee4iwdcaph.us-east-1.rds.amazonaws.com'
USER = 'ds3002'
PASS = os.environ.get('RDS_PASS')

# In ~/.bashrc
# export RDS_PASS='xxxxyyyyzzzz'

db=MySQLdb.connect(host=HOST,user=USER,passwd=PASS,db="ds3002")

c=db.cursor()
c.execute("""SELECT id,email,ip_address FROM MOCK_DATA LIMIT 5""")
results = c.fetchall()
print(results)

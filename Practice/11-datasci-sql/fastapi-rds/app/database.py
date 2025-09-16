import os
import MySQLdb

DB_NAME = 'ds3002'
HOST = 'ds3002-rds.cqee4iwdcaph.us-east-1.rds.amazonaws.com'
USER = 'ds3002'
PASS = os.environ.get('RDS_PASS')

db = MySQLdb.connect(
    host=HOST,
    user=USER,
    passwd=PASS,
    db="ds3002"
)
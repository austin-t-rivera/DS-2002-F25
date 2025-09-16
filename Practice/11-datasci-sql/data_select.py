#!/usr/bin/env python3

import json
import os
import MySQLdb

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "nem2p"

db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
cursor = db.cursor(MySQLdb.cursors.DictCursor)

# Insert statement as a list w/ string replacement
add_record = ("INSERT INTO mock_data (id, first_name, last_name, email, gender, ip_address) VALUES (%s, %s, %s, %s, %s, %s)")

# Data as a list
record_data = (1001, "Mickey", "Mouse", "mickey@disney.com", "Non-binary", "1.2.3.4")

# Set up the cursor execution
cursor.execute(add_record, record_data)

# Perform the actual commit
db.commit()

# Close the db connections
cursor.close()
db.close()
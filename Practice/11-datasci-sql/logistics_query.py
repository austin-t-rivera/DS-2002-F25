#!/usr/bin/env python3

import json
import os
import MySQLdb
import MySQLdb._exceptions
import decimal
from decimal import Decimal
import datetime

def Decoder(o):
    if isinstance(o, datetime.datetime):
        return str(o)
    if isinstance(o, decimal.Decimal):
        return o.__str__()

year = '2020'
month = '08'

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "nem2p"

db=MySQLdb.connect(host=DBHOST,user=DBUSER,passwd=DBPASS,db=DB)

def get_logistics(year: int, month: int):
    query = f"SELECT * FROM logistics WHERE created_on LIKE '{year}-{month}-%' ORDER BY created_on;"
    c=db.cursor()
    try:
        c.execute(query)
        headers=[x[0] for x in c.description]
        results = c.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
        output = json.dumps(json_data, default = Decoder)
        print(output)
        return(output)
    except MySQLdb.Error as e:
        print("MySQL Error: ", str(e))
        return None
    finally:
        c.close()
        db.close()







    c.close()
    db.close()
    return output


# Run the script
if __name__ == '__main__':
    get_logistics(year,month)

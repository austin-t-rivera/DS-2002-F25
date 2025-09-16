# Hands-On SQL for Data Science

Reference files / commands:

- [`data.sql`](./data.sql) | [`data_select.py`](./data_select.py)
- [`logistics.sql`](./logistsics.sql) | [`logistics_query.py`](./logistics_query.py)
- [Command Reference](./sql-examples.md)
- [Additional SQL Examples](./more.md)

## Setup your repo
1. Go to your fork of the `ds2002-course` repository in GitHub.
2. Use the "Sync Fork" button at the top of the page to sync and update your branch with the upstream repo.
3. Now open your repository in Gitpod. Remember to simply append `gitpod.io/#` before the GitHub URL and it will open automatically.

## Set up Gitpod

1. Install the `mysql` client from the Gitpod terminal and for supporting the `MySQLdb` package:

    ```
    sudo apt install -y mysql-client
    pip install mysqlclient
    ```

2. Run the `mysql` command-line client:

    ```
    mysql -h $DBHOST -u$DBUSER -p$DBPASS
    ```

3. Select your database. Using the DB you have already created under your computing ID, select it with the `use` command:

    ```
    use mst3k;   # replace with your DB name
    ```

## Load Data from SQL Files

1. Open the `data.sql` script and read the SQL commands it contains.
2. To insert SQL data fromo a `.sql` script via the command-line:

    ```
    mysql -h $DBHOST -u$DBUSER -p$DBPASS db-name < script.sql
    ```

    Be sure to update the commands above specifying your own `db-name` and pointing to the correct `.sql` file.

## Practice with SQL queries in the CLI

```
SELECT
UPDATE
DELETE
```

See [this page](./sql-examples.md) for examples.

## Practice with SQL queries using Python

### imports

```
import json
import os
import MySQLdb
```

### `env` variables

```
# db config stuff
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "nem2p"
```

### Connection Strings

```
db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
```

### Cursor

Create the cursor. Create one with and without a `DictCursor`.

```
cursor = db.cursor()
cursor = db.cursor(MySQLdb.cursors.DictCursor)
```

### Query

```
cursor.execute("SELECT * FROM mock_data ORDER BY last_name LIMIT 20")
results = cursor.fetchall()
```

### Complete SELECT Example
```
import json
import os
import MySQLdb

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "nem2p"

db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, db=DB)
cursor = db.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("SELECT * FROM mock_data ORDER BY last_name LIMIT 20")
results = cursor.fetchall()
db.close()
print(results)
```

## Insert Data

Assume you have data ready to insert as a simple Python list

```
record_data = (1001, "Mickey", "Mouse", "mickey@disney.com", "Non-binary", "1.2.3.4")
```

To insert Pythonic lists into a SQL database, set up a template for the insert statement using string replacement formatting:

```
add_record = ("INSERT INTO mock_data "
               "(id, first_name, last_name, email, gender, ip_address) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
```

Then set up the query statement by combining your two lists:
```
cursor.execute(add_record, record_data)
```

Finally, perform the commit:
```
db.commit()
```

### Complete INSERT Example
```
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
```
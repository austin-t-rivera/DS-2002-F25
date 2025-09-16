# SQL Syntax and Examples

## Basics

1. SQL syntax is rarely case-sensitive. Typically, users will write SQL
using upper-case for visual clarity and readability.
2. End all SQL commands with a semi-colon! You must do this or the SQL
engine will not know that you've issued a complete command.
3. Extra whitespace in SQL commands generally does not matter. This means
you can have line breaks for extra readability.
4. Comments can be added to your SQL using the pound/hashtag `#`. Annotate your code!
4. Think of your SQL as code, and store/version/track it using a version
control system like `git`. This helps you build libraries of reusable blocks of code.
5. Many commands can be used on multiple records at the same time. For example,
an `UPDATE` query might apply to hundreds or thousands of rows at the same time.
Same with `DELETE` or `SELECT`.

## Basic Commands (CRUD)

- `SELECT` - Reads a row(s) from a table or view.
- `INSERT` - Creates a new record in a table.
- `UPDATE` - Edits a record(s).
- `DELETE` - Deletes a record(s).

### SELECT

```sql
SELECT * FROM table_name;
```
Important elements:

- After the SELECT command, the `*` asterisk, or wildcard, means you are requesting ALL columns
from this table.
- You may instead request specific columns.

```sql
SELECT firstname,lastname,dob FROM customers;
```

### INSERT

Insert adds a record to your table. Depending upon which columns are required (i.e. where a `NULL` value is disallowed) you may submit only some columns. Integers and floats usually do not have to be quote-wrapped.
The order of columns in your `INSERT` statement do not have to match the table column order, but do have
to be paired, in order, with the values you submit.

```sql
INSERT INTO tracking 
  (id, telem_1, telem_2, longitude, latitude, created_on) 
  VALUES 
  ('7c9d79c7-092b-4c21-b41a-89e2f845101f', 0.773, 0.01, 105.888827, 28.753497, '2020-04-14T09:28:19Z');
```

### UPDATE

Update is used to modify one or more columns in a table, for one or more records. Some examples

```sql
# Update two columns of a single record
UPDATE customers 
  SET middle_name = 'Edward', dob = '2001-04-01 00:00:00'
  WHERE customer_kd = '12345';

# Update all records that apply
UPDATE purchases
  SET status = 'closed'
  WHERE purchase_date IS NULL OR purchase_date = '';
```

### DELETE

Delete is used to remove records from a table, and should always be scoped (applied) to rows that you specify
with a `WHERE` clause. (Unless you are deleting all records in a table.)

Some examples

```sql
# Delete a single customer
DELETE FROM customers WHERE customer_key = '12345';

# Delete customer records that are missing a value
DELETE FROM customers WHERE dob IS NULL OR dob = '';

# Delete old customers who have not visited your app recently
DELETE FROM customers WHERE last_visit < '2015-12-31 00:00:00';

# Delete records that meet more complex conditions
DELETE FROM customers 
  WHERE 
    mfa_auth = 0 AND
    last_visit < '2015-12-31 00:00:00' AND
    password_age > 90;
```
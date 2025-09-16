# Working with file formats

## json

Some iterations to try using the `jq` tool in the command-line:

Filter the `mock_data.json` file containing "flat", non-nested data.
```
cd /root/course/01-data/
cat mock_data.json
cat mock_data.json | jq -r .[]
cat mock_data.json | jq -r .[] | jq ."dob"
cat mock_data.json | jq -r .[] | jq ."dob" | grep "1998"
cat mock_data.json | jq -r .[] | jq ."dob" | grep "1998" | wc -l
```

Filter the `mock_data_nested.json` file containing nested data.
```
cd /root/course/01-data/
cat mock_data_nested.json
cat mock_data_nested.json | jq ."healthChecks"
cat mock_data_nested.json | jq ."healthChecks" | jq .[]."delaySeconds"
cat mock_data_nested.json | jq ."healthChecks" | jq -r .[]."delaySeconds"
```

```
cd /root/course/01-data/
cat mock_data_nested.json | jq ."container"
cat mock_data_nested.json | jq ."container" | jq ."volumes"
cat mock_data_nested.json | jq ."container" | jq ."volumes" | jq -r .[]."hostPath"
```

Notice the `-r` flag to toggle "raw" output versus quote-wrapped output.

Try https://jqplay.org for more lessons, inputs, filters, etc.

## csv

```
cat mock_data.csv
```

Note that the 6 columns are separated by 5 commas. Fields that must contain a comma should be quote-enclosed.

## tsv

Like CSV files separated by commas, tab-separated files are delimited by tabs. This can fool the naked eye, and throw off import
processes when stray tabs are inserted into the data fields.

To convert TSV to CSV, or vice versa, use a text search+replace function such as `awk`, `tr`, or a good IDE/text editor:

Use `tr`
```
tr '\t' ',' < file.tsv > file.csv
```

Use `sed`
```
sed 's/'$'\t''/,/g' file.tsv > file.csv
```

Use `awk`
```
awk 'BEGIN { FS="\t"; OFS="," } {$1=$1; print}' file.tsv > file.csv
```

## xml

Structured data. Note that every record, and every data field within each record, is fully wrapped in markup that is opened and closed:

```xml
<dataset>
  . . .
  <record>
    <id>97</id>
    <first_name>Tamarra</first_name>
    <last_name>Jeannaud</last_name>
    <email>tjeannaud2o@fema.gov</email>
    <ip_address>26.106.176.174</ip_address>
    <dob>11/19/1981</dob>
  </record>
  <record>
    <id>98</id>
    <first_name>Korney</first_name>
    <last_name>Hazlegrove</last_name>
    <email>khazlegrove2p@wsj.com</email>
    <ip_address>218.117.101.96</ip_address>
    <dob>01/06/1981</dob>
  </record>
  . . .
</dataset>
```

## sql

`cat` and `head` and `tail` the SQL snippet. Notice that each line consists of an isolated query.
The SQL file is therefore not a bulk insert statement (not properly) but a concatenated series of independent
SQL statements. This is a best practice so that any single line that triggers a failure can be more
easily identified and the previous inserts will have succeeded.

```
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (1, 'Berkley', 'Annon', 'bannon0@accuweather.com', '193.95.255.138', '10/20/1991');
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (2, 'Doro', 'Morse', 'dmorse1@moonfruit.com', '170.67.183.172', '12/01/1995');
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (3, 'Charmain', 'Halden', 'chalden2@europa.eu', '170.112.37.136', '03/03/1982');
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (4, 'Allissa', 'Wakefield', 'awakefield3@usgs.gov', '23.46.25.161', '10/05/1988');
```

## Using Python to Parse JSON

Try the notebook based [Kaggle Lab](https://www.kaggle.com/nealmagee/parsing-json).

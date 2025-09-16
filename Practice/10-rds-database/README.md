# Working with RDS Databases

## Assignment

- [ ] Create an RDS of your own following instructions from the lecture.
- [ ] Connect to your RDS instnce using either the `mysql` command-line (in the course container), or [MySQL WorkBench](https://dev.mysql.com/downloads/workbench/), [PHPMyAdmin](https://phpmyadmin.uvadcos.io/), or other tools.
- [ ] Create a database in your RDS instance.
- [ ] Manually create a table within that database using a schema that matches the `MOCK_DATA` table from the lecture. Be sure to set a primary key.
- [ ] Import [`mock_data.sql`](mock_data.sql) into your table.

## `mysql` CLI Reference

To connect to a host using the `mysql` command-line in the course container:

```
mysql -h hostname-goes-here -uUSERNAME -p
```

You will be prompted to enter your password once you press return.

## Connection Issues

If you cannot connect to your RDS instance, check to make sure your local IP address is allowed to make
a connection over port 3306 in your [RDS security group](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#SecurityGroups:). Use [ifconfig.me](http://ifconfig.me/) to get your IP.

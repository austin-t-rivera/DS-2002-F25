# NoSQL Databases

We will touch three NoSQL database systems in this section of the course:

1. [**Redis**](#redis) - an in-memory Key-Value database.
2. [**MongoDB**](#mongodb) - a popular document database.
3. [**DynamoDB**](#dynamodb) - Amazon's cloud-based NoSQL service that offers both key-value and document features.

## Redis

Think of Redis as an exceptionally fast, 2-column lookup table. It makes no use of schemas, relations, or indexes.

- The LEFT `key` column (metaphorically speaking) in a Redis DB stores keys. Keys can consist of any useful, unique, identifier.
- The RIGHT `value` column in a Redis DB can consist of a variety of data types, such as strings, integers, lists, sets, hash tables, etc.

![Redis Data Types](https://keestalkstech.com/wp-content/uploads/2019/04/redis-data-structure-types1.jpeg)

Redis is "fast" despite its data storage capabilities being relatively large (the `value` half has a maximum capacity of 512MB),
while the database engine attempts to keep frequently-access data in memory for optimal return to requests.

Redis's strongest features for data science are:

1. Incredibly simple to use.
2. Stores large records.
3. Returns results quickly.
4. Useful for storing and retrieving lists, queues, tasks, items, orchestration, settings, etc.

[**Learn more about Redis**](https://redis.io/)

### Run Redis & Connect

For practice you will run Redis in a container next to your course container, without storage, clustering, or any custom settings.

```
docker run -d -p 6379:6379 redis
```
The Docker command above will run Redis in detached mode, exposed on port `6379` of your local computer. From there, you can connect
to the Redis service from your course container using the `-h` flag to specify a host:

```
redis-cli -h 172.17.0.1
```

#### For Gitpod Users

In Gitpod you can run the redis server directly within your container using a second terminal window. Follow these steps:
1. Open your forked version of the `course` repository using Gitpod. [Instructions here](https://github.com/nmagee/course#gitpod).
2. Go to the TERMINAL menu --> "New Terminal" to open a secondary terminal pane.
3. In that terminal, start a Redis server:
```
redis-server
```
4. A prompt that "A service is available on port 6379" will appear. Ignore or close it.
5. Return to your original terminal pane and you can now interact with Redis using the `redis-cli`.

### Practice

After watching the lecture video, try the following:

1. List all keys:
```
KEYS *
```
2. Insert some keys using the firstnames and lastnames of people as keys and values:
```
SET jim ryan
SET tina fey
SET leonardo davcinci
```
3. Fetch those values using their keys:
```
GET jim
GET leonardo
GET tina
```
4. Set 3 Key-Value pairs using integers as the value. Add expiration times in seconds:
```
SET counter1 10 EX 10 
SET counter2 472 EX 30 
SET counter3 984 EX 28 
```
Next retrieve these values by key, one by one. Repeat this process for the next minute. Can you continue to fetch these values?

5. Set up a counter and increment it. You can increment by any integer amount:
```
SET counter 1
INCR counter 5
INCR counter 5
INCR counter 5
GET counter
```
6. For more hands-on practice and advanced usage, try the [**try.redis.io Interactive Tutorial**](https://try.redis.io/). Pay particular
attention to commands like:

- `MSET` / `MGET` - setting multiple items
- `LPUSH` / `LSET` / `LRANGE` / `LREM` / `LPOP` - create and manage lists
- `ZADD` / `ZRANGE` / `ZREM` / `ZCOUNT` - create and manage sorted sets

## MongoDB

MongoDB helped popularize the NoSQL approach and remains a favorite choice among many developers because of its speed and
relative simplicity to work with. Like Redis, MongoDB tables (i.e. "collections") consist of keys and values, but the value
side is made up of variable payloads of JSON. This means that one row (i.e. "record" or "document") may contain JSON with
a handful of values while the next row contains dozens more. There is no requirement for records to conform to a pre-defined
schema or structure.

![MongoDB Documents](https://media.geeksforgeeks.org/wp-content/uploads/20200726190757/subtractdatabase-648x660.jpg)

Mongo allows developers to search across documents for specific data elements in the JSON tree, to add arbitrary documents within
the same collection, but a relatively small amount of data per document (16MB). This allows Mongo to keep frequently-accessed documents
in memory.

MongoDB's strongest features for data science are:

1. Simple to use for storing varied datasets.
2. Popularity in the community.
3. Can be run locally, on a server, or in the cloud.
4. Returns results quickly.

[**Learn more about MongoDB**](https://www.mongodb.com/)

### Run MongoDB & Connect

**Setup**

This course will be using MongoDB Atlas, a cloud-based Mongo service, for hands-on exercises. Follow the instructions in the [**How To video**](https://www.youtube.com/watch?v=5-tIfDCb-T4) for setup. I recommend
using a Google account when creating your [**Atlas MongoDB Cluster**](https://www.mongodb.com/cloud/atlas/register).

[![Create MongoDB Atlas Account](https://nmagee.github.io/ds3002/images/google-signup.png)](https://account.mongodb.com/account/sso/google?signupSource=&referer=null)

**Connect**

The DS3002 course container contains the `mongo` shell application. From MongoDB Atlas, click on the CONNECT button of your cluster
and select "Connect with the Mongo shell." This will give you a connection string:

```
mongo "mongodb+srv://cluster0.pguxs.mongodb.net/myFirstDatabase" --username <username>
```

Customize the command slightly:

- Remove `myFirstDatabase` from the connection string.
- Replace `<username>` with the user you created.

You will be prompted for your password and should then gain a prompt:

```
root@a18a980325ad:/workspaces/course# mongo "mongodb+srv://cluster0.pguxs.mongodb.net" --username mongo
MongoDB shell version v4.4.4
Enter password: 
connecting to: mongodb://cluster0-shard-00-00.pguxs.mongodb.net:27017,cluster0-shard-00-01.pguxs.mongodb.net:27017,cluster0-shard-00-02.pguxs.mongodb.net:27017/?authSource=admin&compressors=disabled&gssapiServiceName=mongodb&replicaSet=atlas-f0pmyi-shard-0&ssl=true
Implicit session: session { "id" : UUID("bb19fed7-39b9-4089-b292-fbbcc5f0efcf") }
MongoDB server version: 4.4.4
MongoDB Enterprise atlas-f0pmyi-shard-0:PRIMARY> 
```

### Practice

Follow either Exercise 1 or 2 in [**MongoDB Hands-On Exercises**](mongodb.md)

## DynamoDB

Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multi-region, multi-active, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. DynamoDB can handle more than 10 trillion requests per day and can support peaks of more than 20 million requests per second.

DynamoDB's strongest features for data science are:

1. It "just works."
2. As a managed service there is nothing to provision or maintain.
3. Regardless of user requests it remains fast.
4. Scales to any load.

The maximum value of the `value` half of a row in DynamoDB is 400KB, which is considerably smaller than Redis or MongoDB.

[**Learn more about DynamoDB**](https://aws.amazon.com/dynamodb/)

[![Intro to AWS DynamoDB](http://img.youtube.com/vi/sI-zciHAh-4/0.jpg)](http://www.youtube.com/watch?v=sI-zciHAh-4 "AWS DynamoDB")

### Hands-On Exercises

Follow the [**Qwiklab: Introduction to Amazon DynamoDB**](https://www.qwiklabs.com/focuses/14815?catalog_rank=%7B%22rank%22%3A3%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=9596628) lab for hands-on exercises.

## Managed NoSQL Services in the Cloud

Versions/variations of these NoSQL solutions are available in each of the three major public clouds:

| Cloud Vendor | Redis K-V | MongoDB Document | Global-Distributed |
| --- | --- | -- | -- |
| AWS | ElastiCache | DocumentDB, Atlas | DynamoDB |
| Google | MemoryStore | Atlas | BigTable |
| Azure | Azure Cache | Atlas | Cosmos |

## Read More

* [Ledger Databases](https://ivan.mw/2019-11-24/what-is-a-ledger-database)
* [Graph Databases](https://neo4j.com/developer/graph-database/)
* [Time Series Databases](https://aws.amazon.com/timestream/)

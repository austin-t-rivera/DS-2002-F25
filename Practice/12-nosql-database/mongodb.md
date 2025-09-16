# Lab 9: MongoDB

- [Lab 9: MongoDB](#lab-9-mongodb)
  - [Run MongoDB \& Connect](#run-mongodb--connect)
  - [Exercise 1](#exercise-1)
  - [Exercise 2](#exercise-2)
  - [Reference: CRUD Operations](#reference-crud-operations)
  - [Integrating with `python3`](#integrating-with-python3)

## Run MongoDB & Connect

**Setup**

This course will be using MongoDB Atlas, a cloud-based Mongo service, for hands-on exercises. Follow the instructions in the [**How To video**](https://www.youtube.com/watch?v=9DbZ2ii01ew) for setup. I recommend
using a Google account when creating your [**Atlas MongoDB Cluster**](https://www.mongodb.com/cloud/atlas/register).

**Connect**

Install the `mongosh` client for your laptop. Or use a Gitpod environment and run the installer:
```
sudo apt update
sudo apt install mongosh
```

```
mongosh "mongodb+srv://cluster0.pguxs.mongodb.net/" --username <username>
```

Customize the command slightly:

- Replace `<USERNAME>` and `<PASSWORD>` with the user you created.

You will be prompted for your password and should then gain a prompt:

```
root@a18a980325ad:/workspaces/course# mongosh "mongodb+srv://USERNAME:PASSWORD@cluster0.xxxx.mongodb.net" --username mongo
MongoDB shell version v4.4.4
Enter password: 
connecting to: mongodb://cluster0-shard-00-00.pguxs.mongodb.net:27017,cluster0-shard-00-01.pguxs.mongodb.net:27017,cluster0-shard-00-02.pguxs.mongodb.net:27017/?authSource=admin&compressors=disabled&gssapiServiceName=mongodb&replicaSet=atlas-f0pmyi-shard-0&ssl=true
Implicit session: session { "id" : UUID("bb19fed7-39b9-4089-b292-fbbcc5f0efcf") }
MongoDB server version: 4.4.4
MongoDB Enterprise atlas-f0pmyi-shard-0:PRIMARY> 
```

After watching the [**MongoDB Crash Course**]([https://www.youtube.com/watch?v=pWbMrx5rVBE](https://www.youtube.com/watch?v=ofme2o29ngU)) video, complete one of 
these two exercises:

## Exercise 1

This task uses sample data available on the Atlas Cloud console.

1. From within the Atlas Cloud console, load sample data using the `...` button in your cluster settings.
![Add sample data to MongoDB](https://nmagee.github.io/ds3002/images/mongo-sample-data.png)
2. Using your `mongo` shell, list your databases, select the `sample_weatherdata` set, then show collections within that:
```
show dbs;
use sample_weatherdata;
show collections;
```
3. This should show you there is a `data` collection within that database. Find all documents in the collection, then display them using the `.pretty()` flag, and finally count them:
```
db.data.find();
db.data.find().pretty();
db.data.find().count();
```
4. Search for all documents containing a `skyCondition.ceilingHeight.value` of `750` and count the results. Then display the results:
```
db.data.find({"skyCondition.ceilingHeight.value":750}).count();
db.data.find({"skyCondition.ceilingHeight.value":750}).pretty();
```
5. Retrieve a single document based on `ObjectId`:
```
db.data.find(ObjectId("5553a998e4b02cf7151195d3")).pretty();
```
6. Finally, using the code below insert a new document. After insertion, can you retrieve this document?
```
db.data.insertOne({
        "st" : "x+85600-124000",
        "ts" : ISODate("1984-03-07T13:00:00Z"),
        "position" : {
                "type" : "Point",
                "coordinates" : [
                        -124,
                        85.6
                ]
        },
        "elevation" : 8787,
        "callLetters" : "ROBZ",
        "qualityControlProcess" : "V020",
        "dataSource" : "3",
        "type" : "FM-13",
        "airTemperature" : {
                "value" : -22.9,
                "quality" : "1"
        },
        "dewPoint" : {
                "value" : -24.9,
                "quality" : "1"
        },
        "pressure" : {
                "value" : 1000.2,
                "quality" : "1"
        },
        "wind" : {
                "direction" : {
                        "angle" : 270,
                        "quality" : "1"
                },
                "type" : "N",
                "speed" : {
                        "rate" : 7,
                        "quality" : "1"
                }
        },
        "visibility" : {
                "distance" : {
                        "value" : 7000,
                        "quality" : "1"
                },
                "variability" : {
                        "value" : "N",
                        "quality" : "9"
                }
        },
        "skyCondition" : {
                "ceilingHeight" : {
                        "value" : 760,
                        "quality" : "1",
                        "determination" : "C"
                }
        }
});
```

## Exercise 2

This exercise walks you through creating your own database and populating a collection with your own data.

1. List DBs
```
show dbs
```
2. Show the DB you are currently in
```
db
```
3. Use a specific database. If it does not exist, it will be created.
```
use things
show dbs
```
Notice that your new database does not yet show up. This is because it needs to contain some documents first.
4. Insert a simple document. You will specify a collection within the `things` DB, and if it does not yet exist it will be created.
```
db.hobbies.insert({name:"horseback riding"})
```
5. List all documents in this collection. Repeat and make the output pretty.
```
db.hobbies.find()
db.hobbies.find().pretty()
```
You should get back the full document:
```
{
    "_id" : ObjectId("606b5e9d37c1606354c39e3d"),
    "name" : "horseback riding",
    "equipment" : [
        "horse",
        "saddle",
        "helmet"
    ]
}
```
Note
6. Insert several more documents, varied in their data complexity.
```
db.hobbies.insert({"name":"cycling","equipment":["bicycle","helmet","air pump"]})
db.hobbies.insert({"name":"basketball","equipment":["ball","shoes","court","rim","game"]})
db.hobbies.insert({"name":"archery","equipment":["bow","arrows"]})
```
7. View all documents again:
```
db.hobbies.find().pretty()
```
8. Notice your first document lacks any equipment values. To update it
```
db.hobbies.updateOne({name:"horseback riding"},{$set : {equipment:["horse","saddle","helmet"]}})
```
9. Search for all hobbies that require a helmet:
```
db.hobbies.find({equipment:"helmet"})
```
10. Upsert - adds a document when it does not exist from an `UPDATE` command
```
db.hobbies.update({name:"ultimate frisbee"},{name:"ultimate frisbee",equipment:["friends","frisbee"]},{upsert: true})
```
11. Remove a document
You can remove document based on any `find` parameters, such as a particular value. However, the most unique key for
single-row deletions is the `_id` of a particular row. Try deleting some documents (replace the `ObjectId` value with one
from your collection:
```
db.hobbies.remove(ObjectId("606b417e37c1606354c39e38"))
db.hobbies.remove({name:"archery"})
```

## Reference: CRUD Operations

**Create**
```
db.<db-name>.insertOne({...})
db.<db-name>.insertMany({...})
```

**Read**
```
db.<db-name>.find({...})
db.<db-name>.findOne({...})
```

**Update / Upsert**
```
db.<db-name>.update({{"<search-key>" : "<search-value>"},{$set : {"<key>": "<updated-value>"}}})
db.<db-name>.updateOne({SingleKeyToUpdate},{Set Command})
```

**Delete**
```
db.<db-name>.deleteOne(<search-condition>)
db.<db-name>.delete(<search-condition>)
```

## Integrating with `python3`

Try installing the `pymongo` library!

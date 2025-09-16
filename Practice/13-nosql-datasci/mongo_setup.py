#!/usr/bin/env python3

from pymongo import MongoClient, errors
import os
from database import *

# mongopass = os.getenv('MONGOPASS')
# uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/sample_restaurants"
# client = MongoClient(uri, username='nmagee', password=mongopass, connectTimeoutMS=200, retryWrites=True)

stats = client.stats
print(stats)

dbs = client.list_database_names()
print(dbs)

thisdb = client.sample_restaurants
colls = thisdb.list_collection_names()
print(colls)

restaurants = thisdb.restaurants
count = restaurants.count_documents({})
print(count, "restaurants")
italian = restaurants.count_documents({'cuisine': 'Italian'})
print(italian, "Italian restaurants")

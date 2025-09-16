#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import prettyprint as pprint
import os

mongopass = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pguxs.mongodb.net/sample_restaurants"
client = MongoClient(uri, username='mongo', password=mongopass, connectTimeoutMS=200, retryWrites=True)
sampler = client.sample_restaurants
restaurants = sampler.restaurants

# Get a single record - in natural order
get_one = restaurants.find_one()
print(dumps(get_one, indent=2))

# Get a specific record by property
get_another = restaurants.find({"borough":"Brooklyn"})
print(dumps(get_another, indent=2))

# # Get several based on a property and count
get_more = restaurants.count_documents({"borough":"Brooklyn"})
print(get_more)
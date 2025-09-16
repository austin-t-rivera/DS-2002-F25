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

# Updates a single record - the first matching criteria
# using the $set operator
restaurants.update_one({"name": "Mama Gina's Classy Kitchen"}, {"$set": {"freshness_factor":"8"}})

# Update a single record - add tags
# using the $push operator
restaurants.update_one({"name": "Mama Gina's Classy Kitchen"}, {"$push": {"tagz":"fancy"}})

# Updates several records - all matching criteria
# restaurants.update_many(new_record)

# The full list of mongodb operators is here:
# https://docs.mongodb.com/manual/reference/operator/

get_record = restaurants.find({"name":"Mama Gina's Classy Kitchen"})
print(dumps(get_record, indent=2))
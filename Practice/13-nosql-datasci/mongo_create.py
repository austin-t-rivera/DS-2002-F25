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

new_record = {
    "address": {
      "building": "502",
      "coord": [
        -73.976112,
        40.786714
      ],
      "street": "Fifth Avenue",
      "zipcode": "10024"
    },
    "borough": "Manhattan",
    "cuisine": "Chicken",
    "name": "Papa Gina's Classy Kitchen"
}

# Insert a single record
restaurants.insert_one(new_record)

get_record = restaurants.find({"name":"Papa Gina's Classy Kitchen"})
print(dumps(get_record, indent=2))
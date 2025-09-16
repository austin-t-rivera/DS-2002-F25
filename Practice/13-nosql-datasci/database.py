from pymongo import MongoClient, errors
from bson.json_util import dumps
import prettyprint as pprint
import os

# mongopass = os.getenv('MONGOPASS')
# uri = "mongodb+srv://cluster0.pguxs.mongodb.net/sample_restaurants"
# client = MongoClient(uri, username='mongo', password=mongopass, connectTimeoutMS=200, retryWrites=True)
# sampler = client.sample_restaurants
# restaurants = sampler.restaurants

mongopass = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/sample_restaurants"
client = MongoClient(uri, username='nmagee', password=mongopass, connectTimeoutMS=200, retryWrites=True)
sampler = client.sample_restaurants
restaurants = sampler.restaurants
from chalice import Chalice, Response
import os
import logging
import bson
import json
from pymongo import MongoClient

# Set up normal Mongo Atlas connection + db + collection
mongopass = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pguxs.mongodb.net/things"
client = MongoClient(uri, username='mongo', password=mongopass, connectTimeoutMS=200, retryWrites=True)
db = client.things
hobbies = db.hobbies

# Instantiate the Chalice app
app = Chalice(app_name='mongo-api')

# A simple base route
@app.route('/') # zone apex
def index():
    return {'hello': 'world', "methods": ["GET","POST"], "endpoints": ["/hobbies"]}

# get all hobbies
@app.route('/hobbies', methods=['GET'])
def get_hobbies():
    hobbies = db.hobbies.find({})
    results = []
    for hobby in hobbies:
        output = {}
        output['name'] = hobby['name']
        output['requires']= hobby['requires']
        results.append(output)
    return results

# post a new hobby
@app.route('/hobbies', methods=['POST'])
def post_hobbies():
    payload = app.current_request.json_body
    addthis = {}
    addthis['name'] = payload['name']
    addthis['requires'] = payload['requires']
    hobbies = db.hobbies.insert_one(addthis)
    return {"inserted": 200}
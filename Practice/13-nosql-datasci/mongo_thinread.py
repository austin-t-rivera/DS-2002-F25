#!/usr/bin/env python3

from bson.json_util import dumps
import database

get_more = database.restaurants.count_documents({"borough":"Brooklyn"})
print(get_more)
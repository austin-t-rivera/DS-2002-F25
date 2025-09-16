#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
from database import *
import json
import decimal
from decimal import Decimal
import datetime

def Decoder(o):
    if isinstance(o, datetime.datetime):
        return str(o)
    elif isinstance(o, decimal.Decimal):
        return o.__str__()

app = FastAPI()

class Track(BaseModel):
    id: str
    telem_1: float
    telem_2: float
    longitude: float
    latitude: float
    created_on: str

@app.get("/")  # zone apex
def read_root():
    return {"Hello": "Grabbing DB data!"}

@app.get("/tracking/{year}/{month}")
def get_tracks(year: int, month: int):
    # pay attention to dropped leading zeroes in months values
    month2 = format(month, '02')
    # perform a LIKE query
    query = f"SELECT * FROM tracking WHERE created_on LIKE '{year}-{month2}-%';"
    # set up cursor
    c=db.cursor()
    # execute query against cursor
    c.execute(query)
    # grab headers
    headers=[x[0] for x in c.description]
    # a fetchall to return results
    results = c.fetchall()
    # set up an empty container for results
    data=[]
    # iterate out results in a dict and append
    for result in results:
        data.append(dict(zip(headers,result)))
    # pass data through the json encoder above
    json_compatible_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_data)
    
@app.post("/tracking/", status_code=201)
async def add_track(item: Track):
    # get out columnar values from submitted payload
    id = item.id
    telem_1 = item.telem_1
    telem_2 = item.telem_2
    longitude = item.longitude
    latitude = item.latitude
    created_on = item.created_on
    # pay attention to quote-wrapped values
    query = f"INSERT INTO tracking (id,telem_1,telem_2,longitude,latitude,created_on) VALUES ('{id}','{telem_1}','{telem_2}','{longitude}','{latitude}','{created_on}');"
    try:
        c=db.cursor()
        c.execute(query)
        # This time commit instead of fetchall()
        results = db.commit()
        return {"created":"success","id":id}
        db.close()
    except (MySQLdb.Error) as e:
        error_data = str(e)
        raise HTTPException(status_code=400, detail=error_data)
        db.close()

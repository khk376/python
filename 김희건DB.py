import pymongo
from pymongo import MongoClient
conn = MongoClient('localhost', 27017)
db = conn.hkDB
collection = db.hk

#CREATE
collection.insert_one(
    {
        'name':"Heekun",
        'age': "26",
        'loc': "seoul"
    }
)
collection.insert_one(
    {
        'name':"Dongwon",
        'age': "25",
        'loc': "kyeounggi",
    }
)
results = collection.find()
for result in results:
    print(result)

#READ
collection.find_one()

results = collection.find()
for result in results:
    print(result)

#UPDATE
collection.update_one({'name': 'Heekun'},
                      {'$set': {'name': 'Hyunbae'}})

#DELETE
collection.delete_one(
    {
        'name':"Hyunbae",
        'age': "26",
        'loc': "seoul"
    }
)

import pymongo

from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.my_db
col_jobs = db.jobs

col_jobs.insert_one(
    {'title':'loop', 'likes':50},
    
)
print(db.list_collection_names())
ret = col_jobs.find_one({'title':'loop'})

print(ret  )
'''
from pymongo import MongoClient
client = MongoClient('localhost',27017)
#client = MongoClient("mongodb://localhost:27017/")
mydatabase = client['name_of_the_database']
#mydatabase = client.name_of_the_database
mycollection = mydatabase['mytable']
#mycollection = mydatabase.mytable
#insert_one() or insert_many()
rec = mytable.insert_one(record)
for i in mydatabase.mytable.find({title:'MongoDB and Python'}):
    print(i)
print(mydatabase.mytable.count({title:'MongoDB and Python'}))
print(mydatabase.mytable.find({title:'MongoDB and Python'}).count())
'''
print("........................................................................................................................")
from pymongo import MongoClient
try:
    client = MongoClient()
    print("connected successfully")
except:
    print("could not connect to mongodb")
db = client.mydatabase
collection = db.mytable
cursor = collection.find()
for record in cursor:
    print(record)
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#print(myclient.list_database_names())
#print(mydb.list_collection_names())

mydict = { "name": "John3", "address": "Park Lane 38" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

'''
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
'''
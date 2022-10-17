from pymongo import MongoClient

collection_name = 'cfigroup.se'

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['HAKA']

#Creating a collection
coll = db[collection_name]

#Inserting document into a collection
data = [
   {"_id": "101", "name": "Ram", "age": "26", "city": "Hyderabad"},
   {"_id": "102", "name": "Rahim", "age": "27", "city": "Bangalore"},
   {"_id": "103", "name": "Robert", "age": "28", "city": "Mumbai"}
]


print(client.list_database_names())
res = coll.insert_many(data)
print("Data inserted ......")
print(res.inserted_ids)
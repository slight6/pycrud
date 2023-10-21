

import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()
URI = os.getenv('MONGODB_URI')
# Create a new client and connect to the server
client = MongoClient(URI, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Getting a Database

db = client['pycrud']
print(f'Your database is: {db}')

# Creating a new collection

db.create_collection('users')
print(f'Your collections are: {db.list_collection_names()}')

# Getting a Collection

users = db['users']
print(f'Your collection is: {users}')

# Inserting a Document

users.insert_one({'name': 'John Doe', 'age': 25})
print(f'You inserted a document: {users.find_one()}')

# Inserting Multiple Documents

users.insert_many([
    {'name': 'Jane Doe', 'age': 25},
    {'name': 'John Smith', 'age': 30},
    {'name': 'Jane Smith', 'age': 30}
])

# Finding Documents

users.find_one({'name': 'John Doe'})

# Finding All Documents

users.find()

# Finding Documents with a Query Filter

output = users.find({'age': 30})
print(f'We found the users with the ages of 30: {output}')

# Updating Documents

users.update_one({'name': 'John Doe'}, {'$set': {'age': 26}})
users.update_many({'age': 30}, {'$set': {'age': 31}})

# Deleting Collections

users.delete_many({'age': 31, 'age': 26, 'age': 25})


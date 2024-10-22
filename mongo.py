from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# Create
result = db.my_collection.insert_one({
    'name': 'John',
    'age': 28
})

# Read
result = db.my_collection.find_one({'name': 'John'})
print(result)

# Update
result = db.my_collection.update_one(
    {'name': 'John'},
    {'$set': {'age': 30}}
)

# Delete
result = db.my_collection.delete_one({'name': 'John'})

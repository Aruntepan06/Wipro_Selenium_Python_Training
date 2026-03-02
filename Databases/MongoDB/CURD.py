from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("Connected successfully")

db = client["school"]          # create the database
collection = db["students"]    # create collection

# insert data to the collection
students = [
    {"name": "Ravi", "subject": "Science", "marks": 90},
    {"name": "Sneha", "subject": "Math", "marks": 78},
    {"name": "Kiran", "subject": "Science", "marks": 88}
]

collection.insert_many(students)

# printing the data
for doc in collection.find():
    print(doc)

# update the data
collection.update_one(
    {"name": "Ravi"},
    {"$set": {"marks": 95}}
)

# deletion
collection.delete_one({"name": "Sneha"})

import pandas as pd

data = list(collection.find())
df = pd.DataFrame(data)

print(df)

print(df["marks"].mean())

print(df[df["marks"] == df["marks"].max()])

print(df.groupby("subject")["marks"].mean())
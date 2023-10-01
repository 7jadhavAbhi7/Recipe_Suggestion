import pymongo 
import json

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['RecipeSuggestionSystem']
collection = db['Recipes']
idx = 0 
for document in collection.find():
    print(idx, document["_id"])
    idx += 1
    collection.update_one(
        {"_id": document["_id"]},
        {"$set": {
        "ingredients": json.loads(json.dumps(eval(str(document["ingredients"])))),
        "steps": json.loads(json.dumps(eval(str(document["steps"])))),
        "tags": json.loads(json.dumps(eval(str(document["tags"]))))
        }}
    )

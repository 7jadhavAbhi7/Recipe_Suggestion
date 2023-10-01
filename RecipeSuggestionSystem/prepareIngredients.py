import pymongo 
import json

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['RecipeSuggestionSystem']
collection = db['Recipes']

ingredients = set()
for document in collection.find():
    ingredients.update(set(document["ingredients"]))

print("Total Ingredients:", len(ingredients))

ingredients = sorted(ingredients)

with open('ingredients.py', 'w') as f:
    f.write("ingredientsSet = " + str(ingredients))

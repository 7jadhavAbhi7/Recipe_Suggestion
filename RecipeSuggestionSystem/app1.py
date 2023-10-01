from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/RecipeSuggestionSystem"
mongo = PyMongo(app)

# Create a new recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    recipe = request.json
    result = mongo.db.recipes.insert_one(recipe)
    return jsonify(str(result.inserted_id))

# Retrieve all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = mongo.db.recipes.find()
    response = []
    for recipe in recipes:
        recipe['_id'] = str(recipe['_id'])
        response.append(recipe)
    return jsonify(response)

# Retrieve a single recipe by ID
@app.route('/recipes/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if recipe:
        recipe['_id'] = str(recipe['_id'])
        return jsonify(recipe)
    else:
        return jsonify({'error': 'Recipe not found'})

# Update an existing recipe
@app.route('/recipes/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = request.json
    result = mongo.db.recipes.update_one({'_id': ObjectId(recipe_id)}, {'$set': recipe})
    if result.modified_count == 1:
        return jsonify({'message': 'Recipe updated successfully'})
    else:
        return jsonify({'error': 'Recipe not found'})

# Delete a recipe
@app.route('/recipes/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    result = mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Recipe deleted successfully'})
    else:
        return jsonify({'error': 'Recipe not found'})

if __name__ == '__main__':
    app.run(debug=True)
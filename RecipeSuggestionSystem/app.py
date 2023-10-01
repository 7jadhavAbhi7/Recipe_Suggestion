# from flask import Flask, render_template

# app = Flask (__name__, template_folder='template')

# @app.route('/')
# def home ():
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
from flask import Flask
from flask import request, render_template
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['RecipeSuggestionSystem']
collection = db['Recipes']
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index2.html')
@app.route('/filter', methods=['POST'])
def filter_data():
    selected_categories = request.form.getlist('minutes')
    # Code to filter data based on selected categories
    filtered_data = collection.find({'category': {'$in': selected_categories}})
    return render_template('results.html', data=filtered_data)


app.run(debug=True)

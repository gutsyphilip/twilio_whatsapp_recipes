
from pymongo import MongoClient

client = MongoClient('mongodb://localhost/')

recipes = client['twilio']['recipes']

def search_recipe(search_word):
    cursor = recipes.find({'$text': {'$search': search_word}})
    result = []
    for data in cursor:
        result.append(data)
    return result
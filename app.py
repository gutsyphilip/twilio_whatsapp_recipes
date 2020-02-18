
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from services.recipes import search_recipe
from utils.message import convert_result_to_message

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/whatsapp', methods=['POST'])
def reply_with_recipe_info():
    food_name = request.values.get('Body')
    print('Message sent', food_name)
    recipes = search_recipe(food_name)
    message = convert_result_to_message(recipes)
    response = MessagingResponse()
    response.message(message)
    return str(response)


if __name__ == '__main__':
    app.run()
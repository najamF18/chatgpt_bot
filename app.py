from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from chatbot.chat_gpt_bot_api import ChatGptBotApi

load_dotenv()

app = Flask(__name__)

api_key = os.environ.get('GPT_API_KEY')
api = ChatGptBotApi(api_key)


@app.route('/')
def home():
    return "Welcome to the Chatbot API!"


@app.route('/create/prompt', methods=['POST'])
def create_prompt():
    user_message = request.json['message']
    res = api.create_prompt(user_message)
    return jsonify(res)


@app.route('/get/response/<int:prompt_index>', methods=['GET'])
def get_response(prompt_index):
    res = api.get_response(prompt_index)
    return res


@app.route('/update/prompt/<int:prompt_index>', methods=['PUT'])
def update_prompt(prompt_index):
    new_prompt = request.json['message']
    res = api.update_prompt(prompt_index, new_prompt)
    return jsonify(res)


@app.route('/delete/prompt/<int:prompt_index>', methods=['DELETE'])
def delete_prompt(prompt_index):
    res = api.delete_prompt(prompt_index)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)

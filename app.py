from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Chatbot API!"
if __name__ == '__main__':
    app.run(debug=True)

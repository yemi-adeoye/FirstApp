# import flask
from flask import Flask, jsonify, request

# initialize app
app = Flask(__name__)


@app.get('/greet')
def index():

    name = request.args.get('name')
    response = {"data": f"Greetings {name}"}
    return jsonify(response)


@app.get('/')
def home():
    return 'Hello Welcome to Flask!'


if __name__ == '__main__':
    app.run(debug=True)

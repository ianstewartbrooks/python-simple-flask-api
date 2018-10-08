import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

names = [
    {'id': 0, 'name': 'ian'},
    {'id': 1, 'name': 'kath'},
    {'id': 2, 'name': 'emily'}
]


# Used to set headers
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/', methods=['GET'])
def home():
    return '<h1>Home Page</h1>'


# A route to return all of the names in the list.
@app.route('/api/v1/resources/names/all', methods=['GET'])
def api_names_all():
    return jsonify(names)

app.run()
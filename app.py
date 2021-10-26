import re
from flask import Flask, request
from flask_basicauth import BasicAuth

# create a new flask app
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'john'
app.config['BASIC_AUTH_PASSWORD'] = 'doe'

basic_auth = BasicAuth(app)


@app.route('/')
def home():
    return("hello Flask world!")

# by default only GET so let's make entry point for POST for our logs
# DS logs can be TXT or JSON format.


@app.route('/log', methods=['POST'])
@basic_auth.required
def log():
    if request.content_type == 'application/json':
        app.logger.info("JSON: %s", request.get_json())
    else:
        app.logger.info("TXT: %s", request.data)

    return('', 204)

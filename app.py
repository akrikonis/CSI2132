# Libraries
from flask import Flask # Simple rest api library
from db import DB # Custom DB class for handling all DB related connections

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


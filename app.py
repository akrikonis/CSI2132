# Libraries
import configparser # Read credentials to connect to database
from flask import Flask # Simple rest api library
from db import DB # Custom DB class for handling all DB related connections

# Get credentials and connect to database
config = configparser.ConfigParser()
config.read(".env")
database = DB(config["ACCOUNT"]["user"], config["ACCOUNT"]["password"], "web0.eecs.uottawa.ca", 15432, "group_b04_g57")
database.connect()

app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello, World!'


# Libraries
import json # For json response
import configparser # Read credentials to connect to database
from flask import Flask # Simple rest api library
from db import DB # Custom DB class for handling all DB related connections

# Get credentials and connect to database
config = configparser.ConfigParser()
config.read(".env")
database = DB(config["ACCOUNT"]["user"], config["ACCOUNT"]["password"], "web0.eecs.uottawa.ca", 15432, "group_b04_g57")
database.connect(useLocal=True) #For local testing without pg admin

app = Flask(__name__) 

@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>CSI2132 Project</h1>
    <h3> Section 4 Group 57 </h3>
    <p> For a full list of available querries click <a href="https://github.com/akrikonis/CSI2132">here.</a> </p>
    '''


@app.route('/api/parentHotels', methods=['GET'])
def flask_parentHotels():
    return json.dumps(database.fetch("SELECT * FROM ParentHotelBrand;"))

app.run()
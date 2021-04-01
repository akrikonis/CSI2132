# Libraries
import json # For json response
import configparser # Read credentials to connect to database
from flask import Flask, request # Simple rest api library
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
    <h3> Section B04 Group 57 </h3>
    <p> For a full list of available querries click <a href="https://github.com/akrikonis/CSI2132">here.</a> </p>
    '''

#Post will insert new data, get will retrieve all data, delete will delete data
@app.route('/api/parentHotels', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_parentHotels():
    if request.method == 'POST':
        NumOfHotels = request.form["NumOfHotels"]
        ParentHotelID = request.form["ParentHotelID"]
        CentralLocation = request.form["CentralLocation"]
        EmailAddress = request.form["EmailAddress"]
        PhoneNumber = request.form["PhoneNumber"]
        database.commit("INSERT INTO ParentHotelBrand VALUES ("+ParentHotelID+","+NumOfHotels+",'"+CentralLocation+"','"+EmailAddress+"','"+PhoneNumber+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM ParentHotelBrand;"))
    elif request.method == 'PATCH':
        NumOfHotels = request.form["NumOfHotels"]
        ParentHotelID = request.form["ParentHotelID"]
        CentralLocation = request.form["CentralLocation"]
        EmailAddress = request.form["EmailAddress"]
        PhoneNumber = request.form["PhoneNumber"]
        database.commit("UPDATE ParentHotelBrand SET NumOfHotels="+NumOfHotels+", CentralLocation='"+CentralLocation+"', EmailAddress='"+EmailAddress+"', PhoneNumber='"+PhoneNumber+"' WHERE ParentHotelID="+ParentHotelID+";")
        return ""
    elif request.method == 'DELETE':
        ParentHotelID = request.form["ParentHotelID"]
        database.commit("DELETE FROM ParentHotelBrand WHERE ParentHotelID="+ParentHotelID+";")
        return ""

app.run()
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
    <p> For project files click <a href="https://github.com/akrikonis/CSI2132">here.</a> </p>
    '''

#ParentHotelBrand Endpoint
@app.route('/api/parentHotel', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
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

#Customer Endpoint
@app.route('/api/customer', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_parentHotels():
    if request.method == 'POST':
        FullName = request.form["FullName"]
        CusID = request.form["CusID"]
        Address = request.form["Address"]
        DateOfReg = request.form["DateOfReg"]
        Phone = request.form["Phone"]
        SIN = request.form["SIN"]
        database.commit("INSERT INTO Customer VALUES ("+CusID+",'"+FullName+"','"+Address+"','"+DateOfReg+"','"+SIN+"','"+Phone+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM Customer;"))
    elif request.method == 'PATCH':
        FullName = request.form["FullName"]
        CusID = request.form["CusID"]
        Address = request.form["Address"]
        DateOfReg = request.form["DateOfReg"]
        Phone = request.form["Phone"]
        SIN = request.form["SIN"]
        database.commit("UPDATE Customer SET FullName="+FullName+", Address='"+Address+"', DateOfReg='"+DateOfReg+"', SIN='"+SIN+"', Phone='"+Phone+"' WHERE CusID="+CusID+";")
        return ""
    elif request.method == 'DELETE':
        CusID = request.form["CusID"]
        database.commit("DELETE FROM Customer WHERE CusID="+CusID+";")
        return ""

#Employee Endpoint
@app.route('/api/customer', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_parentHotels():
    if request.method == 'POST':
        FullName = request.form["FullName"]
        EmpID = request.form["EmpID"]
        Address = request.form["Address"]
        Salary = request.form["Salary"]
        Role = request.form["Role"]
        ParentHotelID = request.form["ParentHotelID"]
        SIN = request.form["SIN"]
        database.commit("INSERT INTO Employee VALUES ("+EmpID+",'"+FullName+"','"+Address+"',"+Salary+",'"+Role+"',"+ParentHotelID+",'"+SIN+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM Employee;"))
    elif request.method == 'PATCH':
        FullName = request.form["FullName"]
        EmpID = request.form["EmpID"]
        Address = request.form["Address"]
        Salary = request.form["Salary"]
        Role = request.form["Role"]
        ParentHotelID = request.form["ParentHotelID"]
        SIN = request.form["SIN"]
        database.commit("UPDATE Employee SET FullName="+FullName+", Address='"+Address+"', Salary="+Salary+", Role='"+Role+"', ParentHotelID="+ParentHotelID+", SIN='"+SIN+" WHERE EmpID="+EmpID+";")
        return ""
    elif request.method == 'DELETE':
        CusID = request.form["CusID"]
        database.commit("DELETE FROM Employee WHERE EmpID="+EmpID+";")
        return ""

app.run()
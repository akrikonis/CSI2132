# Libraries
import json # For json response
import atexit # For proper db disconnect on app exit
import configparser # Read credentials to connect to database
from flask import Flask, request # Simple rest api library
from db import DB # Custom DB class for handling all DB related connections

# Get credentials and connect to database
config = configparser.ConfigParser()
config.read(".env")
database = DB(config["ACCOUNT"]["user"], config["ACCOUNT"]["password"], "web0.eecs.uottawa.ca", 15432, "group_b04_g57")
database.connect(useLocal=True) #For local testing without pg admin

# Disconnect from database function
def shutdown():
    database.close()
    print("Connection Closed")

atexit.register(shutdown) # Disconnect from database

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
def flask_customer():
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
        database.commit("UPDATE Customer SET FullName='"+FullName+"', Address='"+Address+"', DateOfReg='"+DateOfReg+"', SIN='"+SIN+"', Phone='"+Phone+"' WHERE CusID="+CusID+";")
        return ""
    elif request.method == 'DELETE':
        CusID = request.form["CusID"]
        database.commit("DELETE FROM Customer WHERE CusID="+CusID+";")
        return ""

#Employee Endpoint
@app.route('/api/customer', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_employee():
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
        database.commit("UPDATE Employee SET FullName='"+FullName+"', Address='"+Address+"', Salary="+Salary+", Role='"+Role+"', ParentHotelID="+ParentHotelID+", SIN='"+SIN+"' WHERE EmpID="+EmpID+";")
        return ""
    elif request.method == 'DELETE':
        CusID = request.form["CusID"]
        database.commit("DELETE FROM Employee WHERE EmpID="+EmpID+";")
        return ""

#Hotel Chain Endpoint
@app.route('/api/hotelChain', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_hotelChain():
    if request.method == 'POST':
        StarCategory = request.form["StarCategory"]
        HotelID = request.form["HotelID"]
        NumOfRooms = request.form["NumOfRooms"]
        PhoneNumber = request.form["PhoneNumber"]
        Address = request.form["Address"]
        ContactEmail = request.form["ContactEmail"]
        ParentHotelID = request.form["ParentHotelID"]
        Name = request.form["Name"]
        database.commit("INSERT INTO HotelChain VALUES ("+HotelID+","+StarCategory+","+NumOfRooms+",'"+PhoneNumber+"','"+Address+"','"+ContactEmail+"',"+ParentHotelID+",'"+Name+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM HotelChain;"))
    elif request.method == 'PATCH':
        StarCategory = request.form["StarCategory"]
        HotelID = request.form["HotelID"]
        NumOfRooms = request.form["NumOfRooms"]
        PhoneNumber = request.form["PhoneNumber"]
        Address = request.form["Address"]
        ContactEmail = request.form["ContactEmail"]
        ParentHotelID = request.form["ParentHotelID"]
        Name = request.form["Name"]
        database.commit("UPDATE HotelChain SET StarCategory="+StarCategory+", NumOfRooms="+NumOfRooms+", PhoneNumber='"+PhoneNumber+"', Address='"+Address+"', ContactEmail='"+ContactEmail+"', ParentHotelID="+ParentHotelID+", Name='"+Name+"' WHERE HotelID="+HotelID+";")
        return ""
    elif request.method == 'DELETE':
        CusID = request.form["CusID"]
        database.commit("DELETE FROM HotelChain WHERE HotelID="+HotelID+";")
        return ""

#Room Endpoint
@app.route('/api/room', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_room():
    if request.method == 'POST':
        Price = request.form["Price"]
        RoomID = request.form["RoomID"]
        Amenities = request.form["Amenities"]
        Extendable = request.form["Extendable"]
        Mountainview = request.form["Mountainview"]
        Seaview = request.form["Seaview"]
        Capacity = request.form["Capacity"]
        Available = request.form["Available"]
        HotelID = request.form["HotelID"]
        database.commit("INSERT INTO Room VALUES ("+RoomID+","+Price+",'"+Amenities+"','"+Extendable+"','"+Mountainview+"','"+Seaview+"',"+Capacity+",'"+Available+"',"+HotelID+");")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM HotelChain;"))
    elif request.method == 'PATCH':
        Price = request.form["Price"]
        RoomID = request.form["RoomID"]
        Amenities = request.form["Amenities"]
        Extendable = request.form["Extendable"]
        Mountainview = request.form["Mountainview"]
        Seaview = request.form["Seaview"]
        Capacity = request.form["Capacity"]
        Available = request.form["Available"]
        HotelID = request.form["HotelID"]
        database.commit("UPDATE Room SET Price="+Price+", Amenities='"+Amenities+"', Extendable='"+Extendable+"', Mountainview='"+Mountainview+"', Seaview='"+Seaview+"', Capacity="+Capacity+", Available='"+Available+"', HotelID="+HotelID+" WHERE RoomID="+RoomID+";")
        return ""
    elif request.method == 'DELETE':
        RoomID = request.form["RoomID"]
        database.commit("DELETE FROM Room WHERE RoomID="+RoomID+";")
        return ""

#Booking Endpoint
@app.route('/api/booking', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_booking():
    if request.method == 'POST':
        BookingID = request.form["BookingID"]
        Occupants = request.form["Occupants"]
        RoomID = request.form["RoomID"]
        CusID = request.form["CusID"]
        StartDate = request.form["StartDate"]
        HotelID = request.form["HotelID"]
        database.commit("INSERT INTO Booking VALUES ("+BookingID+","+Occupants+","+RoomID+","+CusID+",'"+StartDate+"',"+HotelID+");")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM HotelChain;"))
    elif request.method == 'PATCH':
        BookingID = request.form["BookingID"]
        Occupants = request.form["Occupants"]
        RoomID = request.form["RoomID"]
        CusID = request.form["CusID"]
        StartDate = request.form["StartDate"]
        HotelID = request.form["HotelID"]
        database.commit("UPDATE Booking SET Occupants="+Occupants+", RoomID="+RoomID+", CusID="+CusID+", StartDate='"+StartDate+"', HotelID="+HotelID+" WHERE BookingID="+BookingID+";")
        return ""
    elif request.method == 'DELETE':
        BookingID = request.form["BookingID"]
        database.commit("DELETE FROM Booking WHERE BookingID="+BookingID+";")
        return ""

app.run()
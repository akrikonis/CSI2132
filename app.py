# Libraries
import json # For json response
import atexit # For proper db disconnect on app exit
import configparser # Read credentials to connect to database
from flask import Flask, request # Simple rest api library
from flask_cors import CORS # allow Cors for flask server
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
CORS(app)

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
        NumOfHotels = request.json["NumOfHotels"]
        ParentHotelID = request.json["ParentHotelID"]
        CentralLocation = request.json["CentralLocation"]
        EmailAddress = request.json["EmailAddress"]
        PhoneNumber = request.json["PhoneNumber"]
        database.commit("INSERT INTO ParentHotelBrand VALUES ("+ParentHotelID+","+NumOfHotels+",'"+CentralLocation+"','"+EmailAddress+"','"+PhoneNumber+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM ParentHotelBrand;"))
    elif request.method == 'PATCH':
        NumOfHotels = request.json["NumOfHotels"]
        ParentHotelID = request.json["ParentHotelID"]
        CentralLocation = request.json["CentralLocation"]
        EmailAddress = request.json["EmailAddress"]
        PhoneNumber = request.json["PhoneNumber"]
        database.commit("UPDATE ParentHotelBrand SET NumOfHotels="+NumOfHotels+", CentralLocation='"+CentralLocation+"', EmailAddress='"+EmailAddress+"', PhoneNumber='"+PhoneNumber+"' WHERE ParentHotelID="+ParentHotelID+";")
        return ""
    elif request.method == 'DELETE':
        ParentHotelID = request.json["ParentHotelID"]
        database.commit("DELETE FROM ParentHotelBrand WHERE ParentHotelID="+ParentHotelID+";")
        return ""

#Customer Endpoint
@app.route('/api/customer', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_customer():
    if request.method == 'POST':
        FullName = request.json["FullName"]
        CusID = request.json["CusID"]
        Address = request.json["Address"]
        DateOfReg = request.json["DateOfReg"]
        Phone = request.json["Phone"]
        SIN = request.json["SIN"]
        database.commit("INSERT INTO Customer VALUES ("+str(CusID)+",'"+str(FullName)+"','"+str(Address)+"','"+str(DateOfReg)+"','"+str(SIN)+"','"+str(Phone)+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM Customer;"))
    elif request.method == 'PATCH':
        FullName = request.json["FullName"]
        CusID = request.json["CusID"]
        Address = request.json["Address"]
        DateOfReg = request.json["DateOfReg"]
        Phone = request.json["Phone"]
        SIN = request.json["SIN"]
        database.commit("UPDATE Customer SET FullName='"+FullName+"', Address='"+Address+"', DateOfReg='"+DateOfReg+"', SIN='"+SIN+"', Phone='"+Phone+"' WHERE CusID="+str(CusID)+";")
        return ""
    elif request.method == 'DELETE':
        CusID = request.json["CusID"]
        database.commit("DELETE FROM Customer WHERE CusID="+CusID+";")
        return ""

#Employee Endpoint
@app.route('/api/employee', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_employee():
    if request.method == 'POST':
        FullName = request.json["FullName"]
        EmpID = request.json["EmpID"]
        Address = request.json["Address"]
        Salary = request.json["Salary"]
        Role = request.json["Role"]
        ParentHotelID = request.json["ParentHotelID"]
        SIN = request.json["SIN"]
        database.commit("INSERT INTO Employee VALUES ("+str(EmpID)+",'"+FullName+"','"+Address+"',"+str(Salary)+",'"+Role+"',"+str(ParentHotelID)+",'"+SIN+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM Employee;"))
    elif request.method == 'PATCH':
        FullName = request.json["FullName"]
        EmpID = request.json["EmpID"]
        Address = request.json["Address"]
        Salary = request.json["Salary"]
        Role = request.json["Role"]
        ParentHotelID = request.json["ParentHotelID"]
        SIN = request.json["SIN"]
        database.commit("UPDATE Employee SET FullName='"+FullName+"', Address='"+Address+"', Salary="+str(Salary)+", Role='"+Role+"', ParentHotelID="+str(ParentHotelID)+", SIN='"+SIN+"' WHERE EmpID="+str(EmpID)+";")
        return ""
    elif request.method == 'DELETE':
        EmpID = request.json["EmpID"]
        database.commit("DELETE FROM Employee WHERE EmpID="+str(EmpID)+";")
        return ""

#Hotel Chain Endpoint
@app.route('/api/hotelChain', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_hotelChain():
    if request.method == 'POST':
        StarCategory = request.json["StarCategory"]
        HotelID = request.json["HotelID"]
        NumOfRooms = request.json["NumOfRooms"]
        PhoneNumber = request.json["PhoneNumber"]
        Address = request.json["Address"]
        ContactEmail = request.json["ContactEmail"]
        ParentHotelID = request.json["ParentHotelID"]
        Name = request.json["Name"]
        database.commit("INSERT INTO HotelChain VALUES ("+str(HotelID)+","+str(StarCategory)+","+str(NumOfRooms)+",'"+PhoneNumber+"','"+Address+"','"+ContactEmail+"',"+str(ParentHotelID)+",'"+Name+"');")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM HotelChain;"))
    elif request.method == 'PATCH':
        StarCategory = request.json["StarCategory"]
        HotelID = request.json["HotelID"]
        NumOfRooms = request.json["NumOfRooms"]
        PhoneNumber = request.json["PhoneNumber"]
        Address = request.json["Address"]
        ContactEmail = request.json["ContactEmail"]
        ParentHotelID = request.json["ParentHotelID"]
        Name = request.json["Name"]
        database.commit("UPDATE HotelChain SET StarCategory="+str(StarCategory)+", NumOfRooms="+str(NumOfRooms)+", PhoneNumber='"+PhoneNumber+"', Address='"+Address+"', ContactEmail='"+ContactEmail+"', ParentHotelID="+str(ParentHotelID)+", Name='"+Name+"' WHERE HotelID="+str(HotelID)+";")
        return ""
    elif request.method == 'DELETE':
        HotelID = request.json["HotelID"]
        database.commit("DELETE FROM HotelChain WHERE HotelID="+HotelID+";")
        return ""

#Room Endpoint
@app.route('/api/room', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_room():
    if request.method == 'POST':
        Price = request.json["Price"]
        RoomID = request.json["RoomID"]
        Amenities = request.json["Amenities"]
        Extendable = request.json["Extendable"]
        Mountainview = request.json["Mountainview"]
        Seaview = request.json["Seaview"]
        Capacity = request.json["Capacity"]
        Available = request.json["Available"]
        HotelID = request.json["HotelID"]
        database.commit("INSERT INTO Room VALUES ("+str(RoomID)+","+str(Price)+",'"+Amenities+"','"+Extendable+"','"+Mountainview+"','"+Seaview+"',"+str(Capacity)+",'"+Available+"',"+str(HotelID)+");")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM Room;"))
    elif request.method == 'PATCH':
        Price = request.json["Price"]
        RoomID = request.json["RoomID"]
        Amenities = request.json["Amenities"]
        Extendable = request.json["Extendable"]
        Mountainview = request.json["Mountainview"]
        Seaview = request.json["Seaview"]
        Capacity = request.json["Capacity"]
        Available = request.json["Available"]
        HotelID = request.json["HotelID"]
        database.commit("UPDATE Room SET Price="+str(Price)+", Amenities='"+Amenities+"', Extendable='"+Extendable+"', Mountainview='"+Mountainview+"', Seaview='"+Seaview+"', Capacity="+str(Capacity)+", Available='"+Available+"', HotelID="+str(HotelID)+" WHERE RoomID="+str(RoomID)+";")
        return ""
    elif request.method == 'DELETE':
        RoomID = request.json["RoomID"]
        database.commit("DELETE FROM Room WHERE RoomID="+str(RoomID)+";")
        return ""

#Book room endpoint
@app.route('/api/room/book', methods=['PATCH'])
def flask_room_book():
    RoomID = request.json["RoomID"]
    database.commit("UPDATE Room SET Available='booked' WHERE RoomID="+str(RoomID)+";")
    return ""

#Rent room endpoint
@app.route('/api/room/rent', methods=['PATCH'])
def flask_room_rent():
    RoomID = request.json["RoomID"]
    database.commit("UPDATE Room SET Available='rented' WHERE RoomID="+str(RoomID)+";")
    return ""

#Booking Endpoint
@app.route('/api/booking', methods=['GET', 'POST', 'PATCH' , 'DELETE'])
def flask_booking():
    if request.method == 'POST':
        BookingID = request.json["BookingID"]
        Occupants = request.json["Occupants"]
        RoomID = request.json["RoomID"]
        CusID = request.json["CusID"]
        StartDate = request.json["StartDate"]
        HotelID = request.json["HotelID"]
        database.commit("INSERT INTO Booking VALUES ("+str(BookingID)+","+str(Occupants)+","+str(RoomID)+","+str(CusID)+",'"+str(StartDate)+"',"+str(HotelID)+");")
        return ""
    elif request.method == 'GET':
        return json.dumps(database.fetch("SELECT * FROM HotelChain;"))
    elif request.method == 'PATCH':
        BookingID = request.json["BookingID"]
        Occupants = request.json["Occupants"]
        RoomID = request.json["RoomID"]
        CusID = request.json["CusID"]
        StartDate = request.json["StartDate"]
        HotelID = request.json["HotelID"]
        database.commit("UPDATE Booking SET Occupants="+Occupants+", RoomID="+RoomID+", CusID="+CusID+", StartDate='"+StartDate+"', HotelID="+HotelID+" WHERE BookingID="+BookingID+";")
        return ""
    elif request.method == 'DELETE':
        BookingID = request.json["BookingID"]
        database.commit("DELETE FROM Booking WHERE BookingID="+BookingID+";")
        return ""

app.run()
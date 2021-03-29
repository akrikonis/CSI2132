# Libraries

# PG Admin 4
import psycopg2
from psycopg2 import Error

# SQLite3
import sqlite3

# Example for retrieving data:
# from db import DB
# x = DB() #No credentials are needed for sqlite3
# x.connect(useLocal=True) #set useLocal to true for sqlite3
# x.fetch("SELECT * FROM ParentHotelBrand")

# Example for adding data:
# from db import DB
# x = DB() #No credentials are needed for sqlite3
# x.connect(useLocal=True) #set useLocal to true for sqlite3
# x.commit("INSERT INTO ParentHotelBrand VALUES (whatever)")

# Custom DB class for handling all DB related connections
class DB:
    # Standard init
    def __init__(self, user=None, password=None, host=None, port=None, database=None):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
    
    # Connect
    def connect(self, useLocal=False):
        if useLocal:
            self.connection = sqlite3.connect('local.db')
        else:
            try:
                self.connection = psycopg2.connect(user=self.user,
                                                password=self.password,
                                                host=self.host,
                                                port=self.port,
                                                database=self.database)
            except (Exception, Error) as error:
                print("Error while connecting to PostgreSQL", error)
                exit(1)
    
    # For SQL statements which modify the database
    def commit(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        self.connection.commit()
        cursor.close()

    # For SQL statements which return data
    def fetch(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        data = cursor.fetchall()
        cursor.close()
        return data
    
    # End connection
    def close(self):
        self.connection.close()
        
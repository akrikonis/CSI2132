# Libraries
import psycopg2
from psycopg2 import Error

# Custom DB class for handling all DB related connections
class DB:
    # Standard init
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
    
    # Connect
    def connect(self):
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
        
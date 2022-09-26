import mysql.connector
from datetime import datetime

class connectMysqlServer:
    def __init__(self,address,user,password,database):
        # Connect to Mysql Server
        self.db = mysql.connector.connect(
            host=address,
            user=user,
            password=password,
            database=database
        )

        # Save class arguments for future use
        self.address = address,
        self.user = user,
        self.password = password,
        self.database = database,
    
    def make_query(self, query):
        db = self.db
        mycursor = db.cursor()
        db_query = mycursor.execute(query)
        for x in mycursor:
            print(x)
        return db_query

db_param = (
    "localhost",
    "python-test-user",
    "negro123",
    "practicedatabase"
)

mysql_server = connectMysqlServer("localhost", "python-test-user", "negro123", "practicedatabase")
query = mysql_server.make_query("SELECT * from User")

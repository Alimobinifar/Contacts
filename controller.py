import mysql.connector

class DataBase:
    def __init__(self) :
        self.conn=mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "contacts"
        )
        
        
    
    def information(self):
        query = "select * from phone_book"
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result

x= DataBase()
data=x.information()
print(data)
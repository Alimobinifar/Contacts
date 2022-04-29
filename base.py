import mysql.connector


class Connection:

    def __init__(self) :
        self.conn=mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "phonebook"
        )
        
        
    
    def information(self):
        query = "select id,name,family,phone from contact"
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result
    

    def register_on_db(self,name,family,phone):

        query = f"insert into contacts (name,family) VALUES('{name}','{family}')"
        cur = self.conn.cursor()
        cur.execute(query)
        
        q2 = "select id from contacts ORDER BY id DESC LIMIT 1"
        cur.execute(q2)
        data = cur.fetchall()


        q3  = f"insert into phones(contact_id , phone)VALUES('{data[0][0]}','{phone}') "
        cur.execute(q3)

    
    def delete_contact(self,id):
        q1 = f"delete from contacts where id = {id}"
        q2 = f"delete from phones where contact_id = {id}"
        cur = self.conn.cursor()
        cur.execute(q1)
        cur.execute(q2)

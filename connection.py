import mysql.connector 

def connection_mysql():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydbfromlocal"
    )
    return conn

# conn=connection_mysql()

# if conn.is_connected():
#     print("connection successful")
# else:
#     print("failed")
import mysql.connector
from mysql.connector import Error

def connection():

    try:

     database = mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="root",
         database="projeto",
         port=3307
     )

     if database.is_connected():

         return database

    except Error as error:

        print("erro ao se conectar: ", error)
        return None

import mysql.connector
from mysql.connector import Error

def connection():

    try:

     database = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
     )

     if database.is_connected():

         return database

    except Error as error:

        print("erro ao se conectar: ", error)
        return None

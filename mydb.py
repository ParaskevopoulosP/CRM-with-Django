import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = '123456!a'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print("Connected")
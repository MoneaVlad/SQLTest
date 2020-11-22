import string

# pip3 install mysql-connector-python
import mysql.connector

from random import randrange, random

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="admin",
    password="admin",
    database="books",
    auth_plugin='mysql_native_password'
)

# ONE TIME SETUP
mycursor = mydb.cursor()
sql = "CREATE TABLE books (code INT, name VARCHAR(20))"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
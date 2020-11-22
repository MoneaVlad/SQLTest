import string

# pip3 install mysql-connector-python
import mysql.connector

from random import randrange
import random

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="admin",
    password="admin",
    database="books",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

def test_one_write():
    sql = "INSERT INTO books (code, name) VALUES (%s, %s)"
    val = (randrange(10000), ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
    mycursor.execute(sql, val)
    mydb.commit()

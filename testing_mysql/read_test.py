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

def test_one_read():
    sql = "SELECT * from books"
    mycursor.execute(sql)

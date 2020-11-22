import string

# pip3 install psycopg2-binary
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname='books',
                        user='admin', host='127.0.0.1',
                        password='admin')

cur = conn.cursor()

def test_one_read():
    cur.execute("SELECT * from books")

import string


from random import randrange
import random

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname='books',
                        user='admin', host='127.0.0.1',
                        password='admin')

cur = conn.cursor()

def test_one_write():
    val = (randrange(10000), ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)))
    cur.execute("INSERT INTO books (code, name) VALUES (%s, \'%s\')" % val)
    conn.commit()

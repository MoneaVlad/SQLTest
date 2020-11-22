import string

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname='books',
                       user='admin', host='127.0.0.1',
                       password='admin')

# ONE TIME SETUP
cur = conn.cursor()
cur.execute("CREATE TABLE books (code INT, name VARCHAR(20))")
conn.commit() # <--- makes sure the change is shown in the database
conn.close()
cur.close()

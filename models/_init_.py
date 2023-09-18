import sqlite3

from logging import getLogger
logger = getLogger("main")

logger.debug("Creating the connections")

# Create a connection to the SQLite database
conn = sqlite3.connect('plantix.db', check_same_thread=False)
cursor = conn.cursor()

def create_tables():

    #  users table 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        password TEXT,
        dob TEXT
        )
    ''')

    

    conn.commit()

# close the connections
def cleanup():
    # cursor.close()
    # conn.close()
    pass


create_tables()

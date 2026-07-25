import sqlite3

DATABASE_NAME = "supermarket.db"

def get_connection():
    """
    Create and return a connection to the SQLite database.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def close_connection(conn):
    """
    Close the database connection.
    """
    if conn:
        conn.close()
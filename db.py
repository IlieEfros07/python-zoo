import sqlite3
from schema import SCHEMA_SQL

DB_NAME = "zoo.db"

def get_db_connection():
    conn = sqlite3.connect('zoo.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.executescript(SCHEMA_SQL)
    conn.commit()
    conn.close()


# Realizati functionalul de baza in baza de date pentru toate tabelele. Operatii crud


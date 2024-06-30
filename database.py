import sqlite3

def get_db():
    db = sqlite3.connect('database.sqlite')
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    with open('schema.sql', 'r') as f:
        db.executescript(f.read())
    db.close()
import sqlite3

class Database:
    def __init__(self):
        self.db = sqlite3.connect("database.db")


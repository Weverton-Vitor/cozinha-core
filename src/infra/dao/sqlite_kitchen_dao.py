import sqlite3
from dao import interfaces


class SQLiteKitchenDAO(interfaces.IKitchenDAO):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def query(self, sql: str, params: tuple = ()):
        if not self.cursor:
            raise Exception("Database connection is not established.")
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

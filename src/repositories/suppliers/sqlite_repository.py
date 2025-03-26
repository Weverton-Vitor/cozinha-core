import sqlite3

import exceptions
from typing import List
from entities import Supplier
from repositories import ISuppliersRepository


class SQLiteSupplierRepository(ISuppliersRepository):
    def __init__(self, db_path: str = 'data/suppliers.db'):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS suppliers (
                        name TEXT PRIMARY KEY,
                        password TEXT
                    )
                ''')
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def create(self, supplier: Supplier) -> None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO suppliers (name, password)
                    VALUES (?, ?)
                ''', (supplier.get_name(), supplier.get_password()))
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def delete(self, name: str) -> None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM suppliers WHERE name = ?', (name,))
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def update(self, name: str, supplier: Supplier) -> None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE suppliers
                    SET password = ?
                    WHERE name = ?
                ''', (supplier.get_password(), name))
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def get(self, name: str) -> Supplier | None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT * FROM suppliers WHERE name = ?', (name,))
                row = cursor.fetchone()
                if row:
                    return Supplier(name=row[0], password=row[1])
                return None
        except Exception:
            raise exceptions.PersistenceException()

    def getAll(self) -> List[Supplier]:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM suppliers')
                rows = cursor.fetchall()
                return [Supplier(name=row[0], password=row[1]) for row in rows]
        except Exception:
            raise exceptions.PersistenceException()

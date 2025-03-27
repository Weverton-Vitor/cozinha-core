

import sqlite3
import exceptions
from typing import Type, TypeVar, List

from dao import interfaces
T = TypeVar("T")

# TODO change SQLiteSupplierDAO class implementing of ISupplierDAO interface

class SQLiteRepository(interfaces.ISupplierDAO):
    def __init__(self, db_path: str, table_name: str, entity_class: Type[T], fields: List[str]):
        self.db_path = db_path
        self.table_name = table_name
        self.entity_class = entity_class
        self.fields = fields
        self._initialize_db()

    def _initialize_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                fields_sql = ", ".join(self.fields)
                cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS {self.table_name} ({fields_sql})
                ''')
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def create(self, entity: T) -> None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                values = [getattr(entity, f"get_{field}")() for field in self.fields[:-1]]
                placeholders = ", ".join(["?"] * len(values))
                cursor.execute(f'''
                    INSERT INTO {self.table_name} ({", ".join(self.fields[:-1])})
                    VALUES ({placeholders})
                ''', values)
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def delete(self, name: str) -> None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f'DELETE FROM {self.table_name} WHERE name = ?', (name,))
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def update(self, name: str, entity: T) -> None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                set_clause = ", ".join([f"{field} = ?" for field in self.fields[1:-1]])
                values = [getattr(entity, f"get_{field}")() for field in self.fields[1:-1]] + [name]
                cursor.execute(f'''
                    UPDATE {self.table_name}
                    SET {set_clause}
                    WHERE name = ?
                ''', values)
                conn.commit()
        except Exception:
            raise exceptions.PersistenceException()

    def get(self, name: str) -> T | None:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f'SELECT * FROM {self.table_name} WHERE name = ?', (name,))
                row = cursor.fetchone()
                if row:
                    return self.entity_class(*row)
                return None
        except Exception:
            raise exceptions.PersistenceException()

    def getAll(self) -> List[T]:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f'SELECT * FROM {self.table_name}')
                rows = cursor.fetchall()
                return [self.entity_class(*row) for row in rows]
        except Exception:
            raise exceptions.PersistenceException()

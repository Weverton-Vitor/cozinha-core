import sqlite3
from infra.dao import interfaces
from infra import exceptions
from business import entities

from typing import List


class SQLiteKitchenDAO(interfaces.IKitchenDAO):
    def __init__(
        self,
        db_path: str,
        table_name: str,
        kitchen_class: entities.Kitchen,
        fields: List[str],
    ):
        self.db_path = db_path
        self.table_name = table_name
        self.kitchen_class = kitchen_class
        self.fields = fields
        self.conn = None
        self.connect()
        self._initialize_db()
        self.close()

    def _initialize_db(self):
        try:
            self.connect()
            fields_sql = ", ".join(self.fields)
            self.query(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({fields_sql})")
            self.conn.commit()
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to connect to database: {e}")

    def query(self, sql: str, params: tuple = ()):
        if not self.cursor:
            raise Exception("Database connection is not established.")
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def create(self, kitchen: entities.Kitchen) -> None:
        try:
            self.connect()
            values = [getattr(kitchen, f"get_{field}")() for field in self.fields[:-1]]
            placeholders = ", ".join(["?"] * len(values))
            self.query(
                f"INSERT INTO {self.table_name} ({', '.join(self.fields[:-1])}) VALUES ({placeholders})",
                values,
            )
            self.conn.commit()
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def delete(self, name: str) -> None:
        try:
            self.connect()
            self.query(f"DELETE FROM {self.table_name} WHERE name = ?", (name,))
            self.conn.commit()
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def update(self, name: str, kitchen: entities.Kitchen) -> None:
        try:
            self.connect()
            set_clause = ", ".join([f"{field} = ?" for field in self.fields[1:-1]])
            values = [
                getattr(kitchen, f"get_{field}")() for field in self.fields[1:-1]
            ] + [name]
            self.query(
                f"UPDATE {self.table_name} SET {set_clause} WHERE name = ?", values
            )
            self.conn.commit()
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def get(self, name: str) -> entities.Kitchen | None:
        try:
            self.connect()
            row = self.query(f"SELECT * FROM {self.table_name} WHERE name = ?", (name,))
            return self.kitchen_class(*row[0]) if row else None
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def getAll(self) -> List[entities.Kitchen]:
        try:
            self.connect()
            rows = self.query(f"SELECT * FROM {self.table_name}")
            return [self.kitchen_class(*row) for row in rows]
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

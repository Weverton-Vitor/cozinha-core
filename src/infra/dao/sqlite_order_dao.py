import sqlite3
from infra.dao import interfaces
from infra import exceptions
from business import entities

from typing import List


class SQLiteOrderDAO(interfaces.IOrderDAO):
    def __init__(
        self,
        db_path: str,
        table_name: str,
        order_class: entities.Order,
        fields: List[str],
    ):
        self.db_path = db_path
        self.table_name = table_name
        self.order_class = order_class
        self.fields = fields
        self.conn = None
        self.cursor = None
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
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to connect to database: {e}")

    def query(self, sql: str, params: tuple = ()):
        if not self.cursor:
            raise Exception("Database connection is not established.")
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def create(self, order: entities.Order) -> None:
        try:
            self.connect()
            values = [getattr(order, f"get_{field}")() for field in self.fields[:-1]]
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

    def delete(self, id: str) -> None:
        try:
            self.connect()
            self.query(f"DELETE FROM {self.table_name} WHERE name = ?", (id,))
            self.conn.commit()
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def update(self, id: str, order: entities.Order) -> None:
        try:
            self.connect()
            set_clause = ", ".join([f"{field} = ?" for field in self.fields[1:-1]])
            values = [
                getattr(order, f"get_{field}")() for field in self.fields[1:-1]
            ] + [id]
            self.query(
                f"UPDATE {self.table_name} SET {set_clause} WHERE name = ?", values
            )
            self.conn.commit()
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def get(self, id: str) -> entities.Order | None:
        try:
            self.connect()
            row = self.query(f"SELECT * FROM {self.table_name} WHERE name = ?", (id,))
            return self.order_class(*row[0]) if row else None
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def getAll(self) -> List[entities.Order]:
        try:
            self.connect()
            rows = self.query(f"SELECT * FROM {self.table_name}")
            return [self.order_class(*row) for row in rows]
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

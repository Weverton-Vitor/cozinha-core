import sqlite3
from dao import interfaces

from typing import List
from infra import exceptions
from business import entities


class SQLiteProductDAO(interfaces.IProductDAO):
    def __init__(
        self,
        db_path: str,
        table_name: str,
        product_class: entities.Product,
        fields: List[str],
    ):
        self.db_path = db_path
        self.table_name = table_name
        self.product_class = product_class
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

    def create(self, product: entities.Product) -> None:
        try:
            self.connect()
            values = [
                product.get_product_id(),
                product.get_name(),
                product.get_stock(),
                product.get_unit()
            ]
            placeholders = ", ".join(["?"] * len(values))
            field_names = "product_id, name, stock, unit"
            self.query(
                f"INSERT INTO {self.table_name} ({field_names}) VALUES ({placeholders})",
                values,
            )
            self.conn.commit()
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to create product: {e}")
        finally:
            self.close()

    def delete(self, product_id: str) -> None:
        try:
            self.connect()
            self.query(f"DELETE FROM {self.table_name} WHERE product_id = ?", (product_id,))
            self.conn.commit()
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to delete product: {e}")
        finally:
            self.close()

    def update(self, product_id: str, product: entities.Product) -> None:
        try:
            self.connect()
            values = [
                product.get_name(),
                product.get_stock(),
                product.get_unit(),
                product_id
            ]
            self.query(
                f"UPDATE {self.table_name} SET name = ?, stock = ?, unit = ? WHERE product_id = ?",
                values
            )
            self.conn.commit()
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to update product: {e}")
        finally:
            self.close()

    def get(self, product_id: str) -> entities.Product | None:
        try:
            self.connect()
            rows = self.query(f"SELECT product_id, name, stock, unit FROM {self.table_name} WHERE product_id = ?", (product_id,))
            if not rows:
                return None
            product_data = rows[0]
            return self.product_class(
                product_id=product_data[0],
                name=product_data[1],
                stock=product_data[2],
                unit=product_data[3]
            )
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to get product: {e}")
        finally:
            self.close()

    def getAll(self) -> List[entities.Product]:
        try:
            self.connect()
            rows = self.query(f"SELECT product_id, name, stock, unit FROM {self.table_name}")
            return [
                self.product_class(
                    product_id=row[0],
                    name=row[1],
                    stock=row[2],
                    unit=row[3]
                ) for row in rows
            ]
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to get all products: {e}")
        finally:
            self.close()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
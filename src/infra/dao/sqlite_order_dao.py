import sqlite3
from infra.dao import interfaces
from infra import exceptions
from business import entities
from typing import List

class SQLiteOrderDAO(interfaces.IOrderDAO):
    def __init__(self, 
        db_path: str, 
        table_name: str, 
        order_class: type, 
        product_class: type
        ):
        self.db_path = db_path
        self.table_name = table_name
        self.order_class = order_class
        self.product_class = product_class
        self.conn = None
        self.cursor = None
        self.connect()
        self._initialize_db()
        self.close()

    def _initialize_db(self):
        try:
            self.connect()
            self.query(f"""
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id_order TEXT,
                    id_product TEXT,
                    name TEXT,
                    stock REAL,
                    unit TEXT,
                    PRIMARY KEY (id_order, id_product)
                )
            """)
            self.conn.commit()
        except Exception as e:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise exceptions.PersistenceException(f"Failed to connect to database: {e}")

    def query(self, query: str):
        if not self.cursor:
            raise Exception("No database connection.")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def _query_with_params(self, sql: str, params: tuple = ()):
        if not self.cursor:
            raise Exception("No database connection.")
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def create(self, order: entities.Order) -> None:
        try:
            self.connect()
            for product in order.get_products():
                self._query_with_params(
                    f"""INSERT INTO {self.table_name} 
                    (id_order, id_product, name, stock, unit) 
                    VALUES (?, ?, ?, ?, ?)""",
                    (
                        order.get_id(),
                        product.get_product_id(),
                        product.get_name(),
                        product.get_stock(),
                        product.get_unit()
                    )
                )
            self.conn.commit()
        except Exception as e:
            raise exceptions.PersistenceException(f"Create error: {e}")
        finally:
            self.close()

    def delete(self, id: str) -> None:
        try:
            self.connect()
            self._query_with_params(f"DELETE FROM {self.table_name} WHERE id_order = ?", (id,))
            self.conn.commit()
        except Exception:
            raise exceptions.PersistenceException("Delete error.")
        finally:
            self.close()

    def update(self, order: entities.Order) -> None:
        try:
            self.delete(order.get_id())
            self.create(order)
        except Exception:
            raise exceptions.PersistenceException()

    def get(self, id: str) -> entities.Order | None:
        try:
            self.connect()
            rows = self._query_with_params(
                f"""SELECT id_product, name, stock, unit 
                FROM {self.table_name} 
                WHERE id_order = ?""", 
                (id,)
            )
            if not rows:
                return None
            products = [
                self.product_class(product_id, name, stock, unit)
                for product_id, name, stock, unit in rows
            ]
            return self.order_class(id, products)
        except Exception:
            raise exceptions.PersistenceException()
        finally:
            self.close()

    def getAll(self) -> List[entities.Order]:
        try:
            self.connect()
            rows = self.query(f"SELECT * FROM {self.table_name}")
            orders = {}
            for id_order, id_product, name, stock, unit in rows:
                if id_order not in orders:
                    orders[id_order] = []
                orders[id_order].append(
                    self.product_class(id_product, name, stock, unit)
                )
            return [
                self.order_class(order_id, products)
                for order_id, products in orders.items()
            ]
        except Exception:
            raise exceptions.PersistenceException("GetAll error.")
        finally:
            self.close()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

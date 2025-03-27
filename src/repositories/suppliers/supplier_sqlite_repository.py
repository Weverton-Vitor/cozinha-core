from repositories import SQLiteRepository
from entities import Supplier

class SQLiteSupplierRepository(SQLiteRepository[Supplier]):
    def __init__(self, db_path: str = "data/suppliers.db"):
        fields = ["name TEXT PRIMARY KEY", "password TEXT"]
        super().__init__(db_path, "suppliers", Supplier, fields)
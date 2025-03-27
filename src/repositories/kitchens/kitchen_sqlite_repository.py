from repositories import SQLiteRepository
from entities import Kitchen

class SQLiteKitchenRepository(SQLiteRepository[Kitchen]):
    def __init__(self, db_path: str = 'data/kitchens.db'):
        fields = [
            "name TEXT PRIMARY KEY", "user_name TEXT", "password TEXT",
            "address TEXT", "phone_number TEXT", "email TEXT",
            "created_at TEXT", "status INTEGER"
        ]
        super().__init__(db_path, "kitchens", Kitchen, fields)

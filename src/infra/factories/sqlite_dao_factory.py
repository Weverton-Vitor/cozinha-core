from business.decorators import singleton
from business.entities.kitchen import Kitchen
from business.entities.supplier import Supplier
from infra import dao, factories

@singleton
class SQLIteDAOFactory(factories.IDAOFactory):
    def get_supplier_dao(self) -> dao.ISupplierDAO:
        return dao.SQLiteSupplierDAO("./data/database.db", "suppliers", Supplier, ["username", "password"])

    def get_kitchen_dao(self) -> dao.IKitchenDAO:
        return dao.SQLiteKitchenDAO("./data/database.db", "kitchens", Kitchen, ["name", "user_name", "password", "address", "phone_number", "email", "created_at"])
    
    def get_product_dao(self) -> dao.interfaces.IProductDAO:
        return dao.SQLiteProductDAO()

    def get_order_dao(self) -> dao.interfaces.IOrderDAO:
        return dao.SQLiteOrderDAO()

from infra import dao
import factories


class SQLIteDAOFactory(factories.interfaces.IDAOFactory):
    def get_supplier_dao(self) -> dao.interfaces.ISupplierDAO:
        return dao.SQLiteSupplierDAO()

    def get_kitchen_dao(self) -> dao.interfaces.IKitchenDAO:
        return dao.SQLiteKitchenDAO()

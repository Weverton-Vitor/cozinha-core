from infra import dao
import factories


class ArrayDAOFactory(factories.interfaces.IDAOFactory):
    def get_supplier_dao(self) -> dao.interfaces.ISupplierDAO:
        return dao.ArraySupplierDAO()

    def get_kitchen_dao(self) -> dao.interfaces.IKitchenDAO:
        return dao.ArrayKitchenDAO()

from infra import dao
import factories
from business.decorators import singleton

@singleton
class ArrayDAOFactory(factories.interfaces.IDAOFactory):
    def get_supplier_dao(self) -> dao.interfaces.ISupplierDAO:
        return dao.ArraySupplierDAO()

    def get_kitchen_dao(self) -> dao.interfaces.IKitchenDAO:
        return dao.ArrayKitchenDAO()
    
    def get_order_dao(self) -> dao.interfaces.IOrderDAO:
        return dao.ArrayOrderDAO()

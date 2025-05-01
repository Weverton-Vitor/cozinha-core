from infra import dao, factories


from business.decorators import singleton

@singleton
class ArrayDAOFactory(factories.IDAOFactory):
    def get_supplier_dao(self) -> dao.interfaces.ISupplierDAO:
        return dao.ArraySupplierDAO()

    def get_kitchen_dao(self) -> dao.interfaces.IKitchenDAO:
        return dao.ArrayKitchenDAO()

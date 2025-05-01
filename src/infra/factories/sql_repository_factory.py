from infra import repositories, factories
from infra.dao import ISupplierDAO, IProductDAO, IKitchenDAO, IOrderDAO


class SQLiteRepositoryFactory(factories.IRepositoryFactory):
    def get_supplier_repository(self, supplier_dao: ISupplierDAO) -> repositories.ISupplierRepository:
        return repositories.SQLiteSupplierRepository(supplier_dao)

    def get_product_repository(self, product_dao: IProductDAO) -> repositories.IProductRepository:
        return repositories.SQLiteProductRepository(product_dao)

    def get_order_repository(self, order_dao: IOrderDAO) -> repositories.interfaces.IOrderRepository:
        return repositories.SQLiteOrderRepository(order_dao)
    
    def get_kitchen_repository(self, kitchen_dao: IKitchenDAO) -> repositories.IKitchenRepository:
        return repositories.SQLiteKitchenRepository(kitchen_dao)

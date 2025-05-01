from infra import repositories, factories
from infra.dao import ISupplierDAO, IKitchenDAO, IOrderDAO, IProductDAO


class InMemoryRepositoryFactory(factories.IRepositoryFactory):
    def get_supplier_repository(self, supplier_dao: ISupplierDAO) -> repositories.ISupplierRepository:
        return repositories.InMemorySuppliersRepository(supplier_dao)

    def get_kitchen_repository(self, kitchen_dao: IKitchenDAO) -> repositories.IKitchenRepository:
        return repositories.InMemoryKitchenRepository(kitchen_dao)
    
    def get_product_repository(self, product_dao: IProductDAO) -> repositories.interfaces.IProductRepository:
        return repositories.InMemoryProductRepository(product_dao)

    def get_order_repository(self, order_dao: IOrderDAO) -> repositories.interfaces.IOrderRepository:
        return repositories.InMemoryOrderRepository(order_dao)
    

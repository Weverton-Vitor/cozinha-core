import factories.interfaces
from infra import repositories
import factories


class InMemoryRepositoryFactory(factories.interfaces.IRepositoryFactory):
    def get_supplier_repository(self) -> repositories.interfaces.ISupplierRepository:
        return repositories.InMemorySuppliersRepository()

    def get_kitchen_repository(self) -> repositories.interfaces.IKitchenRepository:
        return repositories.InMemoryKitchenRepository()
    
    def get_Product_repository(self) -> repositories.interfaces.IProductRepository:
        return repositories.InMemoryProductRepository()

    def get_order_repository(self) -> repositories.interfaces.IOrderRepository:
        return repositories.InMemoryOrderRepository()

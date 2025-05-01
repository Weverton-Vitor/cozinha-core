from abc import ABC, abstractmethod
from infra import repositories
from infra.dao import ISupplierDAO, IKitchenDAO, IOrderDAO, IProductDAO


class IRepositoryFactory(ABC):
    @abstractmethod
    def get_supplier_repository(self, supplier_dao: ISupplierDAO) -> repositories.interfaces.ISupplierRepository:
        pass

    @abstractmethod
    def get_kitchen_repository(self, kitchen_dao: IKitchenDAO) -> repositories.interfaces.IKitchenRepository:
        pass

    @abstractmethod
    def get_product_repository(self, product_dao: IProductDAO) -> repositories.interfaces.IOrderRepository:
        pass
    
    @abstractmethod
    def get_order_repository(self, order_dao: IOrderDAO) -> repositories.interfaces.IOrderRepository:
        pass


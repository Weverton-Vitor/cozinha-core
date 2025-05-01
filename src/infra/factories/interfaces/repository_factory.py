from abc import ABC, abstractmethod
from infra import repositories


class IRepositoryFactory(ABC):
    @abstractmethod
    def get_supplier_repository(self, supplier_dao) -> repositories.interfaces.ISupplierRepository:
        pass

    @abstractmethod
    def get_kitchen_repository(self, kithcen_dao) -> repositories.interfaces.IKitchenRepository:
        pass

    @abstractmethod
    def get_order_repository(self) -> repositories.interfaces.IOrderRepository:
        pass

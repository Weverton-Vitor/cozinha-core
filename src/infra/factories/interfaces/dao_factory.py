from abc import ABC, abstractmethod
from infra import dao


class IDAOFactory(ABC):
    @abstractmethod
    def get_supplier_dao(self) -> dao.interfaces.ISupplierDAO:
        pass

    @abstractmethod
    def get_kitchen_dao(self) -> dao.interfaces.IKitchenDAO:
        pass

    @abstractmethod
    def get_order_dao(self) -> dao.interfaces.IOrderDAO:
        pass

from abc import ABC, abstractmethod

from business import entities

class ISupplierRepository(ABC):
    @abstractmethod
    def create(self, supplier: entities.Supplier) -> None:
        pass

    @abstractmethod
    def delete(self, username: str) -> None:
        pass

    @abstractmethod
    def update(self, username: str, supplier: entities.Supplier) -> None:
        pass

    @abstractmethod
    def get(self, username: str) -> entities.Supplier | None:
        pass

    @abstractmethod
    def getAll(self) -> list[entities.Supplier]:
        pass
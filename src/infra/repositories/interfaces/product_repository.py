from abc import ABC, abstractmethod

from business import entities

class IProductRepository(ABC):
    @abstractmethod
    def create(self, product: entities.Product) -> None:
        pass

    @abstractmethod
    def delete(self, product_id: str) -> None:
        pass

    @abstractmethod
    def update(self, product_id: str, product: entities.Product) -> None:
        pass

    @abstractmethod
    def get(self, product_id: str) -> entities.Product | None:
        pass

    @abstractmethod
    def getAll(self) -> list[entities.Product]:
        pass
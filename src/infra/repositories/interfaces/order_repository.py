from abc import ABC, abstractmethod

from business import entities

class IOrderRepository(ABC):
    @abstractmethod
    def create(self, order: entities.Order) -> None:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass

    @abstractmethod
    def update(self, id: str, order: entities.Order) -> None:
        pass

    @abstractmethod
    def get(self, alias: str) -> entities.Order | None:
        pass

    @abstractmethod
    def getAll(self) -> list[entities.Order]:
        pass
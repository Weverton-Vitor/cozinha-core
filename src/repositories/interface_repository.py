from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

# Tipo genérico para a entidade
T = TypeVar("T")  

class InterfaceRepository(ABC, Generic[T]):
    @abstractmethod
    def create(self, item: T) -> None:
        pass

    @abstractmethod
    def delete(self, identifier: str) -> None:
        pass

    @abstractmethod
    def update(self, identifier: str, item: T) -> None:
        pass

    @abstractmethod
    def get(self, identifier: str) -> T | None:
        pass

    @abstractmethod
    def getAll(self) -> List[T]:
        pass

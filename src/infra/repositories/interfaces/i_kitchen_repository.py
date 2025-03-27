from abc import ABC, abstractmethod

import entities


class IKitchenRepository(ABC):
    @abstractmethod
    def create(self, kitchen: entities.Kitchen) -> None:
        pass

    @abstractmethod
    def delete(self, username: str) -> None:
        pass

    @abstractmethod
    def update(self, username: str, kitchen: entities.Kitchen) -> None:
        pass

    @abstractmethod
    def get(self, username: str) -> entities.Kitchen | None:
        pass

    @abstractmethod
    def getAll(self) -> list[entities.Kitchen]:
        pass
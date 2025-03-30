from abc import ABC, abstractmethod
from business import entities


class InterfaceKitchenDAO(ABC):
    def execute(self):
        self.connect()
        self.query()
        self.close()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, query: str):
        pass

    @abstractmethod
    def create(self, kitchen: entities.Kitchen):
        pass

    @abstractmethod
    def delete(self, name: str):
        pass

    @abstractmethod
    def update(self, kitchen: entities.Kitchen):
        pass

    @abstractmethod
    def get(self, name: str):
        pass

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def close(self):
        pass

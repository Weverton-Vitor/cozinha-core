from abc import ABC, abstractmethod

from business import entities


class ISupplierDAO(ABC):
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
    def create(self, supplier: entities.Supplier):
        pass

    @abstractmethod
    def delete(self, name: str):
        pass

    @abstractmethod
    def update(self, supplier: entities.Supplier):
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

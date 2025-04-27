from abc import ABC, abstractmethod

from business import entities


class IProductDAO(ABC):
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
    def create(self, product: entities.Product):
        pass

    @abstractmethod
    def delete(self, product_id: str):
        pass

    @abstractmethod
    def update(self, product: entities.Product):
        pass

    @abstractmethod
    def get(self, product_id: str):
        pass

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def close(self):
        pass

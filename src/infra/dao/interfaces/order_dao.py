from abc import ABC, abstractmethod
from business import entities


class IOrderDAO(ABC):
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
    def create(self, order: entities.Order):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass

    @abstractmethod
    def update(self, order: entities.Order):
        pass

    @abstractmethod
    def get(self, id: str):
        pass

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def close(self):
        pass

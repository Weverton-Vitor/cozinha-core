from abc import ABC, abstractmethod


class InterfaceKitchenDAO(ABC):
    def execute(self):
        self.connect()
        self.query()
        self.close()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self):
        pass

    @abstractmethod
    def close(self):
        pass

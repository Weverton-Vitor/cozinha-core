from abc import ABC, abstractmethod

class Command(ABC):
    __id: str

    def __init__(self, id: str):
        self.__id = id

    @abstractmethod
    def execute(self):
        pass


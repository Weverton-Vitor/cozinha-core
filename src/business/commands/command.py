from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def __init__(id: str):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

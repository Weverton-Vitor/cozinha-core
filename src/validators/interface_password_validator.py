from abc import ABC, abstractmethod

class IPasswordValidator(ABC):
    @abstractmethod
    def validate(password: str) -> bool:
        pass
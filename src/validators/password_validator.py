from abc import ABC, abstractmethod


class IPasswordValidator(ABC):
    @abstractmethod
    def validate(self, password: str) -> bool:
        pass

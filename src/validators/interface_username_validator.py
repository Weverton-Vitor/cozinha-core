from abc import ABC, abstractmethod

class IUsernameValidator(ABC):
    @abstractmethod
    def validate(username: str) -> bool:
        pass

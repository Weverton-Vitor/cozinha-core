from abc import ABC, abstractmethod


class IUsernameValidator(ABC):
    @abstractmethod
    def validate(self, username: str) -> bool:
        pass

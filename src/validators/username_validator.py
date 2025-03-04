from abc import ABC, abstractmethod
import exceptions

class IUsernameValidator(ABC):
    @abstractmethod
    def validate(username: str) -> bool:
        if not username.strip():
            raise exceptions.InvalidUsernameException("O nome de usuário não pode estar vazio.")
        return True

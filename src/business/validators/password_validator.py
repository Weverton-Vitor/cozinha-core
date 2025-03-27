import re
import exceptions
from abc import ABC, abstractmethod


class IPasswordValidator(ABC):
    @abstractmethod
    def validate(password: str) -> bool:
        pass


class PasswordValidator(IPasswordValidator):
    min_password_length = 8
    max_password_length = 128

    def validate(self, password: str) -> bool:
        if not (self.min_password_length <= len(password) <= self.max_password_length):
            raise exceptions.InvalidPasswordException(
                f"A senha deve ter entre {self.min_password_length} e {self.max_password_length} caracteres.")

        if not re.search(r'[A-Z]', password):
            raise exceptions.InvalidPasswordException(
                "A senha deve conter pelo menos uma letra maiúscula.")

        if not re.search(r'[a-z]', password):
            raise exceptions.InvalidPasswordException(
                "A senha deve conter pelo menos uma letra minúscula.")

        if not re.search(r'\d', password):
            raise exceptions.InvalidPasswordException(
                "A senha deve conter pelo menos um número.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise exceptions.InvalidPasswordException(
                "A senha deve conter pelo menos um caractere especial.")

        return True

import re
import exceptions
from validators.interface_password_validator import IPasswordValidator

class PasswordValidator(IPasswordValidator):
    
    def validate(self, password: str) -> bool:
        if not (8 <= len(password) <= 64):
            raise exceptions.InvalidPasswordException("A senha deve ter entre 8 e 64 caracteres.")

        if not re.search(r'[A-Z]', password):
            raise exceptions.InvalidPasswordException("A senha deve conter pelo menos uma letra maiúscula.")

        if not re.search(r'[a-z]', password):
            raise exceptions.InvalidPasswordException("A senha deve conter pelo menos uma letra minúscula.")

        if not re.search(r'\d', password):
            raise exceptions.InvalidPasswordException("A senha deve conter pelo menos um número.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise exceptions.InvalidPasswordException("A senha deve conter pelo menos um caractere especial.")

        return True

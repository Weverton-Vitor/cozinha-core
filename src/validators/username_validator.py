import exceptions
from validators.interface_username_validator import IUsernameValidator

class UsernameValidator(IUsernameValidator):
    max_username_length = 12
    def validate(self, username: str) -> bool:
        if not username.strip():
            raise exceptions.InvalidUsernameException("O nome de usuário não pode estar vazio.")
        if len(username) > self.max_username_length:
            raise exceptions.InvalidUsernameException(f"O nome de usuário não pode ter mais que {self.max_username_length} caracteres.")

        if any(char.isdigit() for char in username):
            raise exceptions.InvalidUsernameException("O nome de usuário não pode conter números.")
        return True

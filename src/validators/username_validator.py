import exceptions
from validators.interface_username_validator import IUsernameValidator

class UsernameValidator(IUsernameValidator):
    def validate(self, username: str) -> bool:
        if not username.strip():
            raise exceptions.InvalidUsernameException("O nome de usuário não pode estar vazio.")
        return True

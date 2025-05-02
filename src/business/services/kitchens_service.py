from business import validators
from business.decorators import singleton


class KitchensService:
    __username_validator: validators.IUsernameValidator
    __password_validator: validators.IPasswordValidator

    def __init__(self, username_validator: validators.IUsernameValidator, password_validator: validators.IPasswordValidator):
        self.__username_validator = username_validator
        self.__password_validator = password_validator

    def validate_credentials(self, name: str, password: str) -> bool:
        return self.__username_validator.validate(username=name) and self.__password_validator.validate(password=password)

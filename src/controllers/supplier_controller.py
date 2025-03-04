import entities
import services
import exceptions
import validators


class SupplierController:
    __suppliers: list[entities.Supplier]
    __service: services.SuppliersService

    def __init__(self, service: services.SuppliersService=None):
        self.__suppliers = []

        if service is None:
            self.__service = services.SuppliersService(
                username_validator=validators.UsernameValidator(),
                password_validator=validators.PasswordValidator(),
            )
        else:
            self.__service = service

    def add_supplier(self, name: str, password: str):
        try:
            if self.__service.validate_credentials(name, password):
                sup = entities.Supplier(name, password)
                self.__suppliers.append(sup)

        except exceptions.InvalidUsernameException as e:
            print(f"Erro de nome de usuário: {e}")
        except exceptions.InvalidPasswordException as e:
            print(f"Erro de senha: {e}")

    def get_suppliers(self):
        return self.__suppliers

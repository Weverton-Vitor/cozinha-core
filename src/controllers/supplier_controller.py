import entities
import repositories.in_memory_repository
import services
import exceptions
import validators
import repositories


class SupplierController:
    __service: services.SuppliersService
    __in_memory_repository: repositories.in_memory_repository.InMemoryRepository

    def __init__(self, service: services.SuppliersService=None, 
                 in_memory_repository: repositories.ISuppliersRepository=None):

        if service is None:
            self.__service = services.SuppliersService(
                username_validator=validators.UsernameValidator(),
                password_validator=validators.PasswordValidator(),
            )
        else:
            self.__service = service

        if in_memory_repository is None:
            self.__in_memory_repository = repositories.in_memory_repository.InMemoryRepository()
        else:
            self.__in_memory_repository = in_memory_repository


    def add_supplier(self, name: str, password: str, option: bool):
        try:
            if self.__service.validate_credentials(name, password):
                sup = entities.Supplier(name, password)
                if option == 1:
                    self.__in_memory_repository.create(sup)

        except exceptions.InvalidUsernameException as e:
            print(f"Erro de nome de usuário: {e}")
        except exceptions.InvalidPasswordException as e:
            print(f"Erro de senha: {e}")

    def get_suppliers(self, option):
        if option == 1:
            return self.__in_memory_repository.getAll()

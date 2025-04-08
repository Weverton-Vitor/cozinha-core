from business import services
from business import validators
from business import entities
from infra import repositories
from infra import exceptions


class SupplierController:
    __service: services.SuppliersService
    __repository: repositories.IRepository

    def __init__(
        self,
        service: services.SuppliersService = None,
        repository: repositories.IRepository = None,
    ):
        if service is None:
            self.__service = services.SuppliersService(
                validators.UsernameValidator(),
                validators.PasswordValidator(),
            )
        else:
            self.__service = service

        if repository is None:
            self.__repository = repositories.InMemorySuppliersRepository()
        else:
            self.__repository = repository

    def add_supplier(self, name: str, password: str):
        try:
            if self.__service.validate_credentials(name, password):
                sup = entities.Supplier(name, password)
                self.__repository.create(sup)
        except exceptions.InvalidUsernameException as e:
            print(f"Erro de nome de usuário: {e}")
        except exceptions.InvalidPasswordException as e:
            print(f"Erro de senha: {e}")
        except exceptions.PersistenceException as e:
            print(f"Erro de persistência: {e}")

    def update_supplier(self, identifier: str, supplier: entities.Supplier):
        try:
            self.__repository.update(identifier=identifier, item=supplier)
        except exceptions.PersistenceException as e:
            print(f"Erro de persistência: {e}")

    def get_supplier(self, identifier: str) -> entities.Supplier:
        try:
            return self.__repository.get(identifier=identifier)
        except exceptions.LookupException as e:
            print(f"Erro de persistência: {e}")

    def delete_supplier(self, identifier: str) -> entities.Supplier:
        try:
            return self.__repository.delete(identifier=identifier)
        except exceptions.DeleteException as e:
            print(f"Erro de persistência: {e}")

    def get_suppliers(self):
        try:
            return self.__repository.getAll()
        except exceptions.PersistenceException as e:
            print(f"Erro de persistência: {e}")

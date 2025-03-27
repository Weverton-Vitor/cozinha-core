import entities
import exceptions.DeleteException
import exceptions.LookupException
import services
import exceptions
import repositories
import validators


class KitchenController:
    __service: services.KitchensService
    __repository: repositories.InterfaceRepository

    def __init__(
        self,
        service: services.KitchensService = None,
        repository: repositories.InterfaceRepository = None,
    ):
        if service is None:
            self.__service = services.KitchensService(
                validators.UsernameValidator(),
                validators.PasswordValidator(),
            )
        else:
            self.__service = service

        if repository is None:
            self.__repository = repositories.InMemoryKitchenRepository()
        else:
            self.__repository = repository

    def add_kitchen(
        self,
        name: str,
        password: str,
        user_name: str,
        address: str,
        phone_number: str,
        email: str,
    ):
        try:
            if self.__service.validate_credentials(name, password):
                kitchen = entities.Kitchen(
                    name, password, user_name, address, phone_number, email
                )
                self.__repository.create(kitchen)
        except exceptions.InvalidUsernameException as e:
            print(f"Erro de nome de usuário: {e}")
        except exceptions.InvalidPasswordException as e:
            print(f"Erro de senha: {e}")
        except exceptions.PersistenceException as e:
            print(f"Erro de persistência: {e}")

    def update_kitchen(self, identifier: str, kitchen: entities.kitchen):
        try:
            self.__repository.update(identifier=identifier, item=kitchen)
        except exceptions.PersistenceException as e:
            print(f"Erro de persistência: {e}")

    def get_kitchen(self, identifier: str) -> entities.Kitchen:
        try:
            return self.__repository.get(identifier=identifier)
        except exceptions.LookupException as e:
            print(f"Erro de persistência: {e}")

    def delete_kitchen(self, identifier: str) -> entities.kitchen:
        try:
            return self.__repository.delete(identifier=identifier)
        except exceptions.DeleteException as e:
            print(f"Erro de persistência: {e}")

    def get_kitchens(self):
        try:
            return self.__repository.getAll()
        except exceptions.PersistenceException as e:
            print(f"Erro de persistência: {e}")

import business
import infra

from business import services, validators, entities
from infra import repositories


class KitchenController:
    __service: services.KitchensService
    __repository: repositories.IKitchenRepository

    def __init__(
        self,
        service: services.KitchensService = None,
        repository: repositories.IKitchenRepository = None,
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
                return True, kitchen
        except business.exceptions.InvalidUsernameException as e:
            return False, f"Erro de nome de usuário: {e}"
        except business.exceptions.InvalidPasswordException as e:
            return False, f"Erro de senha: {e}"
        except infra.exceptions.PersistenceException as e:
            return False, f"Erro de persistência: {e}"

    def update_kitchen(self, identifier: str, kitchen_dict: dict):
        kitchen = entities.Kitchen(**kitchen_dict)

        try:
            self.__repository.update(identifier=identifier, item=kitchen)
        except infra.exceptions.PersistenceException as e:
            return f"Erro de persistência: {e}"

    def get_kitchen(self, identifier: str) -> entities.Kitchen:
        try:
            return self.__repository.get(identifier=identifier)
        except infra.exceptions.LookupException as e:
            return f"Erro de persistência: {e}"

    def delete_kitchen(self, identifier: str) -> entities.Kitchen:
        try:
            return self.__repository.delete(identifier=identifier)
        except infra.exceptions.DeleteException as e:
            return f"Erro de persistência: {e}"

    def get_kitchens(self):
        try:
            return self.__repository.getAll()
        except infra.exceptions.PersistenceException as e:
            return f"Erro de persistência: {e}"

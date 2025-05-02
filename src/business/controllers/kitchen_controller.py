import business
import infra
from infra.exceptions import LookupException, DeleteException, PersistenceException

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
        self.__service = service
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
        except PersistenceException as e:
            return False, f"Erro de persistência: {e}"

    def update_kitchen(self, identifier: str, kitchen_dict: dict):
        kitchen = entities.Kitchen(**kitchen_dict)

        try:
            self.__repository.update(identifier, kitchen)
            return True, kitchen
        except PersistenceException as e:
            return False, f"Erro de persistência: {e}"

    def get_kitchen(self, identifier: str) -> tuple[bool, entities.Kitchen | str]:
        try:
            return True, self.__repository.get(identifier)
        except LookupException as e:
            return False, f"Erro de persistência: {e}"

    def delete_kitchen(self, identifier: str) -> tuple[bool, entities.Kitchen | str]:
        try:
            return True, self.__repository.delete(identifier)
        except DeleteException as e:
            return False, f"Erro de persistência: {e}"

    def get_kitchens(self):
        try:
            return True, self.__repository.getAll()
        except PersistenceException as e:
            return False, f"Erro de persistência: {e}"

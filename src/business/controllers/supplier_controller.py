from business import services
from business import entities
from infra import repositories
from infra.exceptions import PersistenceException, LookupException, DeleteException
from business.exceptions import InvalidPasswordException, InvalidUsernameException
import logger


class SupplierController:
    __service: services.SuppliersService
    __repository: repositories.ISupplierRepository
    __logger: logger.LoggerAdapter

    def __init__(
        self,
        service: services.SuppliersService,
        repository: repositories.ISupplierRepository,
        logger: logger.LoggerAdapter
    ):
        self.__service = service
        self.__repository = repository
        self.__logger = logger

    def add_supplier(self, name: str, password: str):
        try:
            if self.__service.validate_credentials(name, password):
                sup = entities.Supplier(name, password)
                self.__repository.create(sup)
                self.__logger.log_info(f"{sup} created")
                return True, sup
        except InvalidUsernameException as e:
            return False, f"Erro de nome de usuário: {e}"
        except InvalidPasswordException as e:
            return False, f"Erro de senha: {e}"
        except PersistenceException as e:
            return False, f"Erro de persistência: {e}"

    def update_supplier(self, username: str, supplier_dict: dict):
        supplier = entities.Supplier(**supplier_dict)
        try:
            self.__repository.update(username=username, supplier=supplier)
            return True, supplier
        except PersistenceException as e:
            return False, f"Erro de persistência: {e}"

    def get_supplier(self, username: str) -> tuple[bool, entities.Supplier | str]:
        try:
            return True, self.__repository.get(username=username)
        except LookupException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")
            return False, f"Erro de persistência: {e}"

    def delete_supplier(self, username: str) -> tuple[bool, entities.Supplier | str]:
        try:
            return True, self.__repository.delete(username=username)
        except DeleteException as e:
            return False, f"Erro de persistência: {e}"

    def get_suppliers(self):
        try:
            return True, self.__repository.getAll()
        except PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")
            return False, f"Erro de persistência: {e}"

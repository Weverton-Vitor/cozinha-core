from business import services
from business import entities
from infra import repositories
from infra import exceptions
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
        except exceptions.InvalidUsernameException as e:
            self.__logger.log_error(f"Erro de nome de usuário: {e}")
        except exceptions.InvalidPasswordException as e:
            self.__logger.log_error(f"Erro de senha: {e}")
        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

    def update_supplier(self, identifier: str, supplier: entities.Supplier):
        try:
            self.__repository.update(identifier=identifier, item=supplier)
        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

    def get_supplier(self, identifier: str) -> entities.Supplier:
        try:
            return self.__repository.get(identifier=identifier)
        except exceptions.LookupException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

    def delete_supplier(self, identifier: str) -> entities.Supplier:
        try:
            return self.__repository.delete(identifier=identifier)
        except exceptions.DeleteException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

    def get_suppliers(self):
        try:
            return self.__repository.getAll()
        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

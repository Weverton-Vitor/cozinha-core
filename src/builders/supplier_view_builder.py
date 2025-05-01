from business.controllers import SupplierController
from business.services import SuppliersService
from business.validators import IPasswordValidator, IUsernameValidator
from logger.python_logging_adapter import PythonLoggerAdapter
from logger.logger_adapter import LoggerAdapter

from business.validators.password_validator import PasswordValidator
from business.validators.username_validator import UsernameValidator
from infra.dao import ISupplierDAO
from infra.factories import SQLIteDAOFactory
from infra.factories.sql_repository_factory import SQLiteRepositoryFactory
from infra.repositories import ISupplierRepository

from builders.view_builder import IViewBuilder
from views import SupplierView


class SupplierViewBuilder(IViewBuilder):
    __dao: ISupplierDAO = None

    __password_validator: IPasswordValidator = None
    __username_validator: IUsernameValidator = None

    __repository: ISupplierRepository = None
    __service: SuppliersService = None
    __controller: SupplierController = None
    __logger: LoggerAdapter = None

    __view: SupplierView = None

    def reset(self):
        self.__dao = None
        self.__password_validator = None
        self.__username_validator = None
        self.__repository = None
        self.__service = None
        self.__controller = None
        self.__view = None

    def build_controller(self):
        self.__logger = PythonLoggerAdapter()
        self.__controller = SupplierController(
            self.__service, self.__repository, self.__logger)

    def build_DAO(self):
        self.__dao = SQLIteDAOFactory().get_supplier_dao()

    def build_repository(self):
        self.__repository = SQLiteRepositoryFactory().get_supplier_repository(self.__dao)

    def build_service(self):
        self.__service = SuppliersService(
            self.__username_validator, self.__password_validator)

    def build_validators(self):
        self.__password_validator = UsernameValidator()
        self.__username_validator = PasswordValidator()

    def build_view(self):
        print("construir")
        self.__view = SupplierView(self.__controller)

    def get_product(self):
        return self.__view

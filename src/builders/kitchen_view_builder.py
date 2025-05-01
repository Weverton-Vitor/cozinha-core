from business.controllers import KitchenController
from business.services import KitchensService
from business.validators import IPasswordValidator, IUsernameValidator

from business.validators.password_validator import PasswordValidator
from business.validators.username_validator import UsernameValidator
from infra.dao import IKitchenDAO
from infra.factories import SQLIteDAOFactory
from infra.factories.sql_repository_factory import SQLiteRepositoryFactory
from infra.repositories import IKitchenRepository

from builders.view_builder import IViewBuilder
from views import KitchenView


class KitchenViewBuilder(IViewBuilder):
    __dao: IKitchenDAO = None

    __password_validator: IPasswordValidator = None
    __username_validator: IUsernameValidator = None

    __repository: IKitchenRepository = None
    __service: KitchensService = None
    __controller: KitchenController = None

    __view: KitchenView = None

    def reset(self):
        self.__dao = None
        self.__password_validator = None
        self.__username_validator = None
        self.__repository = None
        self.__service = None
        self.__controller = None
        self.__view = None

    def build_controller(self):
        self.__controller = KitchenController(
            self.__service, self.__repository)

    def build_DAO(self):
        self.__dao = SQLIteDAOFactory().get_kitchen_dao()

    def build_repository(self):
        self.__repository = SQLiteRepositoryFactory().get_kitchen_repository(self.__dao)

    def build_service(self):
        self.__service = KitchensService(
            self.__username_validator, self.__password_validator)

    def build_validators(self):
        self.__password_validator = UsernameValidator()
        self.__username_validator = PasswordValidator()

    def build_view(self):
        self.__view = KitchenView(self.__controller)

    def get_product(self):
        return self.__view

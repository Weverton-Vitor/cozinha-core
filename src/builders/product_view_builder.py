from business.controllers import ProductController
from business.observers.event_manager import EventManager
from logger import LoggerAdapter, PythonLoggerAdapter
# from business.services import ProductsService

from infra.dao import IProductDAO
from infra.factories import SQLIteDAOFactory
from infra.factories.sql_repository_factory import SQLiteRepositoryFactory
from infra.repositories import IProductRepository

from builders.view_builder import IViewBuilder
from views import ProductView


class ProductViewBuilder(IViewBuilder):
    __dao: IProductDAO = None

    __repository: IProductRepository = None
    # __service: ProductsService = None
    __controller: ProductController = None
    __logger: LoggerAdapter = None
    __eventmanager: EventManager = None

    __view: ProductView = None

    def reset(self):
        self.__dao = None
        self.__repository = None
        self.__eventmanager = None
        self.__controller = None
        self.__view = None

    def build_controller(self):
        self.__logger = PythonLoggerAdapter()
        self.__eventmanager = EventManager()
        self.__controller = ProductController(
            self.__repository, self.__logger, self.__eventmanager)

    def build_DAO(self):
        self.__dao = SQLIteDAOFactory().get_kitchen_dao()

    def build_repository(self):
        self.__repository = SQLiteRepositoryFactory().get_kitchen_repository(self.__dao)

    def build_service(self):
        # self.__service = ProductsService(
        #     self.__username_validator, self.__password_validator)
        pass

    def build_validators(self):
        pass

    def build_view(self):
        self.__view = ProductView(self.__controller)

    def get_product(self):
        return self.__view

from business.controllers import OrderController
# from business.services import OrderService
from logger.python_logging_adapter import PythonLoggerAdapter
from logger.logger_adapter import LoggerAdapter

from infra.dao import IOrderDAO
from infra.factories import SQLIteDAOFactory
from infra.factories.sql_repository_factory import SQLiteRepositoryFactory
from infra.repositories import IOrderRepository

from builders.view_builder import IViewBuilder
from views import OrderView


class OrderViewBuilder(IViewBuilder):
    __dao: IOrderDAO = None

    __repository: IOrderRepository = None
    # __service: OrdersService = None
    __controller: OrderController = None
    __logger: LoggerAdapter = None

    __view: OrderView = None

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
        self.__controller = OrderController(
            self.__repository, self.__logger)

    def build_DAO(self):
        self.__dao = SQLIteDAOFactory().get_supplier_dao()

    def build_repository(self):
        self.__repository = SQLiteRepositoryFactory().get_supplier_repository(self.__dao)

    def build_service(self):
        # self.__service = OrdersService(
        #     self.__username_validator, self.__password_validator)
        pass

    def build_validators(self):
        pass

    def build_view(self):
        self.__view = OrderView(self.__controller)

    def get_product(self):
        return self.__view

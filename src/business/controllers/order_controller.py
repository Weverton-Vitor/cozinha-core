from business import entities
from infra import repositories
from business import commands
from infra.exceptions.persistence_exception import PersistenceException


class OrderController:
    __repository: repositories.IOrderRepository
    __command: commands.Command

    def __init__(
        self,
        repository: repositories.IOrderRepository = None,
        command: commands.Command = None
    ):
        if repository is None:
            self.__repository = repositories.InMemoryOrderRepository()
        else:
            self.__repository = repository
        self.__command = command

    def set_command(self, command: commands.Command):
        self.__command = command

    def execute_command(self):
        self.__command.execute(self.__repository)

    def get_order(self, id):
        try:
            return True, self.__repository.get(id)
        except LookupError as e:
            return False, f"{e}"

    def create_order(self, id, products: list[dict]):
        try:
            order = entities.Order(
                id, [entities.Product(**p) for p in products])
            self.__repository.create(order)
            return True, order

        except PersistenceException as e:
            return False, f"Erros de persistência: {e}"

    def update_order(self, id: str, products: list[dict]):
        try:
            order = entities.Order(
                id, [entities.Product(**p) for p in products])
            self.__repository.update(id, order)
            return True, order
        except PersistenceException as e:
            return False, f"Erros de persistência: {e}"

    def get_orders(self):
        return True, self.__repository.getAll()

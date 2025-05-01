from business import entities
from infra import repositories
from business import commands


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

    def create_order(self, id, products):
        order = entities.Order(id, products)
        self.__repository.create(order)

    def update_order(self, id: str, products: list[entities.Product]):
        self.__repository.update(id, products)
                    
    def get_orders(self):
        return self.__repository.getAll()

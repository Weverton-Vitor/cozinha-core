from business import entities
from infra import repositories
from business import commands


class OrderController:
    __repository: repositories.IOrderRepository
    __command: commands.Command

    def __init__(
        self,
        repository: repositories.IOrderRepository,
        command: commands.Command
    ):
        self.__repository = repository
        self.__command = command


def set_command(self, command: commands.Command):
    self.__command = command


def execute_command(self):
    self.__command.execute()


def create_order():
    return

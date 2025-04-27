from business import services
from business import validators
from business import entities
from infra import repositories
from infra import exceptions
from business import commands


class OrderController:
    __service: services.Service
    __repository: repositories.IKitchenRepository
    __command: commands.Command

    def __init__(
        self,
        service: services.KitchensService = None,
        repository: repositories.IKitchenRepository = None,
        command: commands.Command = None
    ):
        if service is None:
            self.__service = services.KitchensService(
                validators.UsernameValidator(),
                validators.PasswordValidator(),
            )
        else:
            self.__service = service

        if repository is None:
            self.__repository = repositories.InMemoryKitchenRepository()
        else:
            self.__repository = repository
        self.__command = command

def setCommand(self, command: commands.Command):
    self.__command = command

def executeCommand(self):
    self.__command.execute()

def createOrder():
    return 
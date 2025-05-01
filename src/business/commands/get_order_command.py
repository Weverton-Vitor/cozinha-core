from business.commands import Command
from infra import repositories

class GetOrderCommand(Command):
    def __init__(id: str):
        return 
    
    def execute(self, repository: repositories.IOrderRepository):
        return self.__repository.get(identifier=self.__id)


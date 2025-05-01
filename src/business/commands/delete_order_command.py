from business.commands import Command
from infra import repositories

class DeleteOrderCommand(Command):
    def __init__(id: str):
        super().__init__(id) 
    
    def execute(self, repository: repositories.IOrderRepository):
        repository.delete(self.__id)
    

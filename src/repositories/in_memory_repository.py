import entities
from repositories import ISuppliersRepository

class InMemoryRepository(ISuppliersRepository):
    __suppliers: list[entities.Supplier]

    def __init__(self):
        self.__suppliers = []  
    
    def create(self, supplier: entities.Supplier) -> None:
        self.__suppliers.append(supplier)
    
    def getAll(self) -> list[entities.Supplier]:
        return self.__suppliers

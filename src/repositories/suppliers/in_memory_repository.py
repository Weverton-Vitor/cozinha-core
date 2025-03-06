import entities
from repositories import ISuppliersRepository

class InMemorySuppliersRepository(ISuppliersRepository):
    __suppliers: list[entities.Supplier]

    def __init__(self):
        self.__suppliers = []  
    
    def create(self, supplier: entities.Supplier) -> None:
        self.__suppliers.append(supplier)

    def delete(self, username: str) -> None:
        supplier_to_delete = next((sup for sup in self.__suppliers if sup.username == username), None)
        if supplier_to_delete:
            self.__suppliers.remove(supplier_to_delete)

    def update(self, username: str, supplier: entities.Supplier) -> None:
        for index, sup in enumerate(self.__suppliers):
            if sup.username == username:
                self.__suppliers[index] = supplier
                return

    def get(self, username: str) -> entities.Supplier | None:
        supplier = next((sup for sup in self.__suppliers if sup.username == username), None)
        return supplier
    
    def getAll(self) -> list[entities.Supplier]:
        return self.__suppliers

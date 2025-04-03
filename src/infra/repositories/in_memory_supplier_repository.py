from infra.repositories import interfaces
from business.entities import Supplier

class InMemorySuppliersRepository(interfaces.ISupplierRepository):
    def __init__(self):

        self._suppliers = {}

    def create(self, supplier: Supplier) -> None:
        
        self._suppliers[supplier.username] = supplier

    def delete(self, username: str) -> None:
        
        if username in self._suppliers:
            del self._suppliers[username]

    def update(self, username: str, supplier: Supplier) -> None:
        
        if username in self._suppliers:
            self._suppliers[username] = supplier

    def get(self, username: str) -> Supplier | None:
        
        return self._suppliers.get(username)

    def getAll(self) -> list[Supplier]:
        
        return list(self._suppliers.values())

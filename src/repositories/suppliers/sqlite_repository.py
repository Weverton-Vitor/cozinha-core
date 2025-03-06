import entities
from repositories import ISuppliersRepository


class SQLiteSuppliersRepository(ISuppliersRepository):
    __suppliers: list[entities.Supplier]

    def __init__(self):
        self.__suppliers = []

    def create(self, supplier: entities.Supplier) -> None:
        pass

    def delete(self, username: str) -> None:
        pass

    def update(self, username: str, supplier: entities.Supplier) -> None:
        pass

    def get(self, username: str) -> entities.Supplier | None:
        pass

    def getAll(self) -> list[entities.Supplier]:
        pass

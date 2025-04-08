from business import entities
from infra import factories
from infra.repositories import interfaces


class InMemorySuppliersRepository(interfaces.ISupplierRepository):
    def __init__(self):
        dao_factory = factories.ArrayDAOFactory()
        self.supplier_dao = dao_factory.get_supplier_dao()

    def create(self, supplier: entities.Supplier) -> None:
        self.supplier_dao.create(supplier)

    def delete(self, username: str) -> None:
        self.supplier_dao.delete(username)

    def update(self, username: str, supplier: entities.Supplier) -> None:
        self.supplier_dao.update(username, supplier)

    def get(self, username: str) -> entities.Supplier | None:
        return self.supplier_dao.get(username)

    def getAll(self) -> list[entities.Supplier]:
        return self.supplier_dao.getAll()

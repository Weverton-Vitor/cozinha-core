from business import entities
from infra import factories
from infra.repositories import interfaces


class InMemoryProductRepository(interfaces.IproductRepository):
    def __init__(self):
        dao_factory = factories.ArrayDAOFactory()
        self.product_dao = dao_factory.get_product_dao()

    def create(self, product: entities.Product) -> None:
        self.product_dao.create(product)

    def delete(self, product_id: str) -> None:
        self.product_dao.delete(product_id)

    def update(self, product_id: str, product: entities.Product) -> None:
        self.product_dao.update(product_id, product)

    def get(self, product_id: str) -> entities.Product | None:
        return self.product_dao.get(product_id)

    def getAll(self) -> list[entities.Product]:
        return self.product_dao.getAll()

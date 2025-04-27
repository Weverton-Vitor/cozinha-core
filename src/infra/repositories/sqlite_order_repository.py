from business import entities
from infra import repositories
from infra.factories.sqlite_dao_factory import SQLIteDAOFactory

class SQLiteOrderRepository(repositories.interfaces.IOrderRepository):
    def __init__(self):
        dao_factory = SQLIteDAOFactory()
        self.order_dao = dao_factory.get_order_dao()

    def create(self, order: entities.Order) -> None:
        self.order_dao.create(order)

    def delete(self, id: str) -> None:
        self.order_dao.delete(id)

    def update(self, id: str, order: entities.Order) -> None:
        self.order_dao.update(id, order)

    def get(self, id: str) -> entities.Order | None:
        return self.order_dao.get(id)

    def getAll(self) -> list[entities.Order]:
        return self.order_dao.getAll()
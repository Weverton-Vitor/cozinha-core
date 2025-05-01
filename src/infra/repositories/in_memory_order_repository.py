from infra.dao import IOrderDAO
from infra.repositories import interfaces
from business import entities

class InMemoryOrderRepository(interfaces.IOrderRepository):
    def __init__(self, order_dao: IOrderDAO):
        self.order_dao = order_dao

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

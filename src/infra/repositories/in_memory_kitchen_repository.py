from infra.factories.array_dao_factory import ArrayDAOFactory
from infra.repositories import interfaces
from business import entities

class InMemoryKitchenRepository(interfaces.IKitchenRepository):
    def __init__(self):
        dao_factory = ArrayDAOFactory()
        self.kitchen_dao = dao_factory.get_kitchen_dao()

    def create(self, kitchen: entities.Kitchen) -> None:
        self.kitchen_dao.create(kitchen)

    def delete(self, username: str) -> None:
        self.kitchen_dao.delete(username)

    def update(self, username: str, kitchen: entities.Kitchen) -> None:
        self.kitchen_dao.update(username, kitchen)

    def get(self, kitchenname: str) -> entities.Kitchen | None:
        return self.kitchen_dao.get(kitchenname)

    def getAll(self) -> list[entities.Kitchen]:
        return self.kitchen_dao.getAll()

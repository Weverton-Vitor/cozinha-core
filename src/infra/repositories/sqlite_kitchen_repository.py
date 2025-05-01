from business import entities
from infra import repositories
from infra.factories.sqlite_dao_factory import SQLIteDAOFactory

# TODO write SQLiteKitchenRepository class that implements IKitchenRepository interface


class SQLiteKitchenRepository(repositories.interfaces.IKitchenRepository):
    def __init__(self, kitchen_dao):
        self.kitchen_dao = kitchen_dao

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

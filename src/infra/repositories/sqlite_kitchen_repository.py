from infra import repositories
from business import entities
from factories import sqlite_dao_factory

class SQLiteKitchenRepository(repositories.interfaces.IKitchenRepository):
    kitchen_dao = sqlite_dao_factory.SQLIteDAOFactory.get_kitchen_dao()

    def create(self, kitchen: entities.Kitchen) -> None:
        pass

    def delete(self, username: str) -> None:
        pass

    def update(self, username: str, kitchen: entities.Kitchen) -> None:
        pass

    def get(self, username: str) -> entities.Kitchen | None:
        pass

    def getAll(self) -> list[entities.Kitchen]:
        pass

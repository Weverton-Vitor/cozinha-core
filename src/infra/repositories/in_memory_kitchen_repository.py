from infra.repositories import interfaces
from business import entities

class InMemoryKitchenRepository(interfaces.IKitchenRepository):
    def __init__(self):
        self._kitchens = []

    def create(self, kitchen: entities.Kitchen) -> None:
        self._kitchens.append(kitchen)

    def delete(self, username: str) -> None:
        self._kitchens = [k for k in self._kitchens if k.username != username]

    def update(self, username: str, kitchen: entities.Kitchen) -> None:
        for index, existing_kitchen in enumerate(self._kitchens):
            if existing_kitchen.username == username:
                self._kitchens[index] = kitchen
                return

    def get(self, username: str) -> entities.Kitchen | None:
        return next((k for k in self._kitchens if k.username == username), None)

    def getAll(self) -> list[entities.Kitchen]:
        return self._kitchens

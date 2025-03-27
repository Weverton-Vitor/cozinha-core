from typing import TypeVar, List
from repositories import interface_repository

T = TypeVar("T")

class InMemoryRepository(interface_repository.InterfaceRepository):
    def __init__(self):
        self._items: List[T] = []

    def create(self, item: T) -> None:
        self._items.append(item)

    def delete(self, identifier: str) -> None:
        item_to_delete = next((item for item in self._items if getattr(item, "username", None) == identifier), None)
        if item_to_delete:
            self._items.remove(item_to_delete)

    def update(self, identifier: str, item: T) -> None:
        for index, existing_item in enumerate(self._items):
            if getattr(existing_item, "username", None) == identifier:
                self._items[index] = item
                return

    def get(self, identifier: str) -> T | None:
        return next((item for item in self._items if getattr(item, "username", None) == identifier), None)

    def getAll(self) -> List[T]:
        return self._items

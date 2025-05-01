from typing import List
from infra.dao import interfaces
from business import entities


class ArrayOrderDAO(interfaces.IOrderDAO):
    def __init__(self):
        self._items: List[entities.Order] = []

    def connect(self):
        pass

    def query(self, condition=lambda item: True):
        raise NotImplementedError()

    def create(self, item: entities.Order) -> None:
        self._items.append(item)

    def delete(self, identifier: str) -> None:
        item_to_delete = next(
            (
                item
                for item in self._items
                if getattr(item, "id", None) == identifier
            ),
            None,
        )
        if item_to_delete:
            self._items.remove(item_to_delete)

    def update(self, identifier: str, item: entities.Order) -> None:
        for index, existing_item in enumerate(self._items):
            if getattr(existing_item, "id", None) == identifier:
                self._items[index] = item
                return

    def get(self, identifier: str) -> entities.Order | None:
        return next(
            (
                item
                for item in self._items
                if getattr(item, "id", None) == identifier
            ),
            None,
        )

    def getAll(self) -> List[entities.Order]:
        return self._items

    def close(self):
        pass

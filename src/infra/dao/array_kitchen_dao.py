from typing import List
from infra.dao import interfaces
from business import entities


class ArrayKitchenDAO(interfaces.IKitchenDAO):
    def __init__(self):
        self._items: List[entities.Kitchen] = []

    def connect(self):
        pass

    def query(self, condition=lambda item: True):
        raise NotImplementedError()

    def create(self, item: entities.Kitchen) -> None:
        self._items.append(item)

    def delete(self, identifier: str) -> None:
        item_to_delete = next(
            (
                item
                for item in self._items
                if getattr(item, "username", None) == identifier
            ),
            None,
        )
        if item_to_delete:
            self._items.remove(item_to_delete)

    def update(self, identifier: str, item: entities.Kitchen) -> None:
        for index, existing_item in enumerate(self._items):
            if getattr(existing_item, "username", None) == identifier:
                self._items[index] = item
                return

    def get(self, identifier: str) -> entities.Kitchen | None:
        return next(
            (
                item
                for item in self._items
                if getattr(item, "username", None) == identifier
            ),
            None,
        )

    def getAll(self) -> List[entities.Kitchen]:
        return self._items

    def close(self):
        pass

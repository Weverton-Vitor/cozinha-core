from typing import List
from business import entities
from infra.dao import interfaces


class ArrayProductDAO(interfaces.IProductDAO):
    def __init__(self):
        self._items: List[entities.Product] = []

    def connect(self):
        pass  # Nenhuma conexão necessária para armazenamento em memória

    def query(self, condition=lambda item: True):
        raise NotImplementedError()
    
    def create(self, item: entities.Product) -> None:
        self._items.append(item)

    def delete(self, identifier: str) -> None:
        item_to_delete = next((item for item in self._items if item.get_product_id() == identifier), None)
        if item_to_delete:
            self._items.remove(item_to_delete)

    def update(self, identifier: str, item: entities.Product) -> None:
        for index, existing_item in enumerate(self._items):
            if existing_item.get_product_id() == identifier:
                self._items[index] = item
                return

    def get(self, identifier: str) -> entities.Product | None:
        return next((item for item in self._items if item.get_product_id() == identifier), None)

    def getAll(self) -> List[entities.Product]:
        return self._items

    def close(self):
        pass  # Nenhuma conexão para fechar
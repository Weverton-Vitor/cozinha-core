from typing import TypeVar, List
from dao import interfaces

T = TypeVar("T")


class ArrayKitchenDAO(interfaces.IKitchenDAO):
    def __init__(self):
        self._items: List[T] = []

    def connect(self):
        pass  # Nenhuma conexão necessária para armazenamento em memória

    def query(self, condition=lambda item: True):
        return [item for item in self._items if condition(item)]

    def close(self):
        pass  # Nenhuma conexão para fechar

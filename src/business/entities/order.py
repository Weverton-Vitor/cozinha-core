from business import entities
from business.memento import order_memento


class Order:
    __id: str
    __products: list[entities.Product]

    def __init__(self, id: str, products: list[entities.Product]):
        self.__id = id
        self.__products = products

    def set_id(self, id: str):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_products(self, products: list[entities.Product]):
        self.__products = products

    def get_products(self):
        return self.__products

    def save_state(self):
        return order_memento.OrderMemento(self.__id, self.__products)

    def restore_state(self, memento: order_memento.OrderMemento):
        self.__id = memento.get_id()
        self.__products = memento.get_products()

    def to_json(self):
        return {
            "id": self.__id,
            "products": [product.to_json() for product in self.__products]
        }

    def __str__(self):
        return f"Order {{ Id: {self.__id}}}"

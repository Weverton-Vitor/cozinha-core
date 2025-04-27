import Products
from business.memento import order_memento

class Order:
    __id: str
    __products: list[Products]

    def __init__(self, id: str, products: list[Products]):
        self.__id = id
        self.__products = products

    def set_id(self, id: str):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_products(self, products: list[Products]):
        self.__products = products

    def get_products(self):
        return self.__products
    
    def save_state(self):
        return order_memento.OrderMemento(self.__id, self.__products)
    
    def restore_state(self, memento: order_memento.OrderMemento):
        self.__id = memento.get_id()
        self.__products = memento.get_products()

    def __str__(self):
        return f"Order {{ Id: {self.__id}}}"


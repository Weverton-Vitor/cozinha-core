from business.entities import Product

class OrderMemento:
    __id: str
    __products: list[Product]

    def __init__(self, id: str, products: list[Product]):
        self.__id = id
        self.__products = products

    def get_id(self):
        return self.__id
    
    def get_products(self):
        return self.__products

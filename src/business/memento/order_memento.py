from typing import List
import Products

class OrderMemento:
    __id: str
    __products: List[Products]

    def __init__(self, id: str, products: List[Products]):
        self.__id = id
        self.__products = products

    def get_id(self):
        return self.__id
    
    def get_products(self):
        return self.__products

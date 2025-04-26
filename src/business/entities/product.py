class Product:
    __product_id: str
    __name: str
    __stock: float

    def __init__(self, product_id: str, name: str, stock: float):
        self.__product_id = product_id
        self.__name = name
        self.__stock = stock

    def set_product_id(self, product_id: str):
        self.__product_id = product_id

    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name: str):
        self.__name = name

    def get_stock(self):
        return self.__stock
    
    def set_stock(self, stock: float):
        self.__stock = stock

    def __str__(self):
        return f"Product {{ {self.__product_id} }}"

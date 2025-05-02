from src.business.event.product_events import EventListener

class Product(EventListener):
    __product_id: str
    __name: str
    __stock: float
    __unit: str

    def __init__(self, product_id: str, name: str, stock: float, unit: str):
        self.__product_id = product_id
        self.__name = name
        self.__stock = stock
        self.__unit = unit

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

    def get_unit(self):
        return self.__unit
    
    def set_unit(self, unit: str):
        self.__unit = unit

    def to_json(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "stock": self.__stock,
            "unit": self.__unit
        }

    def update(self, data: dict):
        """Recebe notificações do dispatcher"""
        if data.get("product_id") == self.__product_id:
            self.set_stock(data.get("new_stock"))
            print(f"Estoque do produto '{self.__name}' atualizado para {self.__stock}")

    def __str__(self):
        return f"Product {{ {self.__product_id} }}"

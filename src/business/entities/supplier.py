class Supplier:
    __name: str
    __password: str

    def __init__(self, name: str, password: str):
        self.__name = name
        self.__password = password

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password: str):
        self.__password = password

    def to_json(self):
        return {
            "name": self.__name,
            "password": self.__password
        }

    def __str__(self):
        return f"Supplier {{ {self.__name} }}"

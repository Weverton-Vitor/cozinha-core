
class Supplier:
    __name: str

    def __init__(self, name: str):
        self.__name = name
        pass

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Supplier {{ {self.__name} }}"

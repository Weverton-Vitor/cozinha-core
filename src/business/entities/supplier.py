class Supplier:
    __username: str
    __password: str

    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    def set_username(self, username: str):
        self.__username = username

    def get_username(self):
        return self.__username
    
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
        return f"Supplier {{ {self.__username} }}"

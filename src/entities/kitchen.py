class Kitchen:
    __name: str
    __user_name: str
    __password: str

    def __init__(self, name: str, password: str, user_name: str):
        self.__name = name
        self.__user_name = user_name
        self.__password = password

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_user_name(self, user_name: str):
        self.__user_name = user_name

    def get_user_name(self):
        return self.__user_name
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password: str):
        self.__password = password

    def __str__(self):
        return f"Supplier {{ {self.__name} }}"

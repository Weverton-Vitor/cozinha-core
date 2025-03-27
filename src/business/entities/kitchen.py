from datetime import datetime

class Kitchen:
    __name: str
    __user_name: str
    __password: str
    __address: str
    __phone_number: str
    __email: str
    __created_at: datetime

    def __init__(self, name: str, password: str, user_name: str, address: str, phone_number: str, email: str):
        self.__name = name
        self.__user_name = user_name
        self.__password = password
        self.__address = address
        self.__phone_number = phone_number
        self.__email = email
        self.__created_at = datetime.now()

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_user_name(self, user_name: str):
        self.__user_name = user_name

    def get_user_name(self):
        return self.__user_name

    def set_password(self, password: str):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_address(self, address: str):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

    def set_email(self, email: str):
        self.__email = email

    def get_email(self):
        return self.__email

    def get_created_at(self):
        return self.__created_at

    def __str__(self):
        return f"Kitchen {{ Name: {self.__name}, Address: {self.__address} }}"

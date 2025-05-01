from business import controllers


class SupplierView:
    __controller: controllers.SupplierController

    def __init__(self, controller: controllers.SupplierController):
        self.__controller = controller

    def create_supplier(self, name: str, password: str):
        self.__controller.add_supplier(name, password)

    def display_suppliers(self):
        suppliers = self.__controller.get_suppliers()
        for supplier in suppliers:
            print(supplier)

    def update_supplier(self):
        pass

    def remove_supplier(self):
        pass

    def show_message(self, message: str):
        print(message)

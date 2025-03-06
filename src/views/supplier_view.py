from controllers import supplier_controller

class SupplierView:
    __controller: supplier_controller.SupplierController
    
    def __init__(self, controller: supplier_controller.SupplierController):
        self.__controller = controller
        pass

    def create_supplier(self, name: str, password: str, option: bool):
        self.__controller.add_supplier(name, password, option)
        
    def display_suppliers(self, option: bool):
        suppliers = self.__controller.get_suppliers(option)
        for supplier in suppliers:
            print(supplier)

    def show_message(self, message: str):
        print(message)

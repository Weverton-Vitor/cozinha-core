import entities

class SupplierController:
    __suppliers: list[entities.Supplier]

    def __init__(self):
        self.__suppliers = []
        pass

    def add_supplier(self, name: str):
        sup = entities.Supplier(name)
        self.__suppliers.append(sup)

    def get_suppliers(self):
        return self.__suppliers

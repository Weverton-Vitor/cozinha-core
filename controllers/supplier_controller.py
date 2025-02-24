import entities
from views import supplier_view


class SupplierController:
    __suppliers: list[entities.Supplier]
    __view: supplier_view.SupplierView

    def __init__(self, view: supplier_view.SupplierView):
        self.__view = view
        self.__suppliers = []
        pass

    def add_supplier(self, name: str):
        sup = entities.Supplier(name)
        self.__suppliers.append(sup)
        self.__view.show_message("Fornecedor adicionado com sucesso: " + name)

    def show_suppliers(self):
        self.__view.display_suppliers(self.__suppliers)

import entities


class SupplierView:
    def display_suppliers(self, suppliers: list[entities.Supplier]):
        for supplier in suppliers:
            print(supplier)

    def show_message(self, message: str):
        print(message)

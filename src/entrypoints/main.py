import controllers
import views
from repositories import SQLiteSupplierRepository

def main():
    supplier_controller = controllers.SupplierController(repository=SQLiteSupplierRepository())
    supplier_view = views.SupplierView(supplier_controller)

    supplier_view.create_supplier("Ceasa", "Gf3/@sfsdeasaFsd")
    supplier_view.create_supplier("Assaí", "12348")
    supplier_view.create_supplier("Assaí_um", "testeeeee")
    supplier_view.create_supplier("Assaí_dois", "testeeeeeA")
    supplier_view.create_supplier("Assaí_tres", "testeeeeeA2")
    supplier_view.create_supplier("Assaí_quatro", "testeeeeeA2@")
    supplier_view.create_supplier("Assaí Atacadista", "testeeeeeA2@")

    supplier_view.display_suppliers()


if __name__ == "__main__":
    main()

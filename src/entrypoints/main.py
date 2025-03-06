import controllers
import views


def main():
    supplier_controller = controllers.SupplierController()
    supplier_view = views.SupplierView(supplier_controller)

    supplier_view.create_supplier("Ceasa", "Gf3/@sfsdeasaFsd", 1)
    supplier_view.create_supplier("Assaí Atacadista", "1234", 1)
    supplier_view.create_supplier("Assaí Atacadista", "testeeeee", 1)
    supplier_view.create_supplier("Assaí Atacadista", "testeeeeeA", 1)
    supplier_view.create_supplier("Assaí Atacadista", "testeeeeeA2", 1)
    supplier_view.create_supplier("Assaí Atacadista", "testeeeeeA2@", 1)

    supplier_view.display_suppliers(1)


if __name__ == "__main__":
    main()

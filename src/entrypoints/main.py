import controllers
import views


def main():
    supplier_controller = controllers.SupplierController()
    supplier_view = views.SupplierView(supplier_controller)

    supplier_view.create_supplier("Ceasa", "Gf3/@sfsdeasaFsd")
    supplier_view.create_supplier("Assaí Atacadista", "1234")
    supplier_view.create_supplier("Assaí Atacadista", "testeeeee")
    supplier_view.create_supplier("Assaí Atacadista", "testeeeeeA")
    supplier_view.create_supplier("Assaí Atacadista", "testeeeeeA2")
    supplier_view.create_supplier("Assaí Atacadista", "testeeeeeA2@")

    supplier_view.display_suppliers(1)


if __name__ == "__main__":
    main()

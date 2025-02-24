import controllers
import views


def main():
    supplier_view = views.SupplierView()
    supplier_controller = controllers.SupplierController(supplier_view)

    supplier_controller.add_supplier("Ceasa")
    supplier_controller.add_supplier("Assaí Atacadista")

    supplier_controller.show_suppliers()


if __name__ == "__main__":
    main()

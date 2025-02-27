import controllers
import views


def main():
    supplier_controller = controllers.SupplierController()
    supplier_view = views.SupplierView(supplier_controller)

    supplier_controller.add_supplier("Ceasa")
    supplier_controller.add_supplier("Assaí Atacadista")

    supplier_view.display_suppliers()


if __name__ == "__main__":
    main()

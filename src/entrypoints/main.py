import controllers
import views


def main():
    supplier_controller = controllers.SupplierController()
    supplier_view = views.SupplierView(supplier_controller)

    supplier_controller.add_supplier("Ceasa", "Gf3/@sfsdeasaFsd")
    supplier_controller.add_supplier("Assaí Atacadista", "1234")
    supplier_controller.add_supplier("Assaí Atacadista", "testeeeee")
    supplier_controller.add_supplier("Assaí Atacadista", "testeeeeeA")
    supplier_controller.add_supplier("Assaí Atacadista", "testeeeeeA2")
    supplier_controller.add_supplier("Assaí Atacadista", "testeeeeeA2@")


    supplier_view.display_suppliers()

if __name__ == "__main__":
    main()

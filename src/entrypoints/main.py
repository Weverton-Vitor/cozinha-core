import controllers
import views


def main():
    supplier_controller = controllers.SupplierController()
    supplier_view = views.SupplierView(supplier_controller)

    supplier_controller.add_supplier("", "Gf3/@sfsdeasaFsd")
    supplier_controller.add_supplier("Assaí Atacadista", "Gf3/@sfsdeasaFsd")
    supplier_controller.add_supplier("Assái2", "testeeeeeA2@")
    supplier_controller.add_supplier("Assaí Ataca", "1234")
    supplier_controller.add_supplier("Assaí Ataca", "testeeeee")
    supplier_controller.add_supplier("Assaí Ataca", "testeeeeeA")
    supplier_controller.add_supplier("Assaí Ataca", "testeeeeeA2")
    supplier_controller.add_supplier("Assaí Ataca", "testeeeeeA2@")

    supplier_controller.add_supplier("Ceasa", "Gf3/@sfsdeasaFsd")


    supplier_view.display_suppliers()

if __name__ == "__main__":
    main()

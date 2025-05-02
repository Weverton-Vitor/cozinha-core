import uuid
import flask

from business import controllers, facades


class ProductView:
    __controller: controllers.ProductController

    def __init__(self, controller: controllers.ProductController):
        self.__controller = controller

    def create_product(self, product_id: str, name: str, stock: float, unit: str):
        self.__controller.add_product(product_id, name, stock, unit)

    def update_product(self):
        data = flask.request.get_json()
        name = str(data.get("name", None))
        stock = float(data.get("stock", None))
        unit = str(data.get("unit", None))


        success, result = self.__controller.add_product(
            product_id=str(uuid.uuid4()), name=name, stock=stock, unit=unit
        )

        if not success:
            return {"success": False, "message": result}, 400

        return {"success": True, "product": result}, 201

    def remove_product(self, name: str):
        success, result = self.__controller.delete_product(name)

        if not success:
            return {"success": False, "message": result}, 400

        return {"success": True, "product": result.to_json()}, 200

    def display_products(self):
        products = self.__controller.get_products()
        for product in products:
            print(product)

    def show_message(self, message: str):
        print(message)

    def genereate_report(self, report_facade: facades.ReportFacade):
        return report_facade.report()

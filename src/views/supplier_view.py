import flask
from builders.supplier_view_builder import SupplierViewBuilder
from builders.view_director import ViewDirector
from business import controllers

supplier_bp = flask.Blueprint('supplier', __name__)

class SupplierView:
    __controller: controllers.SupplierController

    def __init__(self, controller: controllers.SupplierController):
        self.__controller = controller

    def create_supplier(self, name: str, password: str):
        self.__controller.add_supplier(name, password)

    def display_suppliers(self):
        suppliers = self.__controller.get_suppliers()
        for supplier in suppliers:
            print(supplier)

    def show_message(self, message: str):
        print(message)

supplier_view_builder = SupplierViewBuilder()
view_director = ViewDirector(supplier_view_builder)
view_director.make()
supplier_view = supplier_view_builder.get_product()

supplier_bp.add_url_rule(
    '/', view_func=supplier_view.create_supplier, methods=['POST'])
supplier_bp.add_url_rule(
    '/', view_func=supplier_view.update_supplier, methods=['PUT'])
supplier_bp.add_url_rule(
    '/', view_func=supplier_view.remove_supplier, methods=['DELETE'])
supplier_bp.add_url_rule(
    '/', view_func=supplier_view.display_suppliers, methods=['GET'])
supplier_bp.add_url_rule(
    '/report', view_func=supplier_view.genereate_report, methods=['GET'])
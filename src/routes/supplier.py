import flask
from builders.supplier_view_builder import SupplierViewBuilder
from builders.view_director import ViewDirector

supplier_bp = flask.Blueprint('supplier', __name__)

supplier_view_builder = SupplierViewBuilder()
view_director = ViewDirector(supplier_view_builder)
view_director.make()
supplier_view = supplier_view_builder.get_product()

print(supplier_view)

supplier_bp.add_url_rule(
    '/', view_func=supplier_view.create_supplier, methods=['POST'])
supplier_bp.add_url_rule(
    '/', view_func=supplier_view.update_supplier, methods=['PUT'])
supplier_bp.add_url_rule(
    '/', view_func=supplier_view.remove_supplier, methods=['DELETE'])
supplier_bp.add_url_rule(
    '/', view_func=supplier_view.display_suppliers, methods=['GET'])

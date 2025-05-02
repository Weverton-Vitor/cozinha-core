# Create the blueprint
import flask

from builders import ViewDirector
from builders.product_view_builder import ProductViewBuilder

product_bp = flask.Blueprint('product', __name__)

product_view_builder = ProductViewBuilder()
view_director = ViewDirector(product_view_builder)
view_director.make()
product_view = product_view_builder.get_product()

product_bp.add_url_rule(
    '/', view_func=product_view.create_product, methods=['POST'])
product_bp.add_url_rule(
    '/', view_func=product_view.update_product, methods=['PUT'])
product_bp.add_url_rule(
    '/<name>', view_func=product_view.remove_product, methods=['DELETE'])
product_bp.add_url_rule(
    '/<name>', view_func=product_view.get_product, methods=['GET'])
product_bp.add_url_rule(
    '/', view_func=product_view.display_products, methods=['GET'])

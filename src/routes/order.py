# Create the blueprint
import flask

from builders import ViewDirector
from builders.order_view_builder import OrderViewBuilder

order_bp = flask.Blueprint('order', __name__)

order_view_builder = OrderViewBuilder()
view_director = ViewDirector(order_view_builder)
view_director.make()
order_view = order_view_builder.get_product()

order_bp.add_url_rule(
    '/', view_func=order_view.create_order, methods=['POST'])
order_bp.add_url_rule(
    '/', view_func=order_view.up, methods=['PUT'])
order_bp.add_url_rule(
    '/', view_func=order_view.delete_order, methods=['DELETE'])
order_bp.add_url_rule(
    '/', view_func=order_view.display_orders, methods=['GET'])

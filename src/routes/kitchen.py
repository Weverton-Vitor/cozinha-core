# Create the blueprint
import flask

from builders import ViewDirector
from builders.kitchen_view_builder import KitchenViewBuilder

kitchen_bp = flask.Blueprint('kitchen', __name__)

kitchen_view_builder = KitchenViewBuilder()
view_director = ViewDirector(kitchen_view_builder)
view_director.make()
kitchen_view = kitchen_view_builder.get_product()

kitchen_bp.add_url_rule(
    '/', view_func=kitchen_view.create_kitchen, methods=['POST'])
kitchen_bp.add_url_rule(
    '/<name>', view_func=kitchen_view.update_kitchen, methods=['PUT'])
kitchen_bp.add_url_rule(
    '/<name>', view_func=kitchen_view.remove_kitchen, methods=['DELETE'])
kitchen_bp.add_url_rule(
    '/<name>', view_func=kitchen_view.get_kitchen, methods=['GET'])
kitchen_bp.add_url_rule(
    '/', view_func=kitchen_view.display_kitchens, methods=['GET'])
kitchen_bp.add_url_rule(
    '/report', view_func=kitchen_view.genereate_report, methods=['GET'])

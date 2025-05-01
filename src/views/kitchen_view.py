import flask

from builders import ViewDirector
from builders.kitchen_view_builder import KitchenViewBuilder
from business import services, validators, controllers, facades
from infra import repositories


# Create the blueprint
kitchen_bp = flask.Blueprint('kitchen', __name__)


class KitchenView:
    __controller_kitchen: controllers.KitchenController

    def __init__(self, controller_kitchen: controllers.KitchenController):
        self.__controller_kitchen = controller_kitchen

    def create_kitchen(
        self,
        #
        #
        #
        #
        #
        #
    ):
        data = flask.request.get_json()
        name = str(data.get("name", None))
        password = str(data.get("password", None))
        user_name = str(data.get("user_name", None))
        address = str(data.get("address", None))
        phone_number = str(data.get("phone_number", None))
        email = str(data.get("email", None))

        result = self.__controller_kitchen.add_kitchen(
            name, password, user_name, address, phone_number, email
        )

        if result:
            return {"success": False, "message": result}, 400

        return {"success": True}, 201

    # TODO
    def update_kitchen(self):
        return {"to": "do"}

    # TODO
    def display_kitchens(self):
        kitchens = self.__controller_kitchen.get_kitchens()
        return kitchens

    def show_message(self, message: str):
        print(message)

    def genereate_report(self, report_facade: facades.ReportFacade):    
        return report_facade.report()
    
    # TODO
    def remove_kitchen(self):
        return {"to": "do"}


kitchen_view_builder = KitchenViewBuilder()
view_director = ViewDirector(kitchen_view_builder)
view_director.make()
kitchen_view = kitchen_view_builder.get_product()

kitchen_bp.add_url_rule(
    '/', view_func=kitchen_view.create_kitchen, methods=['POST'])
kitchen_bp.add_url_rule(
    '/', view_func=kitchen_view.update_kitchen, methods=['PUT'])
kitchen_bp.add_url_rule(
    '/', view_func=kitchen_view.remove_kitchen, methods=['DELETE'])
kitchen_bp.add_url_rule(
    '/', view_func=kitchen_view.display_kitchens, methods=['GET'])
kitchen_bp.add_url_rule(
    '/report', view_func=kitchen_view.genereate_report, methods=['GET'])

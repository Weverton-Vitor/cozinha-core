from business import controllers, facades
import flask


class KitchenView:
    __controller_kitchen: controllers.KitchenController

    def __init__(self, controller_kitchen: controllers.KitchenController):
        self.__controller_kitchen = controller_kitchen

    def create_kitchen(self):
        data = flask.request.get_json()
        name = str(data.get("name", None))
        password = str(data.get("password", None))
        user_name = str(data.get("user_name", None))
        address = str(data.get("address", None))
        phone_number = str(data.get("phone_number", None))
        email = str(data.get("email", None))

        success, result = self.__controller_kitchen.add_kitchen(
            name, password, user_name, address, phone_number, email
        )

        if not success:
            return {"success": False, "message": result}, 400

        return {"success": True, "kitchen": result}, 201

    def update_kitchen(self):
        data = flask.request.get_json()
        name = str(data.get("name", None))

        kitchen_data = {
            "name": name,
            "password": str(data.get("password", None)),
            "user_name": str(data.get("user_name", None)),
            "address": str(data.get("address", None)),
            "phone_number": str(data.get("phone_number", None)),
            "email": str(data.get("email", None)),
        }

        result = self.__controller_kitchen.update_kitchen(name, kitchen_data)

        if result:
            return {"success": False, "message": result}, 400

        return {"success": True, "kitchen": result}, 200

    def display_kitchens(self):
        kitchens = self.__controller_kitchen.get_kitchens()
        return {"success": True, "kitchens": kitchens}, 200

    def show_message(self, message: str):
        print(message)

    def genereate_report(self, report_facade: facades.ReportFacade):
        return {"success": "True", "report": report_facade.report()}, 200

    def remove_kitchen(self):
        data = flask.request.g()
        name = str(data.get("name", None))

        result = self.__controller_kitchen.delete_kitchen(name)

        if result:
            return {"success": False, "message": result}, 400

        return {"success": True, "kitchen": result}, 200

import flask
from business import controllers


class SupplierView:
    __controller: controllers.SupplierController

    def __init__(self, controller: controllers.SupplierController):
        self.__controller = controller

    def create_supplier(self):
        data = flask.request.get_json()
        username = data.get("username", None)
        password = data.get("password", None)

        success, result = self.__controller.add_supplier(username, password)

        if not success:
            return {"success": success, "message": result}, 400

        return {"success": success, "supplier": result.to_json()}, 201

    def display_suppliers(self):
        success, result = self.__controller.get_suppliers()

        if not success:
            return {"success": success, "message": result}, 400

        suppliers = [s.to_json() for s in result]

        return {"success": True, "suppliers": suppliers}, 200

    def update_supplier(self, username):
        print(username)
        data = flask.request.get_json()

        supplier = {
            "username": username,
            "password": data.get("password", None)
        }

        success, result = self.__controller.update_supplier(username, supplier)

        if not success:
            return {"success": success, "message": result}, 400

        return {"success": True, "supplier": result.to_json()}, 200

    def remove_supplier(self, username):
        success, result = self.__controller.delete_supplier(username)

        if not success:
            return {"success": False, "message": result}, 400

        return {"success": True, "supplier": result.to_json()}, 200

    def get_supplier(self, username):

        success, result = self.__controller.get_supplier(username)

        if not success:
            return {"success": success, "message": result}, 400

        return {"success": True, "supplier": result.to_json()}, 200

    def show_message(self, message: str):
        print(message)

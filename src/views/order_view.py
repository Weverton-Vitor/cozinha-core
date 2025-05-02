import flask
from business import controllers
from business import entities
from business import commands
from uuid import uuid4


class OrderView:
    __controller_order: controllers.OrderController

    def __init__(self, controller_order: controllers.OrderController):
        self.__controller_order = controller_order

    def create_order(self):
        data = flask.request.get_json()
        products = data.get("products")
        id = uuid4()

        success, result = self.__controller_order.create_order(id, products)

        if not success:
            return {"success": False, "message": result}

        return {"success": True, "message": result.to_json()}

    def update_order(self, id):
        data = flask.request.get_json()
        products = data.get("products")

        success, result = self.__controller_order.update_order(id, products)

        if not success:
            return {"success": False, "message": result}

        return {"success": True, "message": result.to_json()}

    def display_orders(self):
        success, result = self.__controller_order.get_orders()

        if not success:
            return {"success": False, "message": result}

        orders = [o.to_json() for o in result]

        return {"success": True, "orders": orders}

    def delete_order(self, id: str):
        try:
            s, order = self.__controller_order.get_order(id)
            if not s:
                raise Exception("pedido não existe")

            command = commands.DeleteOrderCommand(id)
            self.__controller_order.set_command(command)
            self.__controller_order.execute_command()
            
            return {"success": True, "order": order}, 200
        except Exception as e:
            return {"success": False, "message": f"{e}"}, 400

    def get_order(self, id: str):
        success, result = self.__controller_order.get_order(id)

        if not success:
            return {"success": False, "message": result}, 400

        return {"success": True, "order": result.to_json() if result else None}, 200

    def show_message(self, message: str):
        print(message)

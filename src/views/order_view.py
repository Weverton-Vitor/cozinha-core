from business import controllers
from business import facades
from business import entities
from business import commands

class OrderView:
    __controller_order: controllers.OrderController

    def __init__(self, controller_order: controllers.OrderController):
        self.__controller_order = controller_order

    def create_order(
        self,
        id: str,
        products: list[entities.Products]
    ):
        self.__controller_order.create_order(
            id, products
        )

    def display_orders(self):
        orders = self.__controller_order.get_orders()
        for order in orders:
            print(order)

    def delete_order(self, id: str):
        command = commands.DeleteOrderCommand(id)
        self.__controller_order.set_command(command)
        self.__controller_order.execute_command()

    def get_order(self, id: str):
        command = commands.GetOrderCommand(id)
        self.__controller_order.set_command(command)
        self.__controller_order.execute_command()

    def show_message(self, message: str):
        print(message)
    

    

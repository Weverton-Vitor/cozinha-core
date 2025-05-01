from business import controllers
from business import facades

class ProductView:
    __controller: controllers.ProductController

    def __init__(self, controller: controllers.ProductController):
        self.__controller = controller

    def create_product(self, product_id: str, name: str, stock: float, unit: str):
        self.__controller.add_product(product_id, name, stock, unit)

    def display_products(self):
        products = self.__controller.get_products()
        for product in products:
            print(product)

    def show_message(self, message: str):
        print(message)

    def genereate_report(self, report_facade: facades.ReportFacade):    
        return report_facade.report()

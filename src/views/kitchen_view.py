from controllers import KitchenController
from facades import ReportFacaSingController

class KitchenView:
    __controller_kitchen: KitchenController

    def __init__(self, controller_kitchen: KitchenController):
        self.__controller_kitchen = controller_kitchen

    def create_kitchen(
        self,
        name: str,
        password: str,
        user_name: str,
        address: str,
        phone_number: str,
        email: str,
    ):
        self.__controller_kitchen.add_kitchen(
            name, password, user_name, address, phone_number, email
        )

    def display_kitchens(self):
        kitchens = self.__controller_kitchen.get_kitchens()
        for kitchen in kitchens:
            print(kitchen)

    def show_message(self, message: str):
        print(message)

    def genereate_report(self, report_facade: ReportFacaSingController):    
        return report_facade.report()
    

    

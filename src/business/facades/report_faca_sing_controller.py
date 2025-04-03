import json
from controllers import SupplierController, KitchenController
from repositories import InterfaceRepository
from entities import Supplier, Kitchen
from business.decorators import singleton


@singleton
class KitchenSupplierFacade:
    def __init__(
        self,
        supplier_repo: InterfaceRepository[Supplier],
        kitchen_repo: InterfaceRepository[Kitchen],
    ):
        self.supplier_controller = SupplierController(supplier_repo)
        self.kitchen_controller = KitchenController(kitchen_repo)

    # TODO: Call template
    def report(self) -> str:
        """Gera um relatório consolidado de fornecedores e cozinhas no formato JSON."""
        suppliers = self.supplier_controller.get_all_suppliers()
        kitchens = self.kitchen_controller.get_all_kitchens()

        report = {
            "suppliers": [{"name": s.name} for s in suppliers],
            "suppliers_count": len(suppliers),
            "kitchens": [{"name": k.name, "user_name": k.user_name} for k in kitchens],
            "kitchens_count": len(kitchens),
        }

        return json.dumps(report, indent=4)

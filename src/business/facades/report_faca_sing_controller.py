import json
from business import controllers
from infra import repositories
from business.decorators import singleton


@singleton
class KitchenSupplierFacade:
    def __init__(
        self,
        supplier_repo: repositories.interfaces.ISupplierRepository,
        kitchen_repo: repositories.interfaces.IKitchenRepository,
    ):
        self.supplier_controller = controllers.SupplierController(supplier_repo)
        self.kitchen_controller = controllers.KitchenController(kitchen_repo)

    # TODO: Call template
    def report(self) -> str:
        """Gera um relatório consolidado de fornecedores e cozinhas no formato JSON."""
        suppliers = self.supplier_controller.get_suppliers()
        kitchens = self.kitchen_controller.get_kitchens()

        report = {
            "suppliers": [{"name": s.name} for s in suppliers],
            "suppliers_count": len(suppliers),
            "kitchens": [{"name": k.name, "user_name": k.user_name} for k in kitchens],
            "kitchens_count": len(kitchens),
        }

        return json.dumps(report, indent=4)

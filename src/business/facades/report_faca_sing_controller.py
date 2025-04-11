import json
from business import controllers, services, templates, validators
from infra import repositories
from business.decorators import singleton


@singleton
class KitchenSupplierFacade:
    def __init__(
        self,
        supplier_repo: repositories.interfaces.ISupplierRepository,
        kitchen_repo: repositories.interfaces.IKitchenRepository,
        report: templates.SystemStatsReportExporter
    ):
        supplier_service = services.SuppliersService(
            validators.UsernameValidator(),
            validators.PasswordValidator(),
        )

        self.supplier_controller = controllers.SupplierController(supplier_service,
                                                                  supplier_repo)
        self.kitchen_controller = controllers.KitchenController(kitchen_repo)
        self._report = report

    def report(self, path_to_save) -> str:
        """Gera um relatório consolidado de fornecedores e cozinhas no formato JSON."""
        suppliers = self.supplier_controller.get_suppliers() or []
        kitchens = self.kitchen_controller.get_kitchens() or []

        self._report.exportar(suppliers + kitchens, path_to_save)

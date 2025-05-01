import json
from business import controllers, services, templates, validators
from infra import repositories
from business.decorators import singleton
import logger

# TODO
@singleton
class ReportFacade:
    def __init__(
        self,
        supplier_repo: repositories.interfaces.ISupplierRepository,
        kitchen_repo: repositories.interfaces.IKitchenRepository,
        product_repo: repositories.interfaces.IProductRepository,
        order_repo: repositories.interfaces.IOrderRepository,
        report: templates.ISystemStatsReportExporter
    ):
        supplier_service = services.SuppliersService(
            validators.UsernameValidator(),
            validators.PasswordValidator(),
        )
        logger_ = logger.PythonLoggerAdapter()

        self.supplier_controller = controllers.SupplierController(supplier_service,
                                                                  supplier_repo, 
                                                                  logger_)
        self.kitchen_controller = controllers.KitchenController(kitchen_repo)
        self.product_controller = controllers.ProductController(product_repo)
        self.order_controller = controllers.OrderController(order_repo)
        self._report = report

    def report(self, path_to_save) -> str:
        """Gera um relatório consolidado de fornecedores, cozinhas e produtos no formato JSON."""
        suppliers = self.supplier_controller.get_suppliers() or []
        kitchens = self.kitchen_controller.get_kitchens() or []
        products = self.product_controller.get_products() or []
        orders = self.order_controller.get_orders() or []

        self._report.exportar(suppliers + kitchens + products + orders, path_to_save)

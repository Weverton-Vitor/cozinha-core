import factories.interfaces
from infra import repositories
import factories


class SQLiteRepositoryFactory(factories.interfaces.IRepositoryFactory):
    def get_supplier_repository(self) -> repositories.interfaces.ISupplierRepository:
        return repositories.SQLiteSupplierRepository()

    def get_kitchen_repository(self) -> repositories.interfaces.IKitchenRepository:
        return repositories.SQLiteKitchenRepository()

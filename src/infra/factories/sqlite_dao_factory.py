# TODO write SQLIteDAOFactory class implementing of IDaoFactory

import factories.interfaces
from infra import repositories
import factories


class SQLIteDAOFactory(factories.interfaces.IRepositoryFactory):
    def get_supplier_repository(self) -> repositories.interfaces.ISupplierRepository:
        return repositories.InMemorySuppliersRepository()

    def get_kitchen_repository(self) -> repositories.interfaces.IKitchenRepository:
        return repositories.InMemoryKitchenRepository()

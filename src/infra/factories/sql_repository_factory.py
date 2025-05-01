from infra import repositories, factories


class SQLiteRepositoryFactory(factories.IRepositoryFactory):
    def get_supplier_repository(self) -> repositories.ISupplierRepository:
        return repositories.SQLiteSupplierRepository()

    def get_kitchen_repository(self, kitchen_dao) -> repositories.IKitchenRepository:
        return repositories.SQLiteKitchenRepository(kitchen_dao)

from infra import repositories, factories


class SQLiteRepositoryFactory(factories.IRepositoryFactory):
    def get_supplier_repository(self) -> repositories.ISupplierRepository:
        return repositories.SQLiteSupplierRepository()

    def get_product_repository(self) -> repositories.IProductRepository:
        return repositories.SQLiteProductRepository()

    def get_order_repository(self) -> repositories.interfaces.IOrderRepository:
        return repositories.SQLiteOrderRepository()
    
    def get_kitchen_repository(self, kitchen_dao) -> repositories.IKitchenRepository:
        return repositories.SQLiteKitchenRepository(kitchen_dao)

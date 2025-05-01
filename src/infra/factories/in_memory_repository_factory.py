from infra import repositories, factories


class InMemoryRepositoryFactory(factories.IRepositoryFactory):
    def get_supplier_repository(self) -> repositories.ISupplierRepository:
        return repositories.InMemorySuppliersRepository()

    def get_kitchen_repository(self) -> repositories.IKitchenRepository:
        return repositories.InMemoryKitchenRepository()

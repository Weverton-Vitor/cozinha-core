# Definição das interfaces dos repositórios
from abc import ABC, abstractmethod
from infra import repositories


# Definição da interface da fábrica
class IRepositoryFactory(ABC):
    @abstractmethod
    def get_supplier_repository(self) -> repositories.interfaces.ISupplierRepository:
        pass

    @abstractmethod
    def get_kitchen_repository(self) -> repositories.interfaces.IKitchenRepository:
        pass

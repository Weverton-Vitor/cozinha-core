from business import entities
from infra import repositories
from infra import exceptions
from business import observers
import logger


class ProductController:
    __repository: repositories.IProductRepository
    __logger: logger.LoggerAdapter
    __event_manager: observers.EventManager

    def __init__(
        self,
        repository: repositories.IProductRepository,
        logger: logger.LoggerAdapter,
        event_manager: observers.EventManager

    ):
        self.__repository = repository
        self.__logger = logger

    def add_product(self, product_id: str, name: str, unit: str, stock: float = 0):
        try:
            if stock < 0:
                self.__logger.log_error("Estoque não pode ser negativo")
                return None

            product = entities.Product(product_id, name, stock, unit)
            self.__repository.create(product)
            self.__logger.log_info(f"{product} created")

            # Notificar sobre a criação do produto
            self.__event_manager.notify(
                "product_created", {"product": product})

        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

    def update_product(self, identifier: str, product_dict: dict):
        try:
            product = entities.Product(**product_dict)

            old_product = self.__repository.get(identifier=identifier)
            old_stock = old_product.get_stock() if old_product else None

            if product.get_stock() < 0:
                self.__logger.log_error("Estoque não pode ser negativo")
                return None

            self.__repository.update(identifier=identifier, item=product)
            self.__logger.log_info(f"Produto {identifier} atualizado")

            # Notificar sobre a atualização do produto
            self.__event_manager.notify(
                "product_updated", {"product": product})

            # Se o estoque mudou, notificar especificamente sobre isso
            if old_stock is not None and old_stock != product.get_stock():
                self.__event_manager.notify("stock_changed", {
                    "product": product,
                    "old_stock": old_stock,
                    "new_stock": product.get_stock()
                })

            return product

        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")
            return f"Erro de persistência: {e}"
        except exceptions.LookupException as e:
            self.__logger.log_error(f"Produto não encontrado: {e}")
            return f"Produto não encontrado: {e}"

    def delete_product(self, identifier: str) -> tuple[bool, entities.Product]:
        try:
            product = self.__repository.delete(identifier=identifier)
            self.__logger.log_info(f"Produto {identifier} deletado")

            # Notificar sobre a exclusão do produto
            self.__event_manager.notify("product_deleted", {
                "product_id": identifier,
                "product": product
            })

            return product
        except exceptions.DeleteException as e:
            self.__logger.log_error(f"Erro ao excluir produto: {e}")
            return f"Erro ao excluir produto: {e}"
        except exceptions.LookupException as e:
            self.__logger.log_error(f"Produto não encontrado: {e}")
            return f"Produto não encontrado: {e}"

    def get_product(self, identifier: str) -> tuple[bool, entities.Product]:
        try:
            return True, self.__repository.get(identifier=identifier)
        except exceptions.LookupException as e:
            return False, "Produto não encontrado: {e}"

    def get_products(self):
        try:
            return self.__repository.getAll()
        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

from business import entities
from infra import repositories
from infra import exceptions
import logger


class ProductController:
    __repository: repositories.IProductRepository
    __logger: logger.LoggerAdapter

    def __init__(
        self,
        repository: repositories.IProductRepository,
        logger: logger.LoggerAdapter
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
        
        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")

    def update_product(self, identifier: str, product: entities.Product):
        try:
            if product.get_stock() < 0:
                self.__logger.log_error("Estoque não pode ser negativo")
                return None
                
            self.__repository.update(identifier=identifier, item=product)
            self.__logger.log_info(f"Produto {identifier} atualizado")
        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")
        except exceptions.LookupException as e:
            self.__logger.log_error(f"Produto não encontrado: {e}")

    def delete_product(self, identifier: str) -> entities.Product:
        try:
            product = self.__repository.delete(identifier=identifier)
            self.__logger.log_info(f"Produto {identifier} deletado")
            return product
        except exceptions.DeleteException as e:
            self.__logger.log_error(f"Erro ao excluir produto: {e}")
        except exceptions.LookupException as e:
            self.__logger.log_error(f"Produto não encontrado: {e}")

    def get_product(self, identifier: str) -> entities.Product:
        try:
            return self.__repository.get(identifier=identifier)
        except exceptions.LookupException as e:
            self.__logger.log_error(f"Produto não encontrado: {e}")

    def get_products(self):
        try:
            return self.__repository.getAll()
        except exceptions.PersistenceException as e:
            self.__logger.log_error(f"Erro de persistência: {e}")
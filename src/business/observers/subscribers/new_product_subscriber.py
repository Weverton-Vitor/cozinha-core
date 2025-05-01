from typing import Any, Dict
from business import observers


class NewProductSubscriber(observers.EventListener):
    """Assinante que monitora a criação de novos produtos"""

    def update(self, data: Dict[str, Any]) -> None | Dict[str, str]:
        """Processa atualizações de eventos relacionados à criação de produtos"""
        if "product" in data:
            product = data["product"]
            return {"msg": f"NOTIFICAÇÃO: Novo produto adicionado: '{product.name}'"}

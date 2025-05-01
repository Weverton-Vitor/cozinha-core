from typing import Any, Dict
from business import observers


class StockAlertSubscriber(observers.EventListener):
    """Assinante que monitora alterações de estoque e gera alertas"""

    def __init__(self, min_stock_threshold: int = 5):
        self.min_stock_threshold = min_stock_threshold

    def update(self, data: Dict[str, Any]) -> None | Dict[str, str]:
        """Processa atualizações de eventos relacionados ao estoque"""
        if "product" in data:
            product = data["product"]
            if product.stock <= self.min_stock_threshold:
                return {
                    "msg": f"ALERTA: Estoque baixo para '{product.name}'. Estoque atual: {product.stock} {product.unit}"
                }

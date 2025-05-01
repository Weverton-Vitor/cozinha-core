class Event:
    def __init__(self, name: str, payload: dict):
        self.name = name
        self.payload = payload

class ProductStockUpdatedEvent(Event):
    def __init__(self, product_id: str, new_stock: float):
        super().__init__("ProductStockUpdated", {
            "product_id": product_id,
            "new_stock": new_stock
        })

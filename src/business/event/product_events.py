class Event:
    def __init__(self, name: str, data: dict):
        self.name = name
        self.data = data

class ProductStockUpdatedEvent(Event):
    def __init__(self, product_id: str, new_stock: float):
        super().__init__("ProductStockUpdated", {
            "product_id": product_id,
            "new_stock": new_stock
        })

# Interface (base class) para ouvintes
class EventListener:
    def update(self, data: dict):
        raise NotImplementedError("Subclasses must implement 'update'")

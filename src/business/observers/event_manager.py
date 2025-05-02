from typing import Any, Dict, List
from business import observers
from business.decorators import singleton

@singleton
class EventManager:
    """Gerenciador de eventos que mantém os assinantes e os notifica quando eventos ocorrem"""

    def __init__(self):
        self._listeners: Dict[str, List[observers.EventListener]] = {}

    def subscribe(self, event_name: str, listener: observers.EventListener) -> None:
        """Adiciona um ouvinte para um evento específico"""
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(listener)

    def unsubscribe(self, event_name: str, listener: observers.EventListener) -> None:
        """Remove um ouvinte de um evento específico"""
        if event_name in self._listeners and listener in self._listeners[event_name]:
            self._listeners[event_name].remove(listener)

    def notify(self, event_name: str, data: Dict[str, Any]) -> None:
        """Notifica todos os ouvintes de um evento específico"""
        if event_name in self._listeners:
            for listener in self._listeners[event_name]:
                listener.update(data)

from abc import ABC, abstractmethod
from typing import Dict


class EventListener(ABC):
    """Interface para os ouvintes de eventos"""

    @abstractmethod
    def update(self, data: Dict[str, any]) -> None:
        """Método chamado quando um evento ocorre"""
        pass

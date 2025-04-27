from business import entities
from memento.order_memento import OrderMemento

class OrderCareTaker:
    __originator: entities.Order
    __history: list[OrderMemento]

    def __init__(self, originator: entities.Order):
        self.__originator = originator
        self.__history = []

    def get_originator(self):
        return self.__originator

    def backup(self):
        self.__history.append(self.get_originator().save_state())
    
    def undo(self):
        if not self.__history:
            return
        memento = self.__history.pop()
        self.get_originator().restore_state(memento)
        
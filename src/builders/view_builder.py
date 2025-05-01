from abc import ABC, abstractmethod

class IViewBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_controller(self):
        pass

    @abstractmethod
    def build_DAO(self):
        pass

    @abstractmethod
    def build_repository(self):
        pass

    @abstractmethod
    def build_service(self):
        pass

    @abstractmethod
    def build_validators(self):
        pass
   
    @abstractmethod
    def build_view(self):
        pass
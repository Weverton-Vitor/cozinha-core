from abc import ABC, abstractmethod


class LoggerAdapter(ABC):
    @abstractmethod
    def log_info(self, message: str):
        pass

    @abstractmethod
    def log_error(self, message: str):
        pass

    @abstractmethod
    def log_debug(self, message: str):
        pass

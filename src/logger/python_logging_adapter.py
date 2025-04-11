from business.decorators import singleton
import logger
import logging


@singleton
class PythonLoggerAdapter(logger.LoggerAdapter):
    def __init__(self):
        self.logger = logging
        logging.basicConfig(level=logging.DEBUG)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)
import logging

level = logging.INFO

logging.basicConfig(level=level, format="[%(levelname)s]: %(message)s")

class Logger:

    def log_error(self, message: str):
        logging.error(message)


    def log_info(self, message: str):
        logging.info(message)


    def log_warn(self, message: str):
        logging.warning(message)


    def log_dbg(self, message: str):
        logging.debug(message)

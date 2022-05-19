import logging

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)


def log_info(message):
    logging.info(message)


def log_debug(message):
    logging.debug(message)


def log_warning(message):
    logging.warning(message)


def log_error(message):
    logging.error(message)

import logging


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    if not logger.hasHandlers():
        logger.addHandler(ch)
    return logger


def log_error(logger, message):
    logger.error(message)


def log_info(logger, message):
    logger.info(message)


def log_warning(logger, message):
    logger.warning(message)
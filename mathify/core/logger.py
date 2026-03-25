import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_info(msg: str):
    logging.info(msg)

def log_error(msg: str):
    logging.error(msg)

def log_debug(msg: str):
    logging.debug(msg)
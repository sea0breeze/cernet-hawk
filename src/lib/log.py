# -*- coding: utf-8 -*-

import logging

from config import CONSOLE_PRINT
from config import LOG_FILE

logger = logging.getLogger("hawk_logger")

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(LOG_FILE)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(CONSOLE_PRINT)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


def cprint(msg, level="debug"):
    """
    use log to print and record variable
    level determine whether print or log
    level could be DEBUG, INFO, WARING, ERROR, CRITICAL

    by default, record all msg to log
    and when level >= CONSOLE_PRINT, will print
    CONSOLE_PRINT was defined in config.py

    :param msg: the val you want to print
    :param level: enum. the level of msg
    """
    if level == "debug":
        logger.debug(msg)
    elif level == "info":
        logger.info(msg)
    elif level == "warning":
        logger.warning(msg)
    elif level == "error":
        logger.error(msg)
    elif level == "critical":
        logger.critical(msg)
    else:
        raise Exception("Error log level")
    # print msg

# -*- coding: utf-8 -*-

import logging

from config import CONSOLE_PRINT
from config import LOG_FILE

class PRINT_LEVEL:
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


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


def cprint(msg, level=PRINT_LEVEL.DEBUG):
    """
    use log print variable
    :param msg: the val you want to print
    :param level: enum. the level of msg
    :param color: enum. the color of msg
    """
    if level == PRINT_LEVEL.DEBUG:
        logger.debug(msg)
    elif level == PRINT_LEVEL.INFO:
        logger.info(msg)
    elif level == PRINT_LEVEL.WARNING:
        logger.warning(msg)
    elif level == PRINT_LEVEL.ERROR:
        logger.error(msg)
    elif level == PRINT_LEVEL.CRITICAL:
        logger.critical(msg)

    #if level <= PRINT_LEVEL.WARNING:
    #    return

    #print msg



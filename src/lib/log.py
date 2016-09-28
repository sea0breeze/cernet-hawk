# -*- coding: utf-8 -*-

import logging

from enums import *


logger = logging.getLogger("hawk_logger")

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('data/log/test.log')

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)


def cout(msg, level=PRINT_LEVEL.DEBUG, color):
    """
    print variable
    :param msg: the val you want to print
    :param level: enum. the level of msg
    :param color: enum. the color of msg
    """
    if level == PRINT_LEVEL.DEBUG:
        logger.debug(msg)
    elif level == PRINT_LEVEL.INFO:
        logger.info(msg)
    elif level == PRINT_LEVEL.WARNING:
        logger.waring(msg)
    elif level == PRINT_LEVEL.ERROR:
        logger.error(msg)
    elif level == PRINT_LEVEL.CRITICAL:
        logger.critical(msg)

    if level <= PRINT_LEVEL.WARNING:
        return

    print msg



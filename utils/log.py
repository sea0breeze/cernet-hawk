#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

from config import CONSOLE_PRINT
from config import LOG_FILE
from config import disableColor

from color import colorizing_stream_handler

formatter_str = '[%(asctime)s] [%(levelname)s] %(message)s'
color_formatter_str = '[%(asctime)s] $CSI[%(levelname)s]$RESET %(message)s'

logger = logging.getLogger("hawk_logger")

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(LOG_FILE)
fh.setLevel(logging.DEBUG)

if disableColor:
    ch = logging.StreamHandler()
    chformatter = logging.Formatter(formatter_str)
else:
    ch = colorizing_stream_handler()
    chformatter = logging.Formatter(color_formatter_str)

ch.setLevel(CONSOLE_PRINT)

formatter = logging.Formatter(formatter_str)
fh.setFormatter(formatter)
ch.setFormatter(chformatter)

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

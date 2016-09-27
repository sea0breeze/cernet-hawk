# -*- coding: utf-8 -*-

import pickle
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


def save(val, identifier):
    """
    save variable into a file
    :param val: the val you want to save
    :param identifier: str. the identifier of variable
    :return: bool. status of save
    """
    try:
        output = open('data/pickle/' + identifier + '.pkl', 'wb')
        pickle.dump(val, output)
        output.close()
        return True
    except:
        return False


def get(identifier):
    """
    get variable from a file
    :param identifier: str. the identifier of variable
    :return: variable
    """
    pkl_file = open('data/pickle/' + name + '.pkl', 'rb')
    data = pickle.load(pkl_file)
    pkl_file.close()
    return data

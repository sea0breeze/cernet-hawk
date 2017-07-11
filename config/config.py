#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import time
import os

NMAP_CMD = ['-sS', '-Pn', '-sV', '-oX', '-']
ZMAP_CMD = ['-q','-v', '0', '-B', '2M']  # silent
PORTS = [80,
         21,
         22,
         25,
         443]

# only when cpint's level >= this level, will print
CONSOLE_PRINT = logging.DEBUG
# CONSOLE_PRINT = logging.INFO

APP_NAME = 'cernet-hawk'
APP_PATH = os.getcwd()
APP_PATH = APP_PATH[:APP_PATH.index(APP_NAME) + len(APP_NAME)]

# log file's path and name
LOG_FILE = APP_PATH + '/src/data/log/'
LOG_FILE += time.strftime('%Y-%m-%d', time.localtime(time.time()))
LOG_FILE += '.log'

PICKLE_PATH = APP_PATH + '/src/data/pickle/'
# PICKLE_PATH = '/usr/local/bin/pickle'

# disableColor = True
disableColor = False

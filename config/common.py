#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

from config.mode import mode


NMAP_CMD = ['-sS', '-Pn', '-sV', '-oX', '-']
ZMAP_CMD = ['-q', '-v', '0', '-B', '2M']  # silent
PORTS = [
    "21",
    "22",
    "25",
    "80",
    "443",
    "3306",
    "8080",
    "27017",
    "6379",
]


# only when cpint's level >= this level, will print
CONSOLE_PRINT = logging.DEBUG
# CONSOLE_PRINT = logging.INFO

# pause for dispatcher
pause = 60

if mode.isProduct():
    DEBUG = False
else:
    DEBUG = True

VERBOSE = False
VERBOSE = True

# if Offline is True, will run Event locally
Offline = False
if mode.isLocal():
    Offline = True
    # pause = 1

# module's timeout
TIMEOUT = 30

# disableColor = True
disableColor = False

# services should be handled
servicesShouldHandle = [
    "ssh",
    "smtp",
    "ftp",
    "http",
    "https",
    "telnet",
    "mongo",
    "mysql",
    "redis",
]

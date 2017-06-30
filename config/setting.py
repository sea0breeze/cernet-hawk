#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from config.mode import mode

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
    pause = 1

# module's timeout
TIMEOUT = 30

# task's runing limit
TIMELIIMIT = 4200
SOFTTIMELIIMIT = 3600
# how many task runs at a second
RATELIMIT = 100

# longest instance's time limit
INSTANCELIMIT = 86400  # = 3600 * 24

# one instance could only run 25 instance at a time
SINGERUNLIMIT = 25

# only 1000 running event at once
MAXRUNLIMIT = 3000

skipmodules = ["__init__"]
reversemodules = ["StoreDomain"]

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common.config.mode import mode

if mode.isProduct():
    backend = "amqp://pocer:gYu22h3RYU@10.31.130.29//"
    broker = "amqp://pocer:gYu22h3RYU@10.31.130.29//"
else:
    backend = "amqp://"
    broker = "amqp://"


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
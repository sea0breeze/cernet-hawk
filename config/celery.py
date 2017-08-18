#!/usr/bin/env python
# -*- coding:utf-8 -*-

from config.mode import mode

if mode.isProduct():
    backend = "amqp://"
    broker = "amqp://"
else:
    backend = "amqp://"
    broker = "amqp://"

flower = "http://localhost:5555/"
apitasks = flower + "api/tasks"

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

# ZMAP thread limit
ZMAPLIMIT = 5

# NMAP thread limit
NMAPLIMIT = 5

# Services thread limit
SERVICESLIMIT = 5
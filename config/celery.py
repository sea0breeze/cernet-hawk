#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common.config.mode import mode

if mode.isProduct():
    backend = "amqp://pocer:gYu22h3RYU@10.31.130.29//"
    broker = "amqp://pocer:gYu22h3RYU@10.31.130.29//"
else:
    backend = "amqp://"
    broker = "amqp://"

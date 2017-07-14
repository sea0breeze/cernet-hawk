#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import datetime


def now():
    # 返回当前时间
    return time.strftime('%Y-%m-%d %X', time.localtime(time.time()))


def today():
    # 返回今天的时间
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def nowdate():
    return datetime.datetime.now()


def timestr(shift=0):
    return time.strftime('%Y-%m-%d %X', time.localtime(time.time() + shift))


def pastTime(old, now=None):
    if now is None:
        now = datetime.datetime.now()
    return int((now - old).total_seconds())

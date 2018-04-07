#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os.path import join
from utils.mtime import timestr

# 各种字典和文件的默认目录配置

datapath = join(".", "data")
logpath = join(".", "logs")
modulepath = join(".", "services")

# ===== log =====

errorlogpath = join(logpath, "error.log")
commonlogpath = join(logpath, timestr()+".log")

dispatchpid = join(logpath, "dispatch.pid")
dispatchlog = join(logpath, "dispatch.log")

zmapprogress = join(logpath, "zmapProgress.log")
nmapprogress = join(logpath, "nmapprogress.log")

# ==== net =====

zmapconf = join(".", "config", "cernet.conf")
v6conf = join(".", "config", "cernetv6.conf")


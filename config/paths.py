#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os.path import join
from utils.time import timestr

# 各种字典和文件的默认目录配置

datapath = join(".", "data")
logpath = join(".", "logs")
modulepath = join(".", "modules")

# ===== log =====

errorlogpath = join(logpath, "error.log")
commonlogpath = join(logpath, timestr()+".log")


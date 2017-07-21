#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common import versioncheck

from celery import Celery
from config.common import DEBUG
from config.celery import *

from port.runzmap import ZmapScan
from port.runnmap import NmapScan

from services.ftp import ftpDetect

app = Celery('hawk', backend=backend, broker=broker)


app.tasks.register(ZmapScan)
app.tasks.register(NmapScan)
app.tasks.register(ftpDetect)

# servicesModules = getModules(modulepath)

# for module in modules:
# app.tasks.register(singleModuleInstance(module))

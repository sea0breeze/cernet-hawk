#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common import versioncheck

from celery import Celery
from config.common import DEBUG
from config.celery import *
from config.paths import modulepath

from common.core import getModules
from common.core import importModules

from port.runzmap import ZmapScan
from port.runnmap import NmapScan

modules = importModules(getModules(modulepath))
app = Celery('hawk', backend=backend, broker=broker)

app.tasks.register(ZmapScan)
app.tasks.register(NmapScan)

for module in modules:
    app.tasks.register(modules[module])

# servicesModules = getModules(modulepath)

# for module in modules:
# app.tasks.register(singleModuleInstance(module))

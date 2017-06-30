#!/usr/bin/env python
# -*- coding:utf-8 -*-

from celery import Celery

from utils.core import singleModuleInstance
from config.setting import DEBUG
from config.celery import *
from common.constant.paths import modulepath

app = Celery('pocer', backend=backend, broker=broker)

modules = getModules(modulepath)

for module in modules:
    app.tasks.register(singleModuleInstance(module))

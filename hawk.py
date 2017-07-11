#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def runcelery():

    app = Celery('pocer', backend=backend, broker=broker)

    modules = getModules(modulepath)

    for module in modules:
        app.tasks.register(singleModuleInstance(module))

def runDispatch(arg, dispatchpid, dispatchlog):
    if arg in ('start', 'stop', 'restart', 'run', 'single', 'init'):
        d = Dispatcher(dispatchpid, verbose=0, stdout=dispatchlog)
        getattr(d, arg)()
    else:
        print("Usage: python hawk.py dispatch [start|stop|restart]")


if __name__ == '__main__':
    if len(sys.argv) <= 1:

        from celery import Celery

        from utils.core import singleModuleInstance
        from config.setting import DEBUG
        from config.celery import *
        from common.constant.paths import modulepath

        runcelery()
    elif sys.argv[1] == "dispatch":

        from tasksrv.Dispatch import Dispatcher
        from common.constant.paths import dispatchpid
        from common.constant.paths import dispatchlog

        arg = sys.argv[2] if len(sys.argv) == 3 else ''
        runDispatch(arg)
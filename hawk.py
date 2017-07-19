#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

from common import versioncheck

def runcelery():

    app = Celery('hawk', backend=backend, broker=broker)
    from services.ftp import ftpDetect
    app.tasks.register(ftpDetect)
    # servicesModules = getModules(modulepath)

    # for module in modules:
        # app.tasks.register(singleModuleInstance(module))

def runDispatch(arg, dispatchpid, dispatchlog):
    if arg in ('start', 'stop', 'restart', 'run', 'single', 'init'):
        d = Dispatcher(dispatchpid, verbose=0, stdout=dispatchlog)
        getattr(d, arg)()
    else:
        print("Usage: python hawk.py dispatch [start|stop|restart]")


if __name__ == '__main__':
    if len(sys.argv) <= 1:

        from celery import Celery

        from config.common import DEBUG
        from config.celery import *

        runcelery()
    elif sys.argv[1] == "dispatch":

        from tasksrv.Dispatch import Dispatcher
        from common.constant.paths import dispatchpid
        from common.constant.paths import dispatchlog

        arg = sys.argv[2] if len(sys.argv) == 3 else ''
        runDispatch(arg)
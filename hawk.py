#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

from common import versioncheck


def runDispatch(arg, dispatchpid, dispatchlog):
    if arg in ('start', 'stop', 'restart', 'run', 'single', 'init'):
        d = Dispatcher(dispatchpid, verbose=0, stdout=dispatchlog)
        getattr(d, arg)()
    else:
        print("Usage: python hawk.py dispatch [start|stop|restart]")


if __name__ == '__main__':

    print sys.argv
    print sys.argc

    if sys.argc <= 1:
        # 这里因为作用域的问题不能写成函数
        from celery import Celery
        from config.common import DEBUG
        from config.celery import *
        from services.ftp import ftpDetect

        app = Celery('hawk', backend=backend, broker=broker)
        app.tasks.register(ftpDetect)

        # servicesModules = getModules(modulepath)

        # for module in modules:
        # app.tasks.register(singleModuleInstance(module))

    elif sys.argv[1] == "dispatch":

        from tasksrv.Dispatch import Dispatcher
        from common.constant.paths import dispatchpid
        from common.constant.paths import dispatchlog

        arg = sys.argv[2] if len(sys.argv) == 3 else ''
        runDispatch(arg)

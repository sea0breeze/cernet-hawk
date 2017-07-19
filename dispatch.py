#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

from common import versioncheck
from common.constant.paths import dispatchpid
from common.constant.paths import dispatchlog
from tasksrv.Dispatch import Dispatcher


if __name__ == '__main__':

    arg = sys.argv[2] if len(sys.argv) == 3 else ''
    if arg in ('start', 'stop', 'restart', 'run', 'single', 'init'):
        d = Dispatcher(dispatchpid, verbose=0, stdout=dispatchlog)
        getattr(d, arg)()
    else:
        print("Usage: python hawk.py dispatch [start|stop|restart]")


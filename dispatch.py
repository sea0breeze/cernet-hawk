#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

from common import versioncheck
from config.paths import dispatchpid
from config.paths import dispatchlog
from common.classes.Dispatch import Dispatcher


if __name__ == '__main__':

    arg = sys.argv[1] if len(sys.argv) == 2 else ''
    if arg in ('start', 'stop', 'restart', 'run', 'single', 'init'):
        d = Dispatcher(dispatchpid, verbose=0, stdout=dispatchlog)
        getattr(d, arg)()
    else:
        print("Usage: python hawk.py [start|stop|restart]")


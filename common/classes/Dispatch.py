#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import json

from config.common import pause
from config.common import DEBUG
from config.common import Offline

from config.path import zmapconf

from utils.time import now, pastTime

from thirdparty.daemon.daemon import Daemon


class Dispatcher(Daemon):

    def __init__(self, *args, **kwargs):
        super(Dispatcher, self).__init__(*args, **kwargs)

    def oneRound(self):
        pass

    def dispatchZmap(self):
        pass

    def run(self):
        self.init()
        while True:
            try:
                self.oneRound()
            except Exception as e:
                print("error occurs")
                errorlog(e)
            finally:
                if DEBUG:
                    print("[%s]: One round finish" % now())
                time.sleep(pause)

    def single(self):
        self.init()
        self.oneRound()

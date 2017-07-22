#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import json

from config.common import pause
from config.common import DEBUG
from config.common import Offline
from config.paths import zmapconf
from config.paths import zmapprogress

from utils.mtime import now, pastTime, unixtoday

from port.runzmap import ZmapScan
from port.runnmap import NmapScan

from thirdparty.daemon.daemon import Daemon


class Dispatcher(Daemon):

    def __init__(self, *args, **kwargs):
        super(Dispatcher, self).__init__(*args, **kwargs)

    def init(self):
        self.z = ZmapScan()
        self.n = NmapScan()

    def oneRound(self):
        self.dispatchZmap()

    def dispatchZmap(self):

        if os.path.exists(zmapprogress) \
                and (os.stat(zmapprogress).st_mtime > unixtoday()):
            line = int(open(zmapprogress).read().strip()) + 1
        else:
            line = 0
        zfile = open(zmapprogress, "w")
        zfile.write(str(line))
        zfile.close()

        nets = [i.strip('\n') for i in open(zmapconf)]
        if line >= len(nets):
            return False
        else:
            self.z.delay(nets[line])
            return True

    def run(self):
        self.init()
        while True:
            try:
                self.oneRound()
            except Exception as e:
                print("error occurs")
                # errorlog(e)
            finally:
                if DEBUG:
                    print("[%s]: One round finish" % now())
                time.sleep(pause)

    def single(self):
        self.init()
        self.oneRound()

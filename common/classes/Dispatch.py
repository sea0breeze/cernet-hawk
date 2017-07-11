#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import json

from config.setting import pause
from config.setting import DEBUG
from config.setting import Offline
from utils.time import now, pastTime

from thirdparty.daemon.daemon import Daemon


class Dispatcher(Daemon):

    def __init__(self, *args, **kwargs):
        super(Dispatcher, self).__init__(*args, **kwargs)

    def init(self):
        self.db = initDB()

    def oneRound(self):
        pass

    def run(self):
        self.init()
        while True:
            try:
                self.oneRound()
                self.db.commit()
            except Exception as e:
                # self.db.rollback()
                print("error occurs")
                errorlog(e)
            finally:
                if DEBUG:
                    print("[%s]: One round finish" % now())
                self.db.close()
                time.sleep(pause)

    def single(self):
        self.init()
        self.oneRound()
        self.db.commit()

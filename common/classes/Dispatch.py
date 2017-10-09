#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import json
import random

import requests

from config.celery import apitasks
from config.celery import ZMAPLIMIT, NMAPLIMIT, SERVICESLIMIT
from config.common import pause
from config.common import DEBUG
from config.common import Offline
from config.common import servicesShouldHandle
from config.paths import zmapconf
from config.paths import zmapprogress
from config.paths import modulepath

from common.core import getModules
from common.core import importModules

from utils.mtime import now, pastTime, unixtoday

from port.runzmap import ZmapScan
from port.runnmap import NmapScan

from orm.zmapinfo import ZmapInfo
from orm.nmapinfo import NmapInfo

from thirdparty.daemon.daemon import Daemon


class Dispatcher(Daemon):

    def __init__(self, *args, **kwargs):
        super(Dispatcher, self).__init__(*args, **kwargs)

    def init(self):
        self.z = ZmapScan()
        self.n = NmapScan()
        self.modules = getModules(modulepath)
        self.modulesMap = importModules(self.modules)

    def oneRound(self):
        self.dispatchZmap()
        self.dispatchNmap()
        self.dispatchServices()

    def dispatchNmap(self):
        tasks = json.loads(requests.get(apitasks).content)
        cnt = 0
        for task in tasks:
            tmp = tasks[task]
            if tmp["name"] == "nmapscan"\
                    and tmp["state"] == "STARTED":
                cnt += 1

        if cnt > NMAPLIMIT:
            return
        tasks = ZmapInfo.getTodayUndispathced()
        random.shuffle(tasks)
        for task in tasks:
            self.n.delay(task.ip, map(str, task.ports))
            ZmapInfo.objects(id=task.id).update(dispatched=True)
            cnt += 1
            if cnt > NMAPLIMIT:
                return
        return

    def dispatchZmap(self):
        tasks = json.loads(requests.get(apitasks).content)
        cnt = 0
        for task in tasks:
            tmp = tasks[task]
            if tmp["name"] == "zmapscan" \
                    and tmp["state"] == "STARTED":
                cnt += 1

        if cnt > ZMAPLIMIT:
            return

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

    def dispatchServices(self):
        tasks = json.loads(requests.get(apitasks).content)
        cnt = 0
        for task in tasks:
            tmp = tasks[task]
            if tmp["name"] != "nmapscan"\
                    and tmp["name"] != "zmapscan"\
                    and tmp["state"] == "STARTED":
                cnt += 1

        if cnt > SERVICESLIMIT:
            return
        tasks = NmapInfo.getTodayUndispathced()
        random.shuffle(tasks)
        for task in tasks:
            if task.name not in servicesShouldHandle:
                continue

            if task.name == "https":
                self.modulesMap["http"].delay(task.ip, task.port, True)
            else:
                self.modulesMap[task.name].delay(task.ip, task.port)
            NmapInfo.objects(id=task.id).update(dispatched=True)
            cnt += 1
            if cnt > SERVICESLIMIT:
                return
        return

    def run(self):
        self.init()
        while True:
            try:
                self.oneRound()
            except Exception as e:
                print("error occurs")
                print(e)
            finally:
                if DEBUG:
                    print("[%s]: One round finish" % now())
                time.sleep(pause)

    def single(self):
        self.init()
        self.oneRound()

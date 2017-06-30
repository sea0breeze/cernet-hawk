#!/usr/bin/env python
# -*- coding:utf-8 -*-

import inspect
import traceback
from random import randint
from time import sleep
from copy import deepcopy

from celery import Task

from common.core import initDB
from config.setting import DEBUG, VERBOSE
from config.setting import TIMEOUT
from config.setting import TIMELIIMIT, SOFTTIMELIIMIT
from config.setting import RATELIMIT


class Base(Task):

    def __init__(self):
        # name is important to use
        self.name = self.__class__.__name__
        self._db = None
        # can't run more than 1 hour
        self.time_limit = TIMELIIMIT
        self.soft_time_limit = SOFTTIMELIIMIT
        # limit 100 task on one hour
        self.rate_limit = RATELIMIT

    @property
    def db(self):
        if self._db is None:
            self._db = initDB()
        return self._db

    def on_success(self, retval, task_id, args, kwargs):
        self.db.commit()
        self.db.close()
        # raise Exception(json.dumps(args))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        try:
            self.db.commit()
        except Exception as e:
            print("error on on_failure:", str(e))
            self.db.rollback()
        finally:
            self.db.close()

    def on_retry(exc, task_id, args, kwargs, einfo):
        pass

    def randomSleep(self, mintime=4, maxtime=15):
        sleep(randint(mintime, maxtime))

    def verbose(self, msg):
        if not VERBOSE:
            return

        try:
            print(msg)
        except Exception as e:
            pass

    def debug(self, msg):
        if not DEBUG:
            return

        try:
            print(msg)
        except Exception as e:
            pass

    def info(self, guid, msg):
        self.db.commit()

    def error(self, guid, msg):
        self.db.commit()

    def test(self):
        # write test code here
        pass
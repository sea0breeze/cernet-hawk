#!/usr/bin/env python
# -*- coding:utf-8 -*-

from json import loads

import orm.db
from mongoengine import *
from utils.mtime import unixnow, unixtoday


class ZmapInfo(Document):

    """nmap"""

    ip = StringField(max_length=30, required=True)
    ports = ListField(required=True)
    generated = IntField(required=True, default=unixnow)
    dispatched = BooleanField(required=True, default=True)

    @classmethod
    def addWithJson(cls, jsStr):
        infos = loads(jsStr)
        for ip in infos.keys():
            zi = ZmapInfo()
            zi.ip = ip
            zi.ports = map(int, infos[ip])
            zi.save()
        return True

    @classmethod
    def getTodayCount(cls):
        return cls.objects(generated__gt=unixtoday()).count()

if __name__ == '__main__':
    s = '{"202.120.7.105": ["22"],"202.120.7.111": ["80", "22", "443"]}'
    ZmapInfo.addWithJson(s)

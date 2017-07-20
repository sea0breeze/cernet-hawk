#!/usr/bin/env python
# -*- coding:utf-8 -*-

from json import loads
from mongoengine import *
from utils.mtime import now


class ZmapInfo(Document):

    """nmap"""

    ip = StringField(max_length=30, required=True)
    ports = ListField(required=True)
    generated = DateTimeField(required=True, default=now)

    @classmethod
    def addWithJson(cls, jsStr):
        infos = loads(jsStr)
        for ip in infos.keys():
            zi = ZmapInfo()
            zi.ip = ip
            zi.ports = map(int, infos[ip])
            zi.save()
        return True

if __name__ == '__main__':
    s = '{"202.120.7.105": ["22"],"202.120.7.111": ["80", "22", "443"]}'
    ZmapInfo.addWithJson(s)

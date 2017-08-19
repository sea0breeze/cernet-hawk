#!/usr/bin/env python
# -*- coding:utf-8 -*-

from time import mktime

from json import loads

import orm.db
from mongoengine import *
from utils.mtime import unixnow, str2time, now, unixtoday


class NmapInfo(Document):

    """nmap"""

    ip = StringField(max_length=30, required=True)
    port = IntField(default=0, required=True)
    name = StringField(max_length=100, required=True)
    version = StringField(max_length=100, required=False)
    extrainfo = StringField(max_length=100, required=False)
    product = StringField(max_length=100, required=False)
    devicetype = StringField(max_length=100, required=False)
    ostype = StringField(max_length=100, required=False)
    generated = IntField(required=True, default=unixnow)
    dispatched = BooleanField(required=True, default=False)

    unrequires = ["name", "version", "extrainfo",
                  "product", "devicetype", "ostype"]

    @classmethod
    def getTodayUndispathced(cls):
        return cls.objects(
            generated__gt=unixtoday(), dispatched__ne=True
        )

    @classmethod
    def addWithJson(cls, jsStr):
        infos = loads(jsStr)
        ip = infos.keys()[0]
        infos = infos[ip]

        if infos is None:
            return

        for port in infos.keys():
            ni = cls()
            ni.ip = ip
            ni.port = port
            for k in cls.unrequires:
                if k in infos[port]:
                    setattr(ni, k, infos[port][k])
            ni.save()
        return True

    @classmethod
    def comp(cls, d=True):
        n = cls.objects()
        if d:
            t86 = str2time("2017-8-11")
            t87 = str2time("2017-8-12")
        else:
            t86 = str2time("2017-8-6")
            t87 = str2time("2017-8-7")
        n86 = set()
        n87 = set()
        for i in n:
            tmp = i.generated
            if tmp >= t86 and tmp < t87:
                n86.add((i.ip, i.port))
            elif tmp >= t87:
                n87.add((i.ip, i.port))
        return (n86 - n87), (n87 - n86)

    @classmethod
    def findByTime(cls, start, end):
        n = cls.objects()
        start = str2time(start)
        end = str2time(end)
        re = set()
        for i in n:
            tmp = i.generated
            if tmp >= start and tmp < end:
                re.add((i.ip, i.port))
        return re

if __name__ == '__main__':
    s = '{"202.120.7.149": {"80": {"version": "1.10.3 ", "extrainfo": "Ubuntu", "ostype": "Linux ", "name": "http ", "product": "nginx "}, "22": {"version": "7.2 p2 Ubuntu 4 ubuntu2.2 ", "extrainfo": "Ubuntu Linux;protocol 2.0 ", "ostype": "Linux ", "name": "ssh ", "product": "OpenSSH "}}}'
    NmapInfo.addWithJson(s)

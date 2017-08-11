#!/usr/bin/env python
# -*- coding:utf-8 -*-

from json import loads

import orm.db
from mongoengine import *
from utils.mtime import unixnow, unixtoday, str2time, time2str


class ZmapInfo(Document):

    """nmap"""

    ip = StringField(max_length=30, required=True)
    ports = ListField(required=True)
    generated = IntField(required=True, default=unixnow)
    dispatched = BooleanField(required=True, default=False)

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

    @classmethod
    def getTodayUndispathced(cls):
        return cls.objects(
            generated__gt=unixtoday(), dispatched__ne=True
        )

    @classmethod
    def comp(cls, comport):
        n = cls.objects()
        t86 = int(str2time("2017-8-6"))
        t87 = int(str2time("2017-8-7"))
        n86 = set()
        n87 = set()
        for i in n:
            tmp = i.generated
            print time2str(i.generated)
            # ports = list(set(i.ports))
            # ports.sort()
            # ports = ",".join(map(str,ports))
            # if comport in i.ports:
                # ports = comport
            # else:
                # continue

            if tmp >= t86 and tmp < t87:
                n86.add(i.ip)
            elif tmp >= t87:
                n87.add(i.ip)
        print len(n86)
        print len(n87)
        print len(n86 - n87)
        print len(n87 - n86)

if __name__ == '__main__':
    s = '{"202.120.7.105": ["22"],"202.120.7.111": ["80", "22", "443"]}'
    ZmapInfo.addWithJson(s)

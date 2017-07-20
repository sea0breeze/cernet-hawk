#!/usr/bin/env python
# -*- coding:utf-8 -*-

from json import loads

from mongoengine import *
from utils.mtime import now
import orm.db


class NmapInfo(Document):

    """nmap"""

    ip = StringField(max_length=30, required=True)
    port = IntField(default=0, required=True)
    name = StringField(max_length=30, required=True)
    version = StringField(max_length=30, required=False)
    extrainfo = StringField(max_length=30, required=False)
    product = StringField(max_length=30, required=False)
    devicetype = StringField(max_length=30, required=False)
    ostype = StringField(max_length=30, required=False)
    generated = DateTimeField(required=True, default=now)

    unrequires = ["name", "version", "extrainfo",
                  "product", "devicetype", "ostype"]

    @classmethod
    def addWithJson(cls, jsStr):
        infos = loads(jsStr)
        ip = infos.keys()[0]
        infos = infos[ip]
        for port in infos.keys():
            ni = cls()
            ni.ip = ip
            ni.port = port
            for k in cls.unrequires:
                if k in infos[port]:
                    setattr(ni, k, infos[port][k])
            ni.save()
        return True

if __name__ == '__main__':
    s = '{"202.120.7.149": {"80": {"version": "1.10.3 ", "extrainfo": "Ubuntu", "ostype": "Linux ", "name": "http ", "product": "nginx "}, "22": {"version": "7.2 p2 Ubuntu 4 ubuntu2.2 ", "extrainfo": "Ubuntu Linux;protocol 2.0 ", "ostype": "Linux ", "name": "ssh ", "product": "OpenSSH "}}}'
    NmapInfo.addWithJson(s)

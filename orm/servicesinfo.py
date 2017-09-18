#!/usr/bin/env python
# -*- coding:utf-8 -*-

import orm.db
from mongoengine import *


class ServicesInfo(Document):

    ip = StringField(max_length=30, required=True)
    port = IntField(default=0, required=True)
    name = StringField(max_length=30, required=True)
    banner = DictField(required=True)

    @classmethod
    def add(cls, ip, port, name, banner):
        ni = cls()
        ni.ip = ip
        ni.port = port
        ni.name = name
        ni.banner = banner
        ni.save()
        return True

    @classmethod
    def searchByName(cls, name):
        return cls.objects(name=name)

    @classmethod
    def searchByPort(cls, port):
        return cls.objects(port=port)

    @classmethod
    def searchByIP(cls, ip):
        return cls.objects(ip=ip)

    @classmethod
    def getDetailByIP(cls, ip):
        return cls.objects(ip=ip)

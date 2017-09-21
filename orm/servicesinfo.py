#!/usr/bin/env python
# -*- coding:utf-8 -*-

import orm.db
from mongoengine import *
from utils.ipaddr import iplookup, ip2domain


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
        objs = cls.objects(name=name)
        res = {}
        for obj in objs:
            if obj.ip in res:
                tmp = "%s/%s" % (obj.name, obj.port)
                if tmp not in res[obj.ip]["services"]:
                    res[obj.ip]["services"].append(tmp)
            else:
                tmp = {}
                tmp["ip"] = obj.ip
                tmp["addr"] = iplookup(obj.ip)
                tmp["domain"] = ip2domain(obj.ip)
                tmp["os"] = ""
                tmp["services"] = ["%s/%s" % (obj.name, obj.port)]
                res[obj.ip] = tmp

        return res.values()

    @classmethod
    def searchByPort(cls, port):
        objs = cls.objects(port=port)
        res = {}
        for obj in objs:
            if obj.ip in res:
                tmp = "%s/%s" % (obj.name, obj.port)
                if tmp not in res[obj.ip]["services"]:
                    res[obj.ip]["services"].append(tmp)
            else:
                tmp = {}
                tmp["ip"] = obj.ip
                tmp["addr"] = iplookup(obj.ip)
                tmp["domain"] = ip2domain(obj.ip)
                tmp["os"] = ""
                tmp["services"] = ["%s/%s" % (obj.name, obj.port)]
                res[obj.ip] = tmp

        return res.values()

    @classmethod
    def searchByIP(cls, ip):
        objs = cls.objects(ip=ip)
        res = {}
        res["ip"] = ip
        res["addr"] = iplookup(ip)
        res["domain"] = ip2domain(ip)
        res["os"] = ""
        res["services"] = set()
        for obj in objs:
            res["services"].add("%s/%s" % (obj.name, obj.port))
        # remove duplication
        res["services"] = list(res["services"])
        return [res]

    @classmethod
    def getDetailByIP(cls, ip):
        objs = cls.objects(ip=ip)
        res = []
        for obj in objs:
            res.append({
                "ip": obj.ip,
                "name": obj.name,
                "banner": obj.banner
            })
        return res

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import tornado.web
from server.controller.base import BaseHandler
from orm.servicesinfo import ServicesInfo


class MainHandler(BaseHandler):

    def get(self):
        with open(os.path.join("server", "static", "index.html"), "r") as f:
            self.write(f.read())


class SearchHandler(BaseHandler):

    def get(self, searchStr):
        t = searchStr.split("=")
        if len(t) != 2:
            return self.error(500, "illegal search str")
        elif t[0] not in ["ip", "services", "port"]:
            return self.error(500, "not support")

        if t[0] == "ip":
            return self.ok(ServicesInfo.searchByIP(t[1]))
        elif t[0] == "services":
            return self.ok(ServicesInfo.searchByName(t[1]))
        elif t[0] == "port":
            return self.ok(ServicesInfo.searchByPort(t[1]))


class IPHandler(BaseHandler):

    def get(self, ip):
        return self.ok(ServicesInfo.getDetailByIP(ip))

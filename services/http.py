#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common.classes.PortBase import PortBase
from orm.servicesinfo import ServicesInfo
from thirdparty.Wappalyzer.Wappalyzer import WebPage


class httpDetect(PortBase):

    def __init__(self):
        # init at here
        super(httpDetect, self).__init__()
        self.name = "httpDetect"

    def run(self, ip, port=80, ishttps=False):
        # WebPage
        port = int(port)
        if ishttps:
            url = "https://" + ip
            if port != 443:
                url += ":" + str(port)
        else:
            url = "http://" + ip
            if port != 80:
                url += ":" + str(port)
        webinfo = WebPage(url).info()
        ServicesInfo.add(ip, port, ["http", "https"][int(ishttps)], webinfo)

if __name__ == '__main__':
    h = httpDetect("localhost")
    h.pprint()

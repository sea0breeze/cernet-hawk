#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import gethostbyaddr

from requests import get

from common.classes.PortBase import PortBase


class httpDetect(PortBase):

    def __init__(self):
        # init at here
        super(httpDetect, self).__init__()
        self.name = "httpDetect"

    def run(self, ip, port=80):
        try:
            self.data.headers = r.headers
            self.data.status_code = r.status_code
            self.data.screenshoot = r.content
        except Exception, e:
            cprint("Connection Error: %s\nException: %s" % (ip, e), "error")
            return

        try:
            self.data.url = gethostbyaddr(ip)[0]
        except Exception, e:
            cprint('Host not found: %s\nException: %s' % (ip, e))

        if hasattr(self.data, 'url'):
            try:
                self.data.whois = whois(self.data.url).text
            except Exception, e:
                cprint('Whois not found: %s\nException: %s' %
                       (self.data.url, e))

if __name__ == '__main__':
    h = httpDetect("localhost")
    h.pprint()

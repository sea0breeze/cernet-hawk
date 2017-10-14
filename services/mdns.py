#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

import dns.query
import dns.zone
import dns.resolver

from common.classes.PortBase import PortBase


class mdnsDetect(PortBase):

    '''
    dns will conflict with python dns library
    '''

    def __init__(self):
        super(dnsDetect, self).__init__()
        self.name = "dnsDetect"

    def run(self, ip, port=53, timeout=2):
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(50).strip('\r\n').split(' ')
            print banner
        except Exception as e:
            # cprint(str(e), 'error')
            print(str(e), 'error')
            # tn.close()
        finally:
            s.close()

    def testDNSzonetrans(self, domain):
        result = ""
        NS = dns.resolver.query(domain, 'NS')
        nameservers = []
        for i in NS.response.answer:
            for j in i.items:
                nameservers.append(j.to_text())

        for nameserver in nameservers:

            try:
                z = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))
                names = sorted(z.nodes)

                for n in names:
                    tmpdomain = str(n) + "." + domain
                    result += z[n].to_text(n) + "\n"
            except dns.exception.FormError as e:
                pass
        return result

if __name__ == '__main__':
    dnsDetect = dnsDetect("114.114.114.114")

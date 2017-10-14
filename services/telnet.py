#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
refer:
    http://www.cnblogs.com/dazhaxie/archive/2012/06/27/2566054.html
    ref 854 855
'''
import socket

from utils.log import cprint
from common.classes.PortBase import PortBase
from orm.servicesinfo import ServicesInfo


class telnetDetect(PortBase):

    '''
    Telnet Detection.

    '''

    def __init__(self):
        super(telnetDetect, self).__init__()
        self.name = "telnetDetect"

    def run(self, ip, port=23):
        try:
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(1024)
            if banner.endswith('login: '):
                banner = banner[:-7]
            self.data.banner = repr(banner)
            ServicesInfo.add(ip, port, 'telnet', self.data)
        except Exception as e:
            cprint(str(e), 'error')
            return None
        finally:
            s.close()
            self.clear()

        return True

if __name__ == '__main__':
    telnetTest = telnetDetect("0.0.0.0")

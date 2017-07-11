#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

from common.classes.PortBase import PortBase


class dnsDetect(PortBase):

    '''
    :str. banner
    :

    '''
    # not complete yet

    def __init__(self):
        super(dnsDetect, self).__init__()
    
    def run(self, ip, port = 53, timeout = 2):
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

if __name__ == '__main__':
    dnsDetect = dnsDetect("114.114.114.114")

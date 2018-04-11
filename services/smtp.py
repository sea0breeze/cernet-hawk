#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
refer:
'''

import socket
import ssl
from utils.log import cprint
from utils.cert import parse_der
from common.classes.PortBase import PortBase
from orm.servicesinfo import ServicesInfo


class smtpDetect(PortBase):

    '''
    SMTP Detection.

    '''

    def __init__(self):
        super(smtpDetect, self).__init__()
        self.name = "smtpDetect"

    def run(self, ip, port=25):
        try:
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(1024).rstrip('\r\n')
            if banner[:3] == '220':
                self.data.banner = banner[4:]
            s.send('EHLO test\n')
            ehlo = s.recv(1024).replace('\r', '').rstrip().split('\n')[1:]
            self.data.ehlo = map(lambda x: x[4:], ehlo)
        except Exception as e:
            cprint(str(e), 'error')
            self.clear()
            return None

        if 'STARTTLS' in self.data.ehlo:
            try:
                s.send("STARTTLS\n")
                resp = s.recv(1024)
                if resp[:3] == '220':
                    ss = ssl.wrap_socket(s)
                    cert = ss.getpeercert(True)
                    self.data.update(parse_der(cert))
            except Exception as e:
                cprint(str(e), 'error')
                self.clear()
                return None
            finally:
                s.close()

        ServicesInfo.add(ip, port, 'smtp', self.data)
        self.clear()
        return True

if __name__ == '__main__':
    Test = smtpDetect("202.120.40.90")

#!/usr/bin/env python
# coding=utf-8

import ssl
import socket

from utils.log import cprint
from utils.cert import parse_der
from common.classes.PortBase import PortBase
from orm.servicesinfo import ServicesInfo


class pop3Detect(PortBase):
    '''
    POP3 Detection.
    '''

    def __init__(self):
        super(pop3Detect, self).__init__()
        self.name = "pop3Detect"

    def run(self, ip, port=110):
        try:
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(1024).rstrip('\r\n')
            self.data.banner = banner
            if banner.startswith('+OK'):
                s.send('CAPA\r\n')
                capa = s.recv(1024).split('\r\n')[1:-2]
                self.data.capability_list = capa
        except Exception as e:
            cprint(str(e), 'error')
            self.clear()
            return None

        if 'STLS' in self.data.capability_list:
            try:
                s.send("STLS\r\n")
                resp = s.recv(1024)
                if resp[:3] == '+OK':
                    ss = ssl.wrap_socket(s)
                    cert = ss.getpeercert(True)
                    self.data.update(parse_der(cert))
            except Exception as e:
                cprint(str(e), 'error')
                self.clear()
                return None

        s.close()
        # from pprint import pprint
        # pprint(self.data)
        ServicesInfo.add(ip, port, 'pop3', self.data)
        self.clear()
        return True

#!/usr/bin/env python
# coding=utf-8

import ssl
import socket

from utils.log import cprint
from utils.cert import parse_der
from common.classes.PortBase import PortBase
from orm.servicesinfo import ServicesInfo


class imapDetect(PortBase):
    '''
    imap Detection.
    '''

    def __init__(self):
        super(imapDetect, self).__init__()
        self.name = "imapDetect"

    def run(self, ip, port=143):
        try:
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(1024).rstrip('\r\n')
            self.data.banner = banner
            if banner.startswith('* OK'):
                s.send('A1 CAPABILITY\r\n')
                capa = s.recv(1024).split('\r\n')[0]
                self.data.capability_list = capa
        except Exception as e:
            cprint(str(e), 'error')
            self.clear()
            return None

        if 'ID ' in self.data.capability_list:
            try:
                s.send('A2 ID ("test" "test")\r\n')
                resp = s.recv(1024)
                mid = resp[6:resp.index(')')].split()
                iddict = {}
                for i in range(0, len(mid), 2):
                    iddict[mid[i].strip('"')] = mid[i+1].strip('"')
                self.data.id = iddict
            except Exception as e:
                cprint(str(e), 'error')
                self.clear()
                return None

        if 'STARTTLS' in self.data.capability_list:
            try:
                s.send("A3 STARTTLS\r\n")
                resp = s.recv(1024)
                if resp[:5] == 'A3 OK':
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
        ServicesInfo.add(ip, port, 'imap', self.data)
        self.clear()
        return True

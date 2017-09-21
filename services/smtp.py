#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
refer:
'''

import smtplib
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
    # not complete yet

    def __init__(self):
        super(smtpDetect, self).__init__()
        self.name = "smtpDetect"

    def run(self, ip, port=25):
        try:
            server = smtplib.SMTP()
            self.data.banner = server.connect(ip, str(port))[1]
            self.data.ehlo = server.ehlo()[1].split('\n')
        except Exception as e:
            cprint(str(e), 'error')
            self.clear()
            return None
        finally:
            server.quit()

        if 'STARTTLS' in self.data.ehlo:
            try:
                s = socket.socket()
                s.connect((ip, port))
                s.recv(1024)
                s.send("STARTTLS\n")
                print s.recv(1024)
                ss = ssl.wrap_socket(s)
                cert = ss.getpeercert(True)
                self.data.update(parse_der(cert))
            except Exception as e:
                cprint(str(e), 'error')
                self.clear()
                return None
            finally:
                ss.close()

        ServicesInfo.add(ip, port, 'smtp', self.data)
        self.clear()
        return True

if __name__ == '__main__':
    Test = smtpDetect("202.120.40.90")

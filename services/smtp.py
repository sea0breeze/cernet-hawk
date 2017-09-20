#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
refer:
'''

import smtplib
from lib.log import cprint
from common.classes.PortBase import PortBase
from orm.servicesinfo import ServicesInfo


class smtpDetect(PortBase):

    '''
    :str. banner
    :

    '''
    # not complete yet

    def __init__(self):
        super(smtpDetect, self).__init__()
        self.name = "smtpDetect"

    def run(self, ip, port=25):
        # not complete yet
        try:
            server = smtplib.SMTP()
            self.data.banner = server.connect(ip, str(port))[1]
            self.data.ehlo = server.ehlo().split('\n')
        except Exception as e:
            cprint(str(e), 'error')
            return None
        server.quit()
        ServicesInfo.add(ip, port, 'smtp', self.data)
        self.clear()
        return True

if __name__ == '__main__':
    Test = smtpDetect("202.120.40.90")

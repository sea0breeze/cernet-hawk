#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
refer:
'''

import smtplib
# from lib.log import cprint
from common.classes.PortBase import PortBase


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
            server.connect(ip, str(port), 'smtp')
        except Exception as e:
            # cprint(str(e), 'error')
            # print(str(e), 'error')
            server.quit()
        finally:
            return

if __name__ == '__main__':
    Test = smtpDetect("0.0.0.0")

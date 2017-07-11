#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ftplib import FTP

from common.classes.PortBase import PortBase


class ftpDetect(PortBase):

    def __init__(self):
        super(ftpDetect, self).__init__()

    def run(self, ip, port=53, timeout=2):
        # cprint("msg","info")
        try:
            if port != 21:
                ip += ':' + str(port)

            ftp = FTP()
            ftp.connect(ip, port, timeout=timeout)

            self.data.banner = ftp.getwelcome()

            ftp.login()
            self.data.anonymous = True

            flist = []
            ftp.retrlines('LIST', lambda i: flist.append(i))
            self.data.flist = flist
            ftp.quit()

        except Exception, e:
            self.data.exception = str(e)


if __name__ == '__main__':
    ftpDetect("public.sjtu.edu.cn", 21).pprint()
    ftpDetect("localhost", 21).pprint()
    ftpDetect("ftp.sjtu.edu.cn").pprint()
    while False:
        try:
            print ">>>",
            print ftpDetect(raw_input(), 21)
        except:
            break

#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
refer:
    http://www.cnblogs.com/dazhaxie/archive/2012/06/27/2566054.html
    ref 854 855
'''

import telnetlib


class telnetDetect:

    '''
    :str. banner
    :

    '''
    # not complete yet

    def __init__(self):
        pass

    def run(self, ip, port=53):
        # not complete yet
        try:
            tn = telnetlib.Telnet(host=ip, port=port, 'telnet')
        except Exception as e:
            # cprint(str(e), 'error')
            tn.close()
        finally:
            return

if __name__ == '__main__':
    telnetTest = telnetDetect("0.0.0.0")

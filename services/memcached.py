#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common.classes.PortBase import PortBase

from lib.log import cprint

class memcachedDetect(PortBase):

    def __init__(self):
        pass

    def run(self, ip, port):

        try:
            return True
        except Exception as e:
            return False

if __name__ == '__main__':
    pass

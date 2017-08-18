#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common.classes.PortBase import PortBase


class memcachedDetect(PortBase):

    def __init__(self):
        super(memcachedDetect, self).__init__()
        self.name = "memcachedDetect"

    def run(self, ip, port):

        try:
            return True
        except Exception as e:
            return False

if __name__ == '__main__':
    pass

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# refer:
# mongo could login without password if not config well
# this mongo code is not complete
# http://blog.itpub.net/26250550/viewspace-1364758/

import pymongo
from common.classes.PortBase import PortBase

class mongoDetect(PortBase):

    def __init__(self):
        super(mongoDetect, self).__init__()
        self.name = "mongoDetect"

    def run(self, ip, port = 27017):

        try:
            conn = pymongo.MongoClient(ip, port, 'mongo')
            dbname = conn.database_names()
            ServicesInfo.add(ip, port, 'mongo', {"vuln":"null pwd"})
            return True
        except Exception as e:
            return False

if __name__ == '__main__':
    pass

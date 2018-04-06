#!/usr/bin/env python
# -*- coding:utf-8 -*-

# this redis code is not complete
# redis could be hacked if not config well
# http://www.oschina.net/news/67975/redis-defect?from=mail-notify

import redis

from common.classes.PortBase import PortBase

class redisDetect(PortBase):

    def __init__(self):
        super(redisDetect, self).__init__()
        self.name = "redisDetect"
        
    def run(self, ip, port=6379, timeout=2):

        try:
            r = redis.StrictRedis(host=host, port=6379, db=0)
            self.data.config = r.config_get()
            ServicesInfo.add(ip, port, 'redis', self.data)
        except Exception, e:
            self.data.exception = e

if __name__ == '__main__':
    pass

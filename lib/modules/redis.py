# this redis code is not complete
# redis could be hacked if not config well
# http://www.oschina.net/news/67975/redis-defect?from=mail-notify

import redis

from Detect import Detect

class redisDetect(Detect):

    def __init__(self, ip, port=6379, timeout=2):

        super(redisDetect, self).__init__(ip, port, 'redis')

        try:
            r = redis.StrictRedis(host=host, port=6379, db=0)
            self.data.config = r.config_get()
        except Exception, e:
            self.data.exception = e

if __name__ == '__main__':
    pass

import redis

def redisDetect(host, port=6379):
    # this redis code is not complete
    # redis could be hacked if not config well
    # http://www.oschina.net/news/67975/redis-defect?from=mail-notify
    try:
        r = redis.StrictRedis(host=host, port=6379, db=0)
        return r.config_get()
    except Exception, e:
        print e
        return

if __name__ == '__main__':
    pass
import redis

def redisDetect(host, port=6379)
    try:
        r = redis.StrictRedis(host=host, port=6379, db=0)
        return r.config_get()
    except Exception, e:
        print e
        return

if __name__ == '__main__':
    pass
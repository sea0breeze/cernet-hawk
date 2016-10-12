import pymongo


def mongo_detect(host, port = 27017):
    # mongo could login without password if not config well
    # this mongo code is not complete
    # http://blog.itpub.net/26250550/viewspace-1364758/
    try:
        conn = pymongo.MongoClient(ip_addr, port)
        dbname = conn.database_names()
        return True
    except Exception as e:
        return False

if __name__ == '__main__':
    pass

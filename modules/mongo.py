# refer:
# mongo could login without password if not config well
# this mongo code is not complete
# http://blog.itpub.net/26250550/viewspace-1364758/

import pymongo

class mongoDetect(Detect):

    def __init__(self, ip, port = 27017):

        try:
            conn = pymongo.MongoClient(ip, port, 'mongo')
            dbname = conn.database_names()
            return True
        except Exception as e:
            return False

if __name__ == '__main__':
    pass
from pymongo import MongoClient

class Mongo(object):
    """
    MongoDB Client
    """
    def __init__(self, table):
        super(Mongo, self).__init__()
        self.conn = MongoClient('localhost')
        self.col = self.conn.hawk[table]

    def insert(self, data):
        self.col.insert(data)

    def find(self, index):
        self.col.find(index)

if __name__ == '__main__':
    m = Mongo('ftp')
    m.insert({'datajson': 'test'})
    print m.find({})


from pymongo import MongoClient
import json

class Mongo(object):
    """
    MongoDB Client
    """
    def __init__(self):
        super(Mongo, self).__init__()
        self.conn = MongoClient('localhost')
        self.col = conn.hawk.table

    def insert(self, data):
        self.col.insert(data)

    def find(self, index):
        self.col.find(index)

if __name__ == '__main__':
    m = Mongo()
    m.insert({'data.json': 'test'})
    m.find('url')


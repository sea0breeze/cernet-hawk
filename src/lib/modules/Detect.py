from pprint import pprint
from attrDict import AttribDict

from lib.schema.mongo import Mongo

class Detect(object):
    """
    base class of Detect
    """
    def __init__(self, ip, port, type):
        self.data = AttribDict()
        self.data.ip = ip
        self.data.port = port
        self.type = type

    def pprint(self, stream=None, indent=1, width=80, depth=None):
        pprint(self.data, stream, indent, width, depth)

    def save(self):
        if self.db is None:
            self.db = Mongo(type)
        self.db.insert(self.data) 
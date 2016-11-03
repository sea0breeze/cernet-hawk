from pprint import pprint
from attrDict import AttribDict

class Detect(object):
    """
    base class of Detect
    """
    def __init__(self, ip, port, timeout = 2):
        self.data = AttribDict()
        self.data.ip = ip
        self.data.port = port

    def pprint(self, stream=None, indent=1, width=80, depth=None):
        pprint(self.data, stream, indent, width, depth)
        
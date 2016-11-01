from attrDict import AttribDict

class Detect(object):
    """
    base class of Detect
    """
    def __init__(self, ip, port, timeout = 2):
        self.data = AttribDict()
        self.data.ip = ip
        self.data.port = port
        
from attrDict import attrDict

class Detect(object):
    """
    base class of Detect
    """
    def __init__(self, ip, port):
        self.data = attrDict()
        self.data['ip'] = ip
        self.data['port'] = port
        
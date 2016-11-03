# refer:

from Detect import Detect

from lib.log import cprint

class memcachedDetect(Detect):

    def __init__(self, ip, port):
        try:
            return True
        except Exception as e:
            return False

if __name__ == '__main__':
    pass

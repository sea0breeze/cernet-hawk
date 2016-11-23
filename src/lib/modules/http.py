from requests import get

from lib.utils.utils import parseUrl
from Detect import Detect

class httpDetect(Detect):

    def __init__(self, ip, port = 80):
        # init at here
        super(httpDetect, self).__init__(ip, port, 'http')
        self.data.headers = get(parseUrl(ip)).headers

if __name__ == '__main__':
    h = httpDetect("localhost")
    h.pprint()


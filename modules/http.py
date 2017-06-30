from socket import gethostbyaddr

from requests import get
from whois import whois

from lib.utils.utils import parseUrl
from lib.scan.log import cprint
from common.classes.PortBase import PortBase


class httpDetect(PortBase):

    def __init__(self, ip, port=80):
        # init at here
        super(httpDetect, self).__init__(ip, port, 'http')

        try:
            r = get(parseUrl(ip))
            self.data.headers = r.headers
            self.data.status_code = r.status_code
            self.data.screenshoot = r.content
        except Exception, e:
            cprint("Connection Error: %s\nException: %s" % (ip, e), "error")
            return

        try:
            self.data.url = gethostbyaddr(ip)[0]
        except Exception, e:
            cprint('Host not found: %s\nException: %s' % (ip, e))

        if hasattr(self.data, 'url'):
            try:
                self.data.whois = whois(self.data.url).text
            except Exception, e:
                cprint('Whois not found: %s\nException: %s' %
                       (self.data.url, e))

if __name__ == '__main__':
    h = httpDetect("localhost")
    h.pprint()

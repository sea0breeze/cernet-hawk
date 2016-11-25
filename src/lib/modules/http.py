from socket import gethostbyaddr

from requests import get
from whois import whois

from lib.utils.utils import parseUrl
from lib.scan.log import cprint
from Detect import Detect

class httpDetect(Detect):

    def __init__(self, ip, port = 80):
        # init at here
        super(httpDetect, self).__init__(ip, port, 'http')
        
        try:
            r = get(parseUrl(ip))
            self.data.headers = r.headers
            self.data.status_code = r.status_code
            self.data.screenshoot = r.content
        except:
            cprint("Connection Error: %s" % ip, "error")
            return
        
        try:
            self.data.url = gethostbyaddr(ip)[0]
        except:
            cprint('Host not found: %s' % ip)

        if hasattr(self.data, 'url'):
            try:
                self.data.whois = whois(self.data.url).text
            except:
                cprint('Whois not found: %s' % self.data.url)            

if __name__ == '__main__':
    h = httpDetect("localhost")
    h.pprint()


import socket

from Detect import Detect
# from lib.log import cprint


class dnsDetect(Detect):

    '''
    :str. banner
    :

    '''
    # not complete yet

    def __init__(self, ip, port = 53, timeout = 2):
        super(dnsDetect, self).__init__(ip, port)
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(50).strip('\r\n').split(' ')
            print banner
        except Exception as e:
            # cprint(str(e), 'error')
            print(str(e), 'error')
            # tn.close()
        finally:
            s.close()

if __name__ == '__main__':
    dnsDetect = dnsDetect("114.114.114.114")

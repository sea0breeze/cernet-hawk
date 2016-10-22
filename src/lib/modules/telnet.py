'''
refer:
    http://www.cnblogs.com/dazhaxie/archive/2012/06/27/2566054.html
    ref 854 855
'''

import telnetlib
# from lib.log import cprint


class telnetDetect:

    '''
    :str. banner
    :

    '''
    # not complete yet

    def __init__(self, ip, port=53):
        # not complete yet
        try:
            tn = telnetlib.Telnet(host=ip, port=port)
        except Exception as e:
            # cprint(str(e), 'error')
            # print(str(e), 'error')
            tn.close()
        finally:
            return

if __name__ == '__main__':
    telnetTest = telnetDetect("0.0.0.0")

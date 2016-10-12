from ftplib import FTP

from lib.log import cprint

def ftp_detect(host, port=21, timeout=5):
    # cprint("msg","info")
    try:
        ret = {}
        ret['host'] = host

        if port != 21:
            ret['host'] += ':' + str(port)

        ftp = FTP()
        ftp.connect(host, port, timeout=timeout)

        ret['banner'] = ftp.getwelcome()

        ftp.login()
        ret['anonymous'] = True

        flist = []
        ftp.retrlines('LIST', lambda i: flist.append(i))
        ret['flist'] = flist
        ftp.quit()

    except Exception, e:
        ret['exception'] = e

    finally:
        return ret

if __name__ == '__main__':
    print ftpDetect("public.sjtu.edu.cn", 21)
    print ftpDetect("localhost", 21)
    print ftpDetect("ftp.sjtu.edu.cn")
    while False:
        try:
            print ">>>",
            print ftpDetect(raw_input(), 21)
        except:
            break

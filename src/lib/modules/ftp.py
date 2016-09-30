from ftplib import FTP


def ftpDetect(host, port=21, timeout=5):
    try:
        ret = {}
        ftp = FTP()
        ftp.connect(host, port, timeout=timeout)

        ret['banner'] = ftp.getwelcome()

        ftp.login()
        ret['anonymous'] = True

        flist = []
        ftp.retrlines('LIST', lambda i: flist.append(i))
        ret['flist'] = flist

    except Exception, e:
        ret['exception'] = e

    finally:
        ftp.quit()
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

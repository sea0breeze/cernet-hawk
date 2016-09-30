from ftplib import FTP

def retBanner(ip, port):
    try:
        ftp = FTP()
        ftp.connect(ip, port)
        banner = ftp.getwelcome()
        ftp.quit()
        return banner
    except:
        return

if __name__ == '__main__':
    print retBanner("public.sjtu.edu.cn", 21)

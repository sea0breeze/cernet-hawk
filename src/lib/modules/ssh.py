import socket


def sshDetect(ip, port):
    # not complete yet
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(50)
        s.send('SSH-2.0-OpenSSH_6.0p1\r\n')
        ciphers = s.recv(984)
        s.close()
        return banner, ciphers
    except:
        return

if __name__ == '__main__':
    print sshDetect("ip", 22)

import telnetlib


def telnetDetect(host, port=2611,  timeout=40):
    # not complete yet
    try:
        tn = telnetlib.Telnet(Host, port=port, timeout=timeout)
    except:
        pass
    finally:
        tn.close()
        return

if __name__ == '__main__':
    pass

import socket
import struct
from pprint import pprint
from cStringIO import StringIO
# from paramiko import Transport

from Detect import Detect
# from lib.log import cprint

# refer:
# https://stribika.github.io/2015/01/04/secure-secure-shell.html
# http://blog.csdn.net/macrossdzh/article/details/5691924
# http://www.iodigitalsec.com/ssh-fingerprint-and-hostkey-with-paramiko-in-python/
# RFC-4251~4

class sshDetect(Detect):
    '''
    :str. banner
    :

    '''
    # not complete yet
    def __init__(self, ip, port = 22, timeout = 2):
        super(sshDetect, self).__init__(ip, port)
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect((ip, port))
            banner = s.recv(50).strip('\r\n').split(' ')

            try:
                self.data.version = banner[0]
                self.data.os = banner[1]
            except IndexError:
                pass

            s.send('{}\r\n'.format(banner[0]))
            self._raw_recv = s.recv(2048)

            # tran = Transport(s)
            # self.ssh_key = tran.get_remote_server_key()
            # tran.close()

            s.close()
            self._parse_raw_data()
        except Exception as e:
            cprint(str(e), 'error')
            return

    def _parse_raw_data(self):
        stream = StringIO(self._raw_recv)
        packet_length = struct.unpack('>i', stream.read(4))[0]
        padding_length = ord(stream.read(1))
        message_code = ord(stream.read(1))
        cookie = stream.read(16)
        kex_algo_length = struct.unpack('>i', stream.read(4))[0]
        self.data.kex_algo = stream.read(kex_algo_length).split(',')
        server_host_key_algo_length = struct.unpack('>i', stream.read(4))[0]
        self.data.server_host_key_algo = stream.read(server_host_key_algo_length).split(',')

        enc_algo_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.data.enc_algo_client_to_server = stream.read(enc_algo_client_to_server_length).split(',')

        enc_algo_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.data.enc_algo_server_to_client = stream.read(enc_algo_server_to_client_length).split(',')

        mac_algo_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.data.mac_algo_client_to_server = stream.read(mac_algo_client_to_server_length).split(',')

        mac_algo_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.data.mac_algo_server_to_client = stream.read(mac_algo_server_to_client_length).split(',')

        compress_algo_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.data.compress_algo_client_to_server = stream.read(compress_algo_client_to_server_length).split(',')

        compress_algo_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.data.compress_algo_server_to_client = stream.read(compress_algo_server_to_client_length).split(',')

        lang_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.data.lang_client_to_server = stream.read(lang_client_to_server_length).split(',')

        lang_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.data.lang_server_to_client = stream.read(lang_server_to_client_length).split(',')


if __name__ == '__main__':
    ssh_test = sshDetect("202.112.26.119", 22)
    pprint(ssh_test.data)

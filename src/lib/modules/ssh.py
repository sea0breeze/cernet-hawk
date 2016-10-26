import socket
import struct
from cStringIO import StringIO
# from paramiko import Transport

from Detect import Detect
from attrDict import attrDict
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
    def __init__(self, ip, port):
        super.__init__(self)
        self.data.ip = ip
        self.data.port = port
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket()
            s.connect((ip, port))
            self.banner = s.recv(50).strip('\r\n').split(' ')

            try:
                self.version = self.banner[0]
                self.os = self.banner[1]
            except IndexError:
                pass

            s.send('{}\r\n'.format(self.banner[0]))
            self._raw_recv = s.recv(2048)

            # tran = Transport(s)
            # self.ssh_key = tran.get_remote_server_key()

            s.close()
            tran.close()
        except Exception as e:
            cprint(str(e), 'error')
            return

    def parse_raw_data(self):
        stream = StringIO(self._raw_recv)
        packet_length = struct.unpack('>i', stream.read(4))[0]
        padding_length = ord(stream.read(1))
        message_code = ord(stream.read(1))
        cookie = stream.read(16)
        kex_algo_length = struct.unpack('>i', stream.read(4))[0]
        self.kex_algo_string = stream.read(kex_algo_length).split(',')
        server_host_key_algo_length = struct.unpack('>i', stream.read(4))[0]
        self.server_host_key_algo_string = stream.read(server_host_key_algo_length).split(',')

        enc_algo_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.enc_algo_client_to_server_string = stream.read(enc_algo_client_to_server_length).split(',')

        enc_algo_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.enc_algo_server_to_client_string = stream.read(enc_algo_server_to_client_length).split(',')

        mac_algo_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.mac_algo_client_to_server_string = stream.read(mac_algo_client_to_server_length).split(',')

        mac_algo_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.mac_algo_server_to_client_string = stream.read(mac_algo_server_to_client_length).split(',')

        compress_algo_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.compress_algo_client_to_server_string = stream.read(compress_algo_client_to_server_length).split(',')

        compress_algo_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.compress_algo_server_to_client_string = stream.read(compress_algo_server_to_client_length).split(',')

        lang_client_to_server_length = struct.unpack('>i', stream.read(4))[0]
        self.lang_client_to_server_string = stream.read(lang_client_to_server_length).split(',')

        lang_server_to_client_length = struct.unpack('>i', stream.read(4))[0]
        self.lang_server_to_client_string = stream.read(lang_server_to_client_length).split(',')

    def result(self):
        re = {}
        re['version'] = self.version
        # re['os'] = self.os
        re['kex_algo'] = self.kex_algo_string
        re['host_key_algo'] = self.server_host_key_algo_string
        re['enc_client_to_server'] = self.server_host_key_algo_string
        re['enc_server_to_client'] = self.enc_algo_server_to_client_string
        re['mac_client_to_server'] = self.mac_algo_server_to_client_string
        re['mac_server_to_client'] = self.mac_algo_server_to_client_string
        re['compress_algo_client_to_server'] = self.compress_algo_client_to_server_string
        re['compress_algo_server_to_client'] = self.compress_algo_server_to_client_string
        re['lang_client_to_server'] = self.lang_client_to_server_string
        re['lang_server_to_client'] = self.lang_server_to_client_string
        return re

if __name__ == '__main__':
    ssh_test = sshDetect("202.120.1.140", 22)
    print ssh_test.banner
    ssh_test.parse_raw_data()
    print ssh_test.result()

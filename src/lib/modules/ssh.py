import socket
import struct
from lib.log import cprint
from cStringIO import StringIO

# refer:
# https://stribika.github.io/2015/01/04/secure-secure-shell.html
# http://blog.csdn.net/macrossdzh/article/details/5691924
# RFC-4253

class sshDetect:
    '''
    :str. banner
    :

    '''
    # not complete yet
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
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
            self._raw_recv = s.recv(984)
            s.close()
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


if __name__ == '__main__':
    ssh_test = sshDetect("0.0.0.0", 22)
    print ssh_test.banner
    ssh_test.parse_raw_data()

#!/usr/bin/env python
# coding=utf-8

import socket
from struct import unpack

from utils.log import cprint
from common.classes.PortBase import PortBase
from orm.servicesinfo import ServicesInfo

def recv_str(s):
    res = ""
    while 1:
        ch = s.recv(1)
        if ch == '\x00':
            break
        res += ch
        if len(res) >= 1024:
            break    # avoid infinite loop
    return res

class mysqlDetect(PortBase):
    '''
    Mysql Detection.
    '''

    def __init__(self):
        super(mysqlDetect, self).__init__()
        self.name = 'mysqlDetect'

    def run(self, ip, port=3306):
        try:
            s = socket.socket()
            s.connect((ip, port))
            s.recv(4)
            self.data.protocol_version = ord(s.recv(1))
            self.data.server_version = recv_str(s)
            self.data.connection_id = unpack('I', s.recv(4))[0]
            self.data.auth_data = recv_str(s)
            if self.data.protocol_version == 10:
                cflag1 = s.recv(2)
                self.data.character_set = ord(s.recv(1))
                self.data.status_flags = unpack('H', s.recv(2))[0]
                self.data.capability_flags = unpack('I', cflag1+s.recv(2))[0]
                auth_len = ord(s.recv(1))
                assert set(s.recv(10)) == set(['\x00'])
                self.data.auth_data += recv_str(s)
                if auth_len:
                    self.data.auth_name = s.recv(auth_len)
                    assert s.recv(1) == '\x00'
        except Exception as e:
            cprint(str(e), 'error')
            self.clear()
            return None

        ServicesInfo.add(ip, port, 'mysql', self.data)
        s.close()
        self.clear()
        return True

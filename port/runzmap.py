#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import os
from json import dumps

import config.common
from utils.log import cprint
from common.classes.Base import Base
from orm.zmapinfo import ZmapInfo

class ZmapScan(Base):
    """
    Zmap scanner.
    """

    def __init__(self):
        """
        Initialize the zmap scanner.
        """
        super(ZmapScan, self).__init__()
        self.zmap_result = {}
        self.zmap_path = subprocess.check_output(['which', 'zmap']).rstrip('\n')
        if not self.zmap_path:
            cprint('Zmap is not installed!', 'error')
            exit()

    def single_run_zmap(self, port, ips):
        """
        Must run this function as root. Otherwise fail.
        :param ports: str. the port that zmap scans
        :param ips: str. ip addresses range in CIDR block notation
        """
        cprint("Run zmap on port {} of {}".format(port, ips), 'debug')
        os.seteuid(0)  # run as root.
        if not self.zmap_path:
            print 'Zmap is not installed!'
            exit()
        cmd = [self.zmap_path] + config.common.ZMAP_CMD + ["-p", port, ips]
        cprint("start process: " + str(cmd), "debug")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if err:
            cprint(err, 'error')
            return

        if out:
            cprint("One zmap scanning finished!", "debug")
        else:
            cprint("No result found this time!", "warning")
            return

        for ip in out.strip().split('\n'):
            if self.zmap_result.has_key(ip):
                self.zmap_result[ip].append(port)
            else:
                self.zmap_result[ip] = [port]

    def run(self, ports, ips):
        """
        A wrapper for single_run_zmap.
        :param ports: list. the ports that zmap scans
        :param ips: str. ip addresses range in CIDR block notation
        """
        cprint("Start running zmap on port {} of {}".format(''.join(ports), ips), 'info')
        for port in ports:
            self.single_run_zmap(port, ips)

        cprint("All zmap scanning finished!", "info")
        ZmapInfo.addWithJson(dumps(self.zmap_result))



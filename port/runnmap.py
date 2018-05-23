#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import os.path
import subprocess
import xml.etree.cElementTree as ET
from json import dumps

import config.common
import config.paths
from common.classes.Base import Base
from orm.nmapinfo import NmapInfo
from orm.servicesinfo import ServicesInfo
from utils.log import cprint
from utils.ipaddr import isIPv4


class NmapScan(Base):
    """
    Nmap scanner.
    """
    name = "nmapscan"

    def __init__(self):
        """
        Initialize the nmap scanner.
        """
        super(NmapScan, self).__init__()
        self.nmap_path = subprocess.check_output(['which', 'nmap']).rstrip('\n')
        if not self.nmap_path:
            cprint('Nmap is not installed!', 'error')
            exit()
        self.error_list = []
        self.nmap_result = {}
        self.current_ip = None

    def parse_nmap_xml(self, nmap_xml):
        """
        Parse the xml file and extract the imforation of web services.
        Service info contains (name, version, extrainfo, product, devicetype, ostype...)
        :param nmap_xml: str. The name of the xml file to parse.
        :return: dict. Use open port number as key and concrete infomation of the web service as value.
        """

        try:
            tree = ET.parse(nmap_xml)
            root = tree.getroot()
            result = {}
            filter_flag = True
            for port in root.find('host').find('ports').findall('port'):
                if port.find('state').get('state') not in ('filtered', 'closed'):
                    filter_flag = False
                if port.find('state').get('state') == 'open':
                    service = port.find('service').attrib
                    service.pop('conf')
                    service.pop('method')
                    result[port.get('portid')] = service
        except Exception as e:
            cprint(e, 'error')
            self.error_list.append(self.current_ip)
            return None

        # What if we get nothing from the xml...
        if not result:
            if filter_flag:
                cprint('All open ports detected by zmap are actually filtered or closed!', 'warning')
            else:
                cprint('Failed to parse nmap xml!', 'error')
                self.error_list.append(self.current_ip)
            return None
        else:
            cprint('Nmap xml parsed!', 'debug')

        return result

    def run(self, ip, ports=config.common.PORTS):
        """
        Must run as root.
        Use nmap to get further imformation about the ip and ports
        scanned by zmap.
        :param ip: str. The target ip that zmap will scan.
        :param port: list. All open ports of the ip founded by zmap.
        :return: list. Further imformation about services on the host.
        """

        self.current_ip = ip
        filename = os.path.join(config.paths.logpath, '{}_{}.xml.log'.format(ip, '-'.join(map(str, ports))))
        # Save time while debugging by not scanning ip that has been scanned.
        if 0 and os.path.exists(filename):
            cprint('Previous scan result exists for {}, just parse the xml.'.format(ip), 'info')
            return self.parse_nmap_xml(filename)

        # os.seteuid(0)  # run as root.
        cprint('Start scanning {} on port {} with nmap'.format(ip, ','.join(ports)), 'info')
        cmd = [self.nmap_path] + config.common.NMAP_CMD + \
              [ip, '-p', ','.join(ports)]
        v6Scan = False
        if not isIPv4(ip):  # ipv6
            cmd.append('-6')
            v6Scan = True
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, error = p.communicate()

        if error:
            cprint(error, 'error')

        cprint('Nmap finished scanning {} on {}'.format(
            ip, ','.join(map(str, ports))), 'info')
        # store temporary xml file in logs dir.
        f = open(filename.replace(":", "_"), 'w+')
        f.write(out)
        f.close()
        cprint('nmap result %s' % self.parse_nmap_xml(filename), 'debug')
        self.nmap_result[ip] = self.parse_nmap_xml(filename)
        if v6Scan:
            for port in self.nmap_result[ip]:
                ServicesInfo.add(ip, port, self.nmap_result[ip][port]["name"], self.nmap_result[ip][port])
        else:
            NmapInfo.addWithJson(dumps(self.nmap_result))

    def nouse_run(self, ipdir):
        """
        A wrapper for single_run_nmap.
        :param ipdir: dict. Using ip:ports as key:value.
        :return: dict. Further imformation about services on each host.
        """

        result = {}
        for ip in ipdir:
            tmp_res = self.single_run_nmap(ip, ipdir[ip])
            if tmp_res != None:
                result[ip] = tmp_res

        if self.error_list:
            cprint('Scanning finished, but some error occurs while nmap scanning!', 'error')
            with open('test.log', 'w') as f:
                for error in self.error_list:
                    f.write("{}\n".format(error))
        else:
            cprint('One ip range scanning finished with no error!', 'info')

        self.nmap_result = result
        NmapInfo.addWithJson(dumps(result))


if __name__ == "__main__":
    print 'Testing'
    test = NmapScan()
    test.run('140.82.4.59', ['22', '80'])
    test.run('2001:da8:8000:6::301', ['22', '80'])

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import os
import xml.etree.cElementTree as ET
import os.path

from utils.log import cprint
import config.paths
import config.common
from common.classes.Base import Base
from orm.schema.mongo import Mongo


def parse_nmap_xml(nmap_xml):
    """
    Parse the xml file and extract the imforation of web services.
    Service info contains (name, version, extrainfo, product, devicetype, ostype...)
    :param nmap_xml: str. The name of the xml file to parse.
    :return: dict. Use open port number as key and concrete infomation of the web service as value.
    """

    errors = []
    try:
        tree = ET.parse(nmap_xml)
        root = tree.getroot()
        result = {}
        filter_flag = True
        for port in root.find('host').find('ports').findall('port'):
            if port.find('state').get('state') not in  ('filtered', 'closed'):
                filter_flag = False
            if port.find('state').get('state') == 'open':
                service = port.find('service').attrib
                service.pop('conf')
                service.pop('method')
                result[int(port.get('portid'))] = service
    except Exception as e:
        cprint(e, 'error')
        errors.append(nmap_xml)
        return None

    # What if we get nothing from the xml...
    if not result:
        if filter_flag:
            cprint('All open ports detected by zmap are actually filtered or closed!', 'info')
            return None
        else:
            cprint('Failed to parse nmap xml!', 'error')
            errors.append(nmap_xml)
    else:
        cprint('Nmap xml parsed!', 'debug')

    return result, errors


class NmapScan(Base):
    """
    Nmap scanner.
    """

    def __init__(self):
        """
        Initialize the nmap scanner.
        :param ipdir: dict. Using ip:ports as key:value.
        """
        super(NmapScan, self).__init__()
        self.nmap_path = subprocess.check_output(['which', 'nmap']).rstrip('\n')
        if not self.nmap_path:
            cprint('Nmap is not installed!', 'error')
            exit()
        self.error_list = []

    def single_run_nmap(self, ip, ports):
        """
        Must run as root.
        Use nmap to get further imformation about the ip and ports
        scanned by zmap.
        :param ip: str. The target ip that zmap will scan.
        :param port: list. All open ports of the ip founded by zmap.
        :return: list. Further imformation about services on the host.
        """

        filename = os.path.join(config.paths.logpath, '{}_{}.xml.log'.format(ip, '-'.join(map(str, ports))))
        # Save time while debugging by not scanning ip that has been scanned.
        if config.common.DEBUG and os.path.exists(filename):
            cprint('Previous scan result exists for {}, just parse the xml.'.format(ip), 'info')
            return parse_nmap_xml(filename)

        os.seteuid(0)  # run as root.
        cprint('Start scanning {} with nmap'.format(ip), 'info')
        cmd = [self.nmap_path] + config.common.NMAP_CMD + [ip, '-p', ','.join(map(str, ports))]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = p.communicate()

        if error:
            cprint(error, 'error')

        cprint('Nmap finished scanning {} on {}'.format(
            ip, ','.join(map(str, ports))), 'info')

        # store temporary xml file in logs dir.
        f = open(filename, 'w+')
        f.write(out)
        f.close()
        result, self.error_list = parse_nmap_xml(filename)
        return result

    def run(self, ipdir):
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
        print result


if __name__ == "__main__":
    print 'Testing'
    test = NmapScan()
    test.run({'202.120.7.149': [80, 22]})

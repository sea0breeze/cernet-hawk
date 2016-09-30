#!/usr/bin/env python
# coding=utf-8

import subprocess
import os
import config
import xml.etree.cElementTree as ET
from log import cprint


def parse_nmap_xml(nmap_xml):
    tree = ET.parse(nmap_xml)
    root = tree.getroot()
    result = {}
    for port in root.find('host').find('ports').findall('port'):
        if port.find('state').get('state') == 'open':
            service = port.find('service').attrib
            service.pop('conf')
            service.pop('method')
            # service info contains (name, version, extrainfo, product,
            # devicetype, ostype...)
            result[port.get('portid')] = service
    if result:
        cprint('Nmap xml parsed!', 'debug')
    else:
        cprint('Failed to parse nmap xml!', 'error')
    return result


def single_run_nmap(ip, ports):
    """
    Must run as root. The path of nmap is returned by 'which' cmd.
    Use nmap to get further imformation about the ip and ports
    scanned by zmap.
    :param ip: str. The target ip that zmap will scan.
    :param port: list. All open ports of the ip founded by zmap.
    :return: list. Further imformation about services on the host.
    """
    os.seteuid(0)  # run as root.
    nmap_path = subprocess.check_output(['which', 'nmap']).rstrip('\n')
    if not nmap_path:
        cprint('Nmap is not installed!', 'error')
        exit()
    cmd = [nmap_path] + config.NMAP_CMD + [ip, '-p', ','.join(map(str, ports))]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = p.communicate()

    if _:
        cprint(_, 'error')
        exit()

    cprint('Nmap finished scanning {} on {}'.format(
        ip, ','.join(map(str, ports))), 'info')

    # store temporary xml file in /data/namp/ dir.
    filename = '../data/nmap/{}_{}'.format(ip, '-'.join(map(str, ports)))
    f = open(filename, 'w+')
    f.write(out)
    f.close()
    return parse_nmap_xml(filename)


def run_nmap(ipdir):
    """
    A wrapper for single_run_nmap.
    :param ipdir: dict. Using ip:ports as key:value.
    :return: dict. Further imformation about services on each host.
    """
    result = {}
    for ip in ipdir:
        result[ip] = single_run_nmap(ip, ipdir[ip])
    cprint('One ip range scanning finished!', 'info')
    return result


if __name__ == "__main__":
    print 'Testing'
    print run_nmap({'127.0.0.1': [80, 22]})

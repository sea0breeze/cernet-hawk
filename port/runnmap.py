#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import os
import config.common
import xml.etree.cElementTree as ET
from utils.log import cprint

error_list = []
nmap_path = ''


def parse_nmap_xml(nmap_xml):
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
            if port.find('state').get('state') not in  ('filtered', 'closed'):
                filter_flag = False
            if port.find('state').get('state') == 'open':
                service = port.find('service').attrib
                service.pop('conf')
                service.pop('method')
                result[int(port.get('portid'))] = service
    except Exception as e:
        cprint(e, 'error')
        error_list.append(nmap_xml)
        return None

    # What if we get nothing from the xml...
    if not result:
        if filter_flag:
            cprint('All open ports detected by zmap are actually filtered or closed!', 'info')
            return None
        else:
            cprint('Failed to parse nmap xml!', 'error')
            error_list.append(nmap_xml)
    else:
        cprint('Nmap xml parsed!', 'debug')

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

    global nmap_path

    filename = 'data/nmap/{}_{}'.format(ip, '-'.join(map(str, ports)))
    # Save time while debugging by not scanning ip that has been scanned.
    if os.path.exists(filename):
        cprint('Previous scan result exists for {}, just parse the xml.'.format(ip), 'info')
        return parse_nmap_xml(filename)

    os.seteuid(0)  # run as root.
    cprint('Start scanning {} with nmap'.format(ip), 'info')
    cmd = [nmap_path] + config.common.NMAP_CMD + [ip, '-p', ','.join(map(str, ports))]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = p.communicate()

    if error:
        cprint(error, 'error')

    cprint('Nmap finished scanning {} on {}'.format(
        ip, ','.join(map(str, ports))), 'info')

    # store temporary xml file in /data/namp/ dir.
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

    global nmap_path
    nmap_path = subprocess.check_output(['which', 'nmap']).rstrip('\n')
    if not nmap_path:
        cprint('Nmap is not installed!', 'error')
        exit()

    result = {}
    for ip in ipdir:
        tmp_res = single_run_nmap(ip, ipdir[ip])
        if tmp_res != None:
            result[ip] = tmp_res

    if error_list:
        cprint('Scanning finished, but some error occurs while nmap scanning!', 'error')
        # save(error_list, 'nmap_error')
        with open('test.log', 'w') as f:
            f.write(str(error_list))
    else:
        cprint('One ip range scanning finished with no error!', 'info')

    return result


if __name__ == "__main__":
    print 'Testing'
    print run_nmap({'202.120.7.149': [80, 22]})

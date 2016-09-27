#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import os
import config
import types
from netaddr import IPAddress, IPNetwork, IPRange, cidr_merge


def do_zmap(port, range):
    """
    Must run this function as root. Otherwise fail.
    The path of zmap is returned by 'which' cmd.
    :param port: int. the port zmap scans
    :param range: str. ip addresses range in CIDR block notation
    :return: list. all ips in the range that zmap deem has port open
    """
    os.seteuid(0)  # run as root.
    zmap_path = subprocess.check_output(['which', 'zmap']).rstrip('\n')
    if not zmap_path:
        print 'Zmap is not installed!'
        exit()
    cmd = [zmap_path] + config.ZMAP_CMD + ["-p", str(port), range] 
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, _ = p.communicate()
    #print ' '.join(out.split('\n'))
    return out.split('\n')


def make_iplist(l):
    """
    Expect the input to be well-formatted.
    :param l: list. ip ranges(or single ip) e.g. [('192.0.2.1', '192.0.2.15'), '192.0.3.1']
    :return: list. CIRD notation of ips in the range
    """
    re = []
    for ip in l:
        if type(ip) == types.TupleType:
            r = IPRange(ip[0], ip[1])
            re.extend(r.cidrs())
        else: # ip is a str. e.g. '192.0.3.1'
            re.append(IPAddress(ip))
    return cidr_merge(re)

def zmap_range(ranges):
    #subprocess.Popen('touch output')
    cidrs = make_iplist(ranges)
    print cidrs
    dirs = {}
    for p in config.PORTS:
        dirs[p] = []
        for c in cidrs:
            dirs[p].extend(do_zmap(p, str(c)))
    return dirs
    #with open("output1", 'w') as f:
    #    for p in config.PORTS:
    #        f.write(str(p) + " ")
    #        for c in cidrs:
    #            print "scanning " + str(c) + str(p)
    #            f.write(' '.join(do_zmap(p, str(c))))
    #        f.write('\n')

if __name__ == "__main__":
    print "Running Test"
    #test_range1 =  [('192.168.0.1', '192.168.0.255'), '192.168.0.3']
    test_range2 =  [('202.120.0.0', '202.120.63.255')] # 虽然提供了多个口的功能,但最好还是CIDR尽量少,不然很慢.
    # TODO: 用一个CIDR的SUPERSET涵盖所有IP,然后再从结果中去掉不在范围内的IP
    res = zmap_range(test_range2)

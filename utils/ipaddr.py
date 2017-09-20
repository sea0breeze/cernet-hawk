#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import pygeoip
import socket

IPREG = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"


def isIPv4(ip):
    return re.compile(IPREG).match(ip)


def iplookup(ip):
    try:
        gi = pygeoip.GeoIP('./utils/GeoLiteCity.dat')['city']
        return gi.record_by_addr(ip)
    except Exception as e:
        return "Unknown"


def addr2int(value):
    _ = value.split('.')
    return (long(_[0]) << 24) + (long(_[1]) << 16) + (long(_[2]) << 8) + long(_[3])


def int2addr(value):
    return '.'.join(str(value >> n & 0xff) for n in (24, 16, 8, 0))


def makeMask(bits):
    return 0xffffffff ^ (1 << 32 - bits) - 1


def compressIpv6(address):
    zeros = re.findall("(?:0000:)+", address)
    if zeros:
        address = address.replace(
            sorted(zeros, key=lambda _: len(_))[-1], ":", 1)
        address = re.sub(r"(\A|:)0+(\w)", "\g<1>\g<2>", address)
        if address == ":1":
            address = "::1"
    return address

# Note: socket.inet_ntop not available everywhere (Reference:
# https://docs.python.org/2/library/socket.html#socket.inet_ntop)


def inetNtoa6(packed_ip):
    _ = packed_ip.encode("hex")
    return compress_ipv6(':'.join(_[i:i + 4] for i in xrange(0, len(_), 4)))


def ip2domain(ip):
    domain = 'no-data'
    try:
        domain = socket.gethostbyaddr(ip)[0]
    except socket.herror as e:
        return None
    if domain == 'no-data':
        return None
    return domain

if __name__ == '__main__':
    print iplookup(raw_input('ip: '))

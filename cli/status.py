#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pprint
import subprocess
from collections import OrderedDict


def status():
    p = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    p = p.communicate()[0]
    p = p.decode('utf8').split('\n')
    workers = []
    flower = ''
    web = ''
    dispatcher = ''
    for i in p:
        if 'celery worker' in i:
            workers.append(i.split()[1])
        elif 'celery -A hawk flower' in i:
            flower = i.split()[1]
        elif 'dispatch.py' in i:
            dispatcher = i.split()[1]
        elif 'app.py' in i:
            web = i.split()[1]
    if len(workers):
        print("Celery: run %i workers" %
              (len(workers)))
    else:
        print("Celery not work...")

    if len(flower):
        print("Flower: run with pid " + flower)
    else:
        print("Flower not work...")

    if len(web):
        print("Web: run with pid " + web)
    else:
        print("Web not work...")

    if len(dispatcher):
        print("Dispatcher: run with pid " + dispatcher)
    else:
        print("Dispatcher not work...")


def CPUinfo():
    '''
    Return the information in /proc/CPUinfo
    as a dictionary in the following format:
    CPU_info['proc0']={...}
    CPU_info['proc1']={...}
    '''
    CPUinfo = OrderedDict()
    procinfo = OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                # end of one processor
                CPUinfo['proc%s' % nprocs] = procinfo
                nprocs = nprocs+1
                # Reset
                procinfo = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[
                        1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return CPUinfo


def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo = OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

if __name__ == '__main__':
    print("======= Worker Status =======")
    status()

    print("=======   CPU Info    =======")
    cpuinfo = CPUinfo()
    for processor in cpuinfo.keys():
        print(cpuinfo[processor]['model name'])

    print("=======  Memory Info  =======")
    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))

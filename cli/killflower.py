#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import subprocess


def killflower():
    p = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
    p = p.communicate()[0]
    p = p.decode('utf8').split('\n')
    flower = ''
    for i in p:
        if 'celery -A hawk flower' in i:
            flower = i.split()[1]
            break
    if len(flower):
        os.system("kill -9 " + flower)

if __name__ == '__main__':
    killflower()

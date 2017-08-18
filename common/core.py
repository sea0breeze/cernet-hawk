#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os


def initDB():
    return True


def getModules(modulepath):

    modules = []

    skip = ["__init__"]

    # split one action into multiple line, make it easy understand
    tmp = os.path.join(modulepath)
    tmp = [i for i in os.listdir(tmp)]
    tmp = filter(lambda i: i[:-3]
                 not in skip and i.endswith(".py"), tmp)
    modules.extend([i[:-3] for i in tmp])

    return modules


def importModules(modules, DEBUG=False):

    # map module to it's code
    # e.g 'whois' => instance of Whois Class
    modulesmap = dict()

    for module in modules:

        if DEBUG:
            print("[*]Init module: ", module)

        modulesmap[module] = getattr(
            getattr(
                __import__("services." + module), module
            ), module + "Detect"
        )()

    return modulesmap

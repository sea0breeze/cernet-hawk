#!/usr/bin/env python
# -*- coding:utf-8 -*-


def check_sudo():
    """
    Checks for sudo/Administrator privileges
    """

    check = None

    if not subprocess.mswindows:
        if getattr(os, "geteuid"):
            check = os.geteuid() == 0
    else:
        import ctypes
        check = ctypes.windll.shell32.IsUserAnAdmin()

    return check


def conversion(keydict):
    '''
    Exchange the key and value of a dictionary
    :param keydict: dict. the dictionary need exchanging
    :return valuedict: dict. the dictionary exchanged
    '''
    valuedict = {}
    for key in keydict.keys():
        valuelist = keydict[key]
        for element in valuelist:
            if element in valuedict:
                valuedict[element] += [key]
            else:
                valuedict[element] = [key]
    return valuedict


def parseUrl(url):

    if not url.startswith("http://") or url.startswith("https://"):
        if ':443' in url:
            url = "https://" + url
        else:
            url = "http://" + url

    url = (url + '/') if url[-1] != '/' else url

    return url


if __name__ == "__main__":
    keydict = {'80': ['202.120.61.34', '202.120.24.151',
                      '202.120.49.25', '202.120.25.239',
                      '202.120.63.184', '202.120.1.7'],
               '443': ['202.120.24.43', '202.120.46.2',
                       '202.120.1.26', '202.120.53.107',
                       '202.120.34.3', '202.120.32.61',
                       '202.120.53.235', '202.120.44.244',
                       '202.120.52.38', '202.120.46.9',
                       '202.120.35.239', '202.120.33.137']}
    print conversion(keydict)

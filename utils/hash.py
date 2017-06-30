#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib


def md5(s):
    return hashlib.md5(s).hexdigest()


def sha1(s):
    return hashlib.sha1(s).hexdigest()


def sha224(s):
    return hashlib.sha224(s).hexdigest()


def sha256(s):
    return hashlib.sha256(s).hexdigest()


def sha384(s):
    return hashlib.sha384(s).hexdigest()


def sha512(s):
    return hashlib.sha512(s).hexdigest()

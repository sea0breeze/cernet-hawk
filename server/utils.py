#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def errormsg(msg):
    msg = {
        "status": "error",
        "msg": msg
    }
    return json.dumps(msg)


def okmsg(data):
    data = {
        "status": "ok",
        "data": data
    }
    return json.dumps(data)

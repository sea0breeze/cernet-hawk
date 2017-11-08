#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def ok(self, data):
        self.write(json.dumps({"data": data}))

    def error(self, status_code, msg):
        self.set_status(status_code)
        self.write(json.dumps({"msg": msg}))

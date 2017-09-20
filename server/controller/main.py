#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from server.controller.base import BaseHandler


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")

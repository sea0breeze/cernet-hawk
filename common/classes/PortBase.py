#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pprint import pprint

from common.classes.AttribDict import AttribDict
from common.classes.Base import Base
from orm.schema.mongo import Mongo


class PortBase(Base):

    """docstring for PortBase"""

    def __init__(self):
        super(PortBase, self).__init__()
        self.data = AttribDict()

    def pprint(self, stream=None, indent=1, width=80, depth=None):
        pprint(self.data, stream, indent, width, depth)

    def save(self):
        self.db = Mongo(self.type)
        self.db.insert(self.data)

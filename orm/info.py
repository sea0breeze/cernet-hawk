#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mongoengine import *


class Info(Document):
    ip = StringField(max_length=30, required=True)
    port = IntField(default=0, required=True)
    details = DictField()

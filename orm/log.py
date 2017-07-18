#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mongoengine import *


class Log(Document):

    lid = StringField(max_length=32, required=True)
    level = StringField(max_length=5, required=True)
    generated = DateTimeField(required=True)
    message = StringField(max_length=320, required=True)

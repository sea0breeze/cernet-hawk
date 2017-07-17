#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mongoengine import *


class Task(Document):

    tid = StringField(max_length=32, required=True)
    data = IntField(default=0, required=True)
    taskType = StringField(max_length=30, required=True)
    status = StringField(max_length=30, required=True)

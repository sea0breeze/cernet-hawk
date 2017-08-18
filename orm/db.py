#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils.mtime import today
from mongoengine import connect

connect('hawk'+today())
# connect('hawk')
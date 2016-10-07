#!/usr/bin/env python
# coding=utf-8

from lib.dozmap import zmap_range
from lib.runnmap import run_nmap
import lib.db as db
from lib.utils import conversion

tmp = zmap_range([('202.120.0.0', '202.120.7.255')])
db.save(tmp, 'test_zmap_tmp')
tmp = db.get('test_zmap_tmp')
result = run_nmap(conversion(tmp))
db.save(result, 'test_nmap_tmp')

#!/usr/bin/env python
# coding=utf-8

from lib.scan.dozmap import zmap_range
from lib.scan.runnmap import run_nmap
import lib.scan.db as db
from lib.scan.utils import conversion

#tmp = zmap_range([('202.120.0.0', '202.120.63.255')])
#db.save(tmp, 'test_zmap_tmp')
tmp = db.get('test_zmap_tmp')
result = run_nmap(conversion(tmp))
db.save(result, 'test_nmap_tmp')

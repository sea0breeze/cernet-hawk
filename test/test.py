#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import db

from log import *


class HawkTest(unittest.TestCase):

    def test_log(self):
        tmp = {'t': 1, 'e': 233, 's': 577}
        db.save(tmp, 'tmpdata')
        self.assertEqual(tmp, db.get('tmpdata'))

if __name__ == '__main__':
    unittest.main()

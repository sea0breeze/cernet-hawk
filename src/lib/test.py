import unittest

from log import *


class HawkTest(unittest.TestCase):

    def test_log(self):
        tmp = {'t': 1, 'e': 233, 's': 577}
        save(tmp, 'tmpdata')
        self.assertEqual(tmp, get('tmpdata'))

if __name__ == '__main__':
    unittest.main()

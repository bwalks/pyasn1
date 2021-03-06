#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2017, Ilya Etingof <etingof@gmail.com>
# License: http://pyasn1.sf.net/license.html
#
from pyasn1 import debug
from pyasn1 import error
from sys import version_info

if version_info[0:2] < (2, 7) or \
        version_info[0:2] in ((3, 0), (3, 1)):
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
else:
    import unittest


class DebugCaseBase(unittest.TestCase):
    def testKnownFlags(self):
        debug.setLogger(debug.Debug('all', 'encoder', 'decoder'))
        debug.setLogger(0)

    def testUnknownFlags(self):
        try:
            debug.setLogger(debug.Debug('all', 'unknown', loggerName='xxx'))

        except error.PyAsn1Error:
            debug.setLogger(0)
            return

        else:
            debug.setLogger(0)
            assert 0, 'unknown debug flag tolerated'



if __name__ == '__main__':
    unittest.main()

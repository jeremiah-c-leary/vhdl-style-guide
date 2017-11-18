import os

import unittest
import sys

from vsg.rules import process
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','process','process_test_input.vhd'))

class testRuleProcessMethods(unittest.TestCase):

    def test_rule_006(self):
        oRule = process.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

if __name__ == '__main__':
    unittest.main()

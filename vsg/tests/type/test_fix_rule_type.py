import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import type
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','type','type_test_input.vhd'))

class testFixRuleTypeMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = type.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = type.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

if __name__ == '__main__':
    unittest.main()

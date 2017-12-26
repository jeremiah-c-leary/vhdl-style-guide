import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import subtype
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','type_definition','type_test_input.vhd'))

class testRuleSubtypeMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = subtype.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'subtype')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [51]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

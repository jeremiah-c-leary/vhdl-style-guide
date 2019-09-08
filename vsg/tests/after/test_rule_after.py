import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import after
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'after_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleAfterMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = after.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'after')
        self.assertEqual(oRule.identifier, '001')
        self.assertTrue(oRule.disable)
        self.assertEqual(oRule.magnitude, 1)
        self.assertEqual(oRule.units, 'ns')
        lExpected = [33, 34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_002(self):
        oRule = after.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'after')
        self.assertEqual(oRule.identifier, '002')
        self.assertTrue(oRule.disable)
        lExpected = ['48-63', '92-98']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_003(self):
        oRule = after.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'after')
        self.assertEqual(oRule.identifier, '003')
        self.assertTrue(oRule.disable)
        lExpected = [145, 147]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

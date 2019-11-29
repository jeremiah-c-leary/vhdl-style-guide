import os
import unittest

from vsg.rules import ranges
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'range_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleRange(unittest.TestCase):

    def test_rule_001_with_default(self):
        oRule = ranges.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'range')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [17,21,28,33]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_001_with_uppercase(self):
        oRule = ranges.rule_001()
        oRule.case = 'upper'
        dExpected = [5,9,17,21,29,33,34]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_with_default(self):
        oRule = ranges.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'range')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [18,22,30,35]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002_with_uppercase(self):
        oRule = ranges.rule_002()
        oRule.case = 'upper'
        dExpected = [6,10,22,30,31,36]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

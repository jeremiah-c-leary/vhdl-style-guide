import os

import unittest

from vsg.rules import attribute
from vsg import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'attribute_test_input.vhd'))

class testRuleAttributeMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = attribute.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'attribute')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [9,11,12]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = attribute.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'attribute')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [9]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = attribute.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'attribute')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [11]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

import os

import unittest

from vsg.rules import file_statement
from vsg import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'file_test_input.vhd'))

class testRuleFileMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = file_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [9,11,12]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = file_statement.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '002')

        dExpected = [9]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = file_statement.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'file')
        self.assertEqual(oRule.identifier, '003')

        dExpected = [9]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

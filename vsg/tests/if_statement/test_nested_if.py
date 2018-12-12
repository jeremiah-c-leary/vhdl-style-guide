import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile


class testRuleIfMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_nested_test_input.vhd'))


    def test_rule_030(self):
        oRule = if_statement.rule_030()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '030')
        dExpected = [19]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)


    def test_fix_rule_030(self):
        oRule = if_statement.rule_030()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[20].isBlank, True)
        self.assertEqual(self.oFile.lines[21].line, '    X <= \'0\';  -- This should be an error') 


    def test_rule_031(self):
        oRule = if_statement.rule_031()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '031')
        dExpected = [23]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_031(self):
        oRule = if_statement.rule_031()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFile.lines[22].line, '    X <= \'1\';  -- This should be an error')
        self.assertEqual(self.oFile.lines[23].isBlank, True)
        self.assertEqual(self.oFile.lines[24].line, '    if (A = \'1\' and B = \'1\') then')

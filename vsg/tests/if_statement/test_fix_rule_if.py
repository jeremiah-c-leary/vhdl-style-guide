import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))

class testFixRuleIfMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = if_statement.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = if_statement.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = if_statement.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = if_statement.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = if_statement.rule_005()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = if_statement.rule_006()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006_case(self):
        oRule = if_statement.rule_006()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = if_statement.rule_007()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = if_statement.rule_008()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008_case(self):
        oRule = if_statement.rule_008()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = if_statement.rule_009()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = if_statement.rule_010()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010_case(self):
        oRule = if_statement.rule_010()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = if_statement.rule_011()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011_case(self):
        oRule = if_statement.rule_011()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_012(self):
        oRule = if_statement.rule_012()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = if_statement.rule_013()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_014(self):
        oRule = if_statement.rule_014()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_015(self):
        oRule = if_statement.rule_015()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

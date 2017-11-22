import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','constant','constant_test_input.vhd'))

class testFixRuleConstantMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = constant.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = constant.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = constant.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = constant.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = constant.rule_005()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = constant.rule_006()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = constant.rule_007()
        self.assertFalse(oRule.fixable)

    def test_fix_rule_009(self):
        oRule = constant.rule_009()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

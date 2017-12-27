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

    def test_fix_rule_010(self):
        oRule = constant.rule_010()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = constant.rule_011()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[9].line, '  constant const   : std_logic :=\'0\';')

    def test_fix_rule_012(self):
        oRule = constant.rule_012()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[22].line, '  (')
        self.assertEqual(oFile.lines[23].line, '    0,')
        self.assertEqual(oFile.lines[24].line, '    1,')
        self.assertEqual(oFile.lines[25].line, '    2,')
        self.assertEqual(oFile.lines[26].line, '    3')
        self.assertEqual(oFile.lines[27].line, '  );')

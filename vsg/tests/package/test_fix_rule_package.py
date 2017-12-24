import os

import unittest

from vsg.rules import package
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','package','package_test_input.vhd'))

class testFixRulePackageMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = package.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = package.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = package.rule_003()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = package.rule_004()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = package.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = package.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = package.rule_007()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = package.rule_008()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = package.rule_009()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = package.rule_010()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_011(self):
        oRule = package.rule_011()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012(self):
        oRule = package.rule_012()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = package.rule_013()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = package.rule_014()
        self.assertFalse(oRule.fixable)

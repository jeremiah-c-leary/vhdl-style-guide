import os
import unittest

from vsg.rules import component
from vsg import vhdlFile


oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','component','component_test_input.vhd'))


class testFixRuleComponentMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = component.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = component.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = component.rule_003()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = component.rule_004()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = component.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = component.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = component.rule_007()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = component.rule_008()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = component.rule_009()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = component.rule_010()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_011(self):
        oRule = component.rule_011()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012(self):
        oRule = component.rule_012()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = component.rule_013()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = component.rule_014()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015(self):
        oRule = component.rule_015()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016(self):
        oRule = component.rule_016()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_017(self):
        oRule = component.rule_017()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = component.rule_018()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

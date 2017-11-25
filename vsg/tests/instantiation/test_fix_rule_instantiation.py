import os

import unittest
import sys

from vsg.rules import instantiation
from vsg import vhdlFile
from vsg import utils

oFilePort = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_test_input.vhd'))
oFileGeneric = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_generic_test_input.vhd'))

class testFixRuleInstantiationMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = instantiation.rule_001()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = instantiation.rule_002()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = instantiation.rule_003()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = instantiation.rule_004()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = instantiation.rule_005()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = instantiation.rule_006()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = instantiation.rule_007()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = instantiation.rule_008()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = instantiation.rule_009()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = instantiation.rule_010()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_011(self):
        oRule = instantiation.rule_011()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012(self):
        oRule = instantiation.rule_012()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = instantiation.rule_013()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = instantiation.rule_014()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015(self):
        oRule = instantiation.rule_015()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016(self):
        oRule = instantiation.rule_016()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_017(self):
        oRule = instantiation.rule_017()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_001_generics(self):
        oRule = instantiation.rule_001()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = instantiation.rule_018()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_019(self):
        oRule = instantiation.rule_019()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_020(self):
        oRule = instantiation.rule_020()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFilePort.lines[64].indentLevel, oFilePort.lines[63].indentLevel + 1)

    def test_fix_rule_021(self):
        oRule = instantiation.rule_021()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_022(self):
        oRule = instantiation.rule_022()
        oRule.fix(oFilePort)
        oRule.analyze(oFilePort)
        self.assertEqual(oRule.violations, [])

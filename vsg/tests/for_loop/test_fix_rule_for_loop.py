import os

import unittest

from vsg.rules import for_loop
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','for_loop','for_loop_test_input.vhd'))

class testFixRuleForLoopMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = for_loop.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_fix_rule_002(self):
#        oRule = for_loop.rule_002()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_003(self):
#        oRule = for_loop.rule_003()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_004(self):
#        oRule = for_loop.rule_004()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_005(self):
#        oRule = for_loop.rule_005()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_006(self):
#        oRule = for_loop.rule_006()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_006_case(self):
#        oRule = for_loop.rule_006()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_007(self):
#        oRule = for_loop.rule_007()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_008(self):
#        oRule = for_loop.rule_008()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_008_case(self):
#        oRule = for_loop.rule_008()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_009(self):
#        oRule = for_loop.rule_009()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_010(self):
#        oRule = for_loop.rule_010()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_010_case(self):
#        oRule = for_loop.rule_010()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_011(self):
#        oRule = for_loop.rule_011()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_011_case(self):
#        oRule = for_loop.rule_011()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFileCase)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_012(self):
#        oRule = for_loop.rule_012()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_013(self):
#        oRule = for_loop.rule_013()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_014(self):
#        oRule = for_loop.rule_014()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)

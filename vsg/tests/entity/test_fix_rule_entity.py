import os

import unittest

from vsg.rules import entity
from vsg import vhdlFile


oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','entity','entity_test_input.vhd'))


class testFixRuleEntityMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = entity.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = entity.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = entity.rule_003()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = entity.rule_004()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = entity.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[51].line, '   generic  (')

    def test_fix_rule_006(self):
        oRule = entity.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = entity.rule_007()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = entity.rule_008()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = entity.rule_009()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = entity.rule_010()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_011(self):
        oRule = entity.rule_011()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012(self):
        oRule = entity.rule_012()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = entity.rule_013()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = entity.rule_014()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015(self):
        oRule = entity.rule_015()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[103].line, 'end entity ENT1;')

    def test_fix_rule_016(self):
        oRule = entity.rule_016()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_017(self):
        oRule = entity.rule_017()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = entity.rule_018()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[21].line, '       G_GENERIC1 : std_logic :=\'0\';          -- Comment')
        self.assertEqual(oFile.lines[22].line, '    G_generic2 : std_logic := \'1\'             -- Comment')

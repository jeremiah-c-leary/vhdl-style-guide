import os

import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','entity','entity_test_input.vhd'))


class testFixRuleEntityMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_014_lowercase(self):
        oRule = entity.rule_014()
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[78].line, 'end entity entity1;')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014_uppercase(self):
        oRule = entity.rule_014()
        oRule.case = 'upper'
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[78].line, 'end ENTITY entity1;')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015(self):
        oRule = entity.rule_015()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[103].line, 'end entity ENT1;')

    def test_fix_rule_016(self):
        oRule = entity.rule_016()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_017(self):
        oRule = entity.rule_017()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = entity.rule_018()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[21].line, '       G_GENERIC1 : std_logic :=\'0\';-- Comment')
        self.assertEqual(self.oFile.lines[22].line, '    G_generic2 : std_logic    := \'1\'             -- Comment')

    def test_fix_rule_019(self):
        oRule = entity.rule_019()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[133].line, 'end entity entity1;')
        self.assertEqual(oRule.violations, [])

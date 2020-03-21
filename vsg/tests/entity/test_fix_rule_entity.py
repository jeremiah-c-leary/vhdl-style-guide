import os

import unittest

from vsg.rules import entity
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','entity','entity_test_input.vhd'))


class testFixRuleEntityMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = entity.rule_001()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = entity.rule_002()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = entity.rule_003()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = entity.rule_004()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = entity.rule_005()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[49].line, 'entity ENTITY1 is')
        self.assertEqual(self.oFile.lines[50].line, '   generic  (')

    def test_fix_rule_006_lowercase(self):
        oRule = entity.rule_006()
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[19].line, ' entITy   entiTY2  is')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006_uppercase(self):
        oRule = entity.rule_006()
        oRule.case = 'upper'
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[3].line, 'entity ENTITY1 IS')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = entity.rule_007()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = entity.rule_008()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = entity.rule_009()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = entity.rule_010()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_011(self):
        oRule = entity.rule_011()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_uppercase(self):
        oRule = entity.rule_012()
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[16].line, 'end entity ENTITY1')
        self.assertEqual(self.oFile.lines[33].line, ' end entity    ENTITY2')
        self.assertEqual(self.oFile.lines[47].line, ' END ENTITY ENTITY3')
        self.assertEqual(self.oFile.lines[63].line, 'End  entity  ENTITY1')
        self.assertEqual(self.oFile.lines[78].line, 'end ENtity ENTITY1')
        self.assertEqual(self.oFile.lines[91].line, 'end   entity ENTITY1')
        self.assertEqual(self.oFile.lines[103].line, 'end ENT1;')
        self.assertEqual(self.oFile.lines[123].line, 'end entity  ENTITY1')
        self.assertEqual(self.oFile.lines[146].line, 'end entity ENTITY1')

        self.assertEqual('Change entity name to uppercase.', oRule._get_solution(0))

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_lowercase(self):
        oRule = entity.rule_012()
        oRule.case = 'lower'
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[16].line, 'end entity entity1')
        self.assertEqual(self.oFile.lines[33].line, ' end entity    entity2')
        self.assertEqual(self.oFile.lines[47].line, ' END ENTITY entity3')
        self.assertEqual(self.oFile.lines[63].line, 'End  entity  entity1')
        self.assertEqual(self.oFile.lines[78].line, 'end ENtity entity1')
        self.assertEqual(self.oFile.lines[91].line, 'end   entity entity1')
        self.assertEqual(self.oFile.lines[103].line, 'end ent1;')
        self.assertEqual(self.oFile.lines[123].line, 'end entity  entity1')
        self.assertEqual(self.oFile.lines[146].line, 'end entity entity1')

        self.assertEqual('Change entity name to lowercase.', oRule._get_solution(0))

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = entity.rule_013()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014_lowercase(self):
        oRule = entity.rule_014()
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[78].line, 'end entity ENTITY1')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014_uppercase(self):
        oRule = entity.rule_014()
        oRule.case = 'upper'
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[78].line, 'end ENTITY ENTITY1')

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
        self.assertEqual(self.oFile.lines[133].line, 'end entity ENTITY1;')
        self.assertEqual(oRule.violations, [])

import os
import unittest

from vsg.rules import component
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_test_input.vhd'))
lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_comment_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(lFileComment)


class testFixRuleComponentMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_fix_rule_001(self):
        oRule = component.rule_001()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = component.rule_002()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = component.rule_003()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = component.rule_004()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = component.rule_005()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = component.rule_006()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = component.rule_007()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = component.rule_008()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = component.rule_009()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = component.rule_010()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_011(self):
        oRule = component.rule_011()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_upper(self):
        oRule = component.rule_012()
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[23].line, '  eNd comPonent COMP1;')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_lower(self):
        oRule = component.rule_012()
        oRule.case = 'lower'
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[23].line, '  eNd comPonent comp1;')
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = component.rule_013()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = component.rule_014()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

#    def test_fix_rule_015(self):
#        oRule = component.rule_015()
#        oRule.fix(self.oFile)
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016(self):
        oRule = component.rule_016()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_017(self):
        oRule = component.rule_017()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = component.rule_018()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_019(self):
        oRule = component.rule_019()
        oRule.fix(oFileComment)
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileComment.lines[7].line, '      generic_1 : std_logic := \'0\';')
        self.assertEqual(oFileComment.lines[12].line, '      port_2 : in    std_logic;')
        self.assertEqual(oFileComment.lines[14].line, '      port_4 : out   std_logic;')

    def test_fix_rule_020(self):
        oRule = component.rule_020()

        lFileComment = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'component_comment_test_input.vhd'))
        oFileComment = vhdlFile.vhdlFile(lFileComment)
        oRule.fix(oFileComment)
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileComment.lines[7].line, '      generic_1 : std_logic := \'0\'; -- This should be removed')
        self.assertEqual(oFileComment.lines[12].line, '      port_2 : in    std_logic;     -- This should be removed')
        self.assertEqual(oFileComment.lines[14].line, '      port_4 : out   std_logic;     -- This should be removed')

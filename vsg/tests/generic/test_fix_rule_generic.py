import os

import unittest

from vsg.rules import generic
from vsg import vhdlFile
from vsg.tests import utils


lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'generic_test_input.vhd'))
lFileMultiple = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'generic_multiple_on_one_line_test_input.vhd'))
oFileMultiple = vhdlFile.vhdlFile(lFileMultiple)


class testFixRuleGenericMethods(unittest.TestCase):


    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)


    def test_fix_rule_001(self):
        oRule = generic.rule_001()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertFalse(self.oFile.lines[81].isBlank)

    def test_fix_rule_002(self):
        oRule = generic.rule_002()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = generic.rule_003()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = generic.rule_004()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = generic.rule_005()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = generic.rule_006()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[37].line,'    G_GeneRIC2 :std_logic := \'1\'')
        self.assertEqual(self.oFile.lines[52].line,'    G_GENERIC1 :   STD_LOGIC := \'0\';')
        self.assertEqual(self.oFile.lines[53].line,'  G_GENERIC2 : std_logic := \'1\'')

    def test_fix_rule_007(self):
        oRule = generic.rule_007()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = generic.rule_008()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = generic.rule_009()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = generic.rule_010()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[98].indentLevel, self.oFile.lines[95].indentLevel)
        self.assertEqual(self.oFile.lines[99].indentLevel, self.oFile.lines[97].indentLevel - 1)

    def test_fix_rule_013(self):
        oRule = generic.rule_013()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[140].indentLevel, self.oFile.lines[139].indentLevel + 1)

    def test_fix_rule_014(self):
        oRule = generic.rule_014()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015(self):
        oRule = generic.rule_015()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016(self):
        oRule = generic.rule_016()
        oRule.fix(oFileMultiple)
        oRule.analyze(oFileMultiple)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileMultiple.lines[4].line,'  generic (')
        self.assertEqual(oFileMultiple.lines[5].line,'    G_GENERIC1 : std_logic := \'0\';')
        self.assertEqual(oFileMultiple.lines[6].line,'G_GENERIC2 : std_logic := \'1\';')
        self.assertEqual(oFileMultiple.lines[7].line,'G_GENERIC3 : std_logic := \'1\';')
        self.assertEqual(oFileMultiple.lines[8].line,'G_GENERIC4 : std_logic := \'1\';')
        self.assertEqual(oFileMultiple.lines[9].line,'G_GENERIC5 : std_logic := \'1\'')
        self.assertEqual(oFileMultiple.lines[10].line,'  );')

    def test_fix_rule_019(self):
        oRule = generic.rule_019()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(self.oFile.lines[172].line,'  );')
        self.assertEqual(self.oFile.lines[173].line,'  port (')

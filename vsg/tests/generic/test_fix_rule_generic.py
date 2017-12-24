import os

import unittest

from vsg.rules import generic
from vsg import vhdlFile


oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'generic_test_input.vhd'))
oFileMultiple = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'generic_multiple_on_one_line_test_input.vhd'))


class testFixRuleGenericMethods(unittest.TestCase):


    def test_fix_rule_001(self):
        oRule = generic.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertFalse(oFile.lines[81].isBlank)

    def test_fix_rule_002(self):
        oRule = generic.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = generic.rule_003()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = generic.rule_004()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = generic.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = generic.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[37].line,'    G_GeneRIC2 : std_logic := \'1\'')
        self.assertEqual(oFile.lines[52].line,'    G_GENERIC1 : STD_LOGIC := \'0\';')
        self.assertEqual(oFile.lines[53].line,'    G_GENERIC2 : std_logic := \'1\'')

    def test_fix_rule_007(self):
        oRule = generic.rule_007()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = generic.rule_008()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = generic.rule_009()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = generic.rule_010()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[96].indentLevel, oFile.lines[95].indentLevel)
        self.assertEqual(oFile.lines[97].indentLevel, oFile.lines[96].indentLevel - 1)

#    def test_fix_rule_011(self):
#        oRule = generic.rule_011()
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012(self):
        oRule = generic.rule_012()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = generic.rule_013()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[140].indentLevel, oFile.lines[139].indentLevel + 1)

    def test_fix_rule_014(self):
        oRule = generic.rule_014()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015(self):
        oRule = generic.rule_015()
        oRule.fix(oFile)
        oRule.analyze(oFile)
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

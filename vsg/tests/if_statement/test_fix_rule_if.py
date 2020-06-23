import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg import rule_list
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(lFileCase)
lFileCompress = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_compressed_line_test_input.vhd'))
oFileCompress = vhdlFile.vhdlFile(lFileCompress)
lFileNested = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_nested_test_input.vhd'))
oFileNested = vhdlFile.vhdlFile(lFileNested)
lFileIf = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_if_input.vhd'))
oFileIf = vhdlFile.vhdlFile(lFileIf)


class testFixRuleIfMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = if_statement.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = if_statement.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oFile.lines[13].line, '    if ( a = 1 or d = 20 or    -- this if should not be replaced')
        self.assertEqual(oFile.lines[14].line, '       g = 34 or x = 3000 ) then')
        self.assertEqual(oFile.lines[24].line, '   elsif ( z = 45 and f = 45 ) then')
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = if_statement.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = if_statement.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = if_statement.rule_005()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = if_statement.rule_006()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006_case(self):
        lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_case_test_input.vhd'))
        oFileCase = vhdlFile.vhdlFile(lFileCase)
        oRule = if_statement.rule_006()
        dExpected = []
        oRule.fix(oFileCase)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)
        self.assertTrue(oFileCase.lines[10].isBlank)
        self.assertTrue(oFileCase.lines[20].isBlank)

    def test_fix_rule_007(self):
        oRule = if_statement.rule_007()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007_case(self):
        lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_case_test_input.vhd'))
        oFileCase = vhdlFile.vhdlFile(lFileCase)
        oRule = if_statement.rule_007()
        dExpected = []
        oRule.fix(oFileCase)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)
        self.assertTrue(oFileCase.lines[18].isBlank)

    def test_fix_rule_008(self):
        oRule = if_statement.rule_008()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008_case(self):
        lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_case_test_input.vhd'))
        oFileCase = vhdlFile.vhdlFile(lFileCase)
        oRule = if_statement.rule_008()
        dExpected = []
        oRule.fix(oFileCase)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)
        self.assertTrue(oFileCase.lines[40].isBlank)

    def test_fix_rule_009(self):
        oRule = if_statement.rule_009()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = if_statement.rule_010()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010_case(self):
        lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_case_test_input.vhd'))
        oFileCase = vhdlFile.vhdlFile(lFileCase)
        oRule = if_statement.rule_010()
        dExpected = []
        oRule.fix(oFileCase)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)
        self.assertTrue(oFileCase.lines[29].isBlank)

    def test_fix_rule_011(self):
        oRule = if_statement.rule_011()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011_case(self):
        lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'if_case_test_input.vhd'))
        oFileCase = vhdlFile.vhdlFile(lFileCase)
        oRule = if_statement.rule_011()
        dExpected = []
        oRule.fix(oFileCase)
        oRule.analyze(oFileCase)
        self.assertEqual(oRule.violations, dExpected)
        self.assertTrue(oFileCase.lines[32].isBlank)

    def test_fix_rule_012(self):
        oRule = if_statement.rule_012()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = if_statement.rule_013()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_014(self):
        oRule = if_statement.rule_014()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_024(self):
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oFile = vhdlFile.vhdlFile(lFile)
        oRule = if_statement.rule_024()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[107].line, '    if (a = 2) then')
        self.assertEqual(oFile.lines[108].line, ' b <= \'1\'; else b <= \'0\'; end if;')
        self.assertEqual(oFile.lines[108].indentLevel, oFile.lines[107].indentLevel + 1)
        self.assertFalse(oFile.lines[107].isEndIfKeyword)
        self.assertFalse(oFile.lines[107].isElseKeyword)

    def test_fix_rule_021(self):
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oFile = vhdlFile.vhdlFile(lFile)
        oRule = if_statement.rule_021()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[105].line, '    if (a = 2) then b <= \'1\'; ')
        self.assertEqual(oFile.lines[106].line, 'else b <= \'0\'; end if;')
        self.assertEqual(oFile.lines[106].indentLevel, oFile.lines[105].indentLevel)


    def test_fix_rule_020(self):
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oFile = vhdlFile.vhdlFile(lFile)
        oRule = if_statement.rule_020()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_015(self):
        oRule = if_statement.rule_015()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_022(self):
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oFile = vhdlFile.vhdlFile(lFile)
        oRule = if_statement.rule_022()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[102].line, '    else')
        self.assertEqual(oFile.lines[103].line, ' g <= x;')
        self.assertEqual(oFile.lines[103].indentLevel, oFile.lines[102].indentLevel + 1)

    def test_fix_compressed_line(self):
        oRuleList = rule_list.rule_list(oFileCompress)
        oRuleList.fix()
#        utils.debug_lines(oFileCompress, 8, 23)
        self.assertEqual(oFileCompress.lines[9].line, '    if (A = \'1\' and B = \'1\') then')
        self.assertEqual(oFileCompress.lines[10].line, '      X <= \'1\';')
        self.assertFalse(oFileCompress.lines[10].isVariableAssignment)
        self.assertTrue(oFileCompress.lines[10].isSequential)
        self.assertEqual(oFileCompress.lines[11].line, '    elsif (C = \'0\') then')
        self.assertEqual(oFileCompress.lines[12].line, '      Y <= \'0\';')
        self.assertFalse(oFileCompress.lines[12].isVariableAssignment)
        self.assertTrue(oFileCompress.lines[12].isSequential)
        self.assertEqual(oFileCompress.lines[13].line, '    else')
        self.assertEqual(oFileCompress.lines[14].line, '      W := \'0\';')
        self.assertTrue(oFileCompress.lines[14].isVariableAssignment)
        self.assertFalse(oFileCompress.lines[14].isSequential)
        self.assertFalse(oFileCompress.lines[14].isLastEndIf)

        self.assertEqual(oFileCompress.lines[17].line, '    if (A = \'1\' and B = \'1\') then')
        self.assertEqual(oFileCompress.lines[18].line, '      X <= \'1\';')
        self.assertEqual(oFileCompress.lines[19].line, '    elsif (C = \'0\') then')
        self.assertEqual(oFileCompress.lines[20].line, '      Y <= \'0\';')
        self.assertEqual(oFileCompress.lines[21].line, '    else')
        self.assertEqual(oFileCompress.lines[22].line, '      W <= \'0\';')

    def test_fix_rule_025(self):
        oRule = if_statement.rule_025()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[13].line, '    if ( a = 1 or d = 20 or    -- this if should not be replaced')

    def test_fix_rule_026(self):
        oRule = if_statement.rule_026()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[24].line, '    elsif ( z = 45 and f = 45 ) then')

    def test_fix_rule_027(self):
        oRule = if_statement.rule_027()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[86].line, '    else')

    def test_fix_rule_028(self):
        oRule = if_statement.rule_028()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[17].line, '    end if;')

    def test_fix_rule_029(self):
        lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
        oFile = vhdlFile.vhdlFile(lFile)
        oRule = if_statement.rule_029()
        self.assertEqual(oFile.lines[14].line, '       g = 34 or x = 3000 THEN')
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[14].line, '       g = 34 or x = 3000 then')

    def test_rule_032(self):
        oRule = if_statement.rule_032()
        lExpected = []
        oRule.fix(oFileIf)
        oRule.analyze(oFileIf)
        self.assertEqual(oFileIf.lines[15].indentLevel, 2)
        self.assertEqual(oFileIf.lines[16].indentLevel, 2)
        self.assertEqual(oFileIf.lines[17].indentLevel, 2)

        self.assertEqual(oFileIf.lines[15].line, '    -- This is a comment')
        self.assertEqual(oFileIf.lines[16].line, '    -- to describe the elsif')
        self.assertEqual(oFileIf.lines[17].line, '    -- code')

        self.assertEqual(oFileIf.lines[20].indentLevel, 2)
        self.assertEqual(oFileIf.lines[21].indentLevel, 2)

        self.assertEqual(oFileIf.lines[20].line, '    -- Yet more code comments')
        self.assertEqual(oFileIf.lines[21].line, '    -- for the next elsif')

        self.assertEqual(oRule.violations, lExpected)

    def test_rule_033(self):
        oRule = if_statement.rule_033()
        lExpected = []
        oRule.fix(oFileIf)
        oRule.analyze(oFileIf)
        self.assertEqual(oFileIf.lines[24].indentLevel, 2)
        self.assertEqual(oFileIf.lines[25].indentLevel, 2)

        self.assertEqual(oFileIf.lines[24].line, '    -- and finally comments for the')
        self.assertEqual(oFileIf.lines[25].line, '    -- else code')

        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_034(self):
        oRule = if_statement.rule_034()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[27].line, '    end if;')

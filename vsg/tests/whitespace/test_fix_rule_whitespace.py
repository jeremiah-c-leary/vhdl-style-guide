import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import whitespace
from vsg import vhdlFile
from vsg import line

sFileName = os.path.join(os.path.dirname(__file__),'whitespace_test_input.txt')


class testFixRuleWhitespaceMethods(unittest.TestCase):

    def test_fix_001(self):
        oRule = whitespace.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '001')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oFile.lines.append(line.line('  This is a test of ending whitespace '))
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oFile.lines.append(line.line('  This is a test of ending whitespace  '))
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_002(self):
        oRule = whitespace.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '002')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  This is a test of tabs\t'))
        oFile.lines.append(line.line('\tThis is a test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oFile.lines.append(line.line('  This is a \t test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_003(self):
        oRule = whitespace.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '003')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  This is a test of tabs;'))
        oFile.lines.append(line.line('  This is a test of tabs ;'))
        oFile.lines.append(line.line('  This is a test of tabs;'))
        oFile.lines.append(line.line('  This is a test of tabs    ;'))
        oFile.lines.append(line.line('  This is a test; of tabs'))
        oFile.lines.append(line.line('  This is a test ; of tabs'))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_004(self):
        oRule = whitespace.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '004')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  This is a test of commas,'))
        oFile.lines.append(line.line('  This is a test of commas ,'))
        oFile.lines.append(line.line('  This is a test of commas,'))
        oFile.lines.append(line.line('  This is a test of commas    ,'))
        oFile.lines.append(line.line('  This is a test, of commas'))
        oFile.lines.append(line.line('  This is a test , of commas'))
        oFile.lines.append(line.line('  This is a test, of commas -- This is a comment ,'))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[7].line, '  This is a test, of commas -- This is a comment ,')

    def test_fix_007(self):
        oRule = whitespace.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '007')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  This is a test,of commas (failure )'))
        oFile.lines.append(line.line('  This is a test, of commas (pass)'))
        oFile.lines.append(line.line('  This is a test of commas,(failure   )'))
        oFile.lines.append(line.line('  This is a test of commas -- 1,2,3,4 (PASS)'))
        oFile.lines.append(line.line('   ) pass'))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_008(self):
        oRule = whitespace.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '008')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('A  std_logic_vector (7 downto 0)'))
        oFile.lines.append(line.line('  std_logic_vector(7 downto 0)'))
        oFile.lines.append(line.line('  std_logic_vector   (7 downto 0)'))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[1].line, 'A  std_logic_vector(7 downto 0)')
        self.assertEqual(oFile.lines[2].line, '  std_logic_vector(7 downto 0)')
        self.assertEqual(oFile.lines[3].line, '  std_logic_vector(7 downto 0)')

    def test_fix_009(self):
        oRule = whitespace.rule_009()

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  a <= b& c -- this is an& comment'))
        oFile.lines.append(line.line('  a <= b & c&d&e -- this should not be caught& '))
        oFile.lines.append(line.line('  a <= b &c'))
        oFile.lines.append(line.line('  a <= b&c'))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[1].line, '  a <= b & c -- this is an& comment')
        self.assertEqual(oFile.lines[2].line, '  a <= b & c &d &e -- this should not be caught& ')
        self.assertEqual(oFile.lines[3].line, '  a <= b &c')
        self.assertEqual(oFile.lines[4].line, '  a <= b &c')

    def test_fix_010(self):
        oRule = whitespace.rule_010()

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  a <= b &c -- this is an &comment'))
        oFile.lines.append(line.line('  a <= b &c&d&e -- this should not be &caught '))
        oFile.lines.append(line.line('  a <= b &c'))
        oFile.lines.append(line.line('  a <= b &'))
        oFile.lines.append(line.line('  a <= b & '))
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[1].line, '  a <= b & c -- this is an &comment')
        self.assertEqual(oFile.lines[2].line, '  a <= b & c& d& e -- this should not be &caught ')
        self.assertEqual(oFile.lines[3].line, '  a <= b & c')
        self.assertEqual(oFile.lines[4].line, '  a <= b &')
        self.assertEqual(oFile.lines[5].line, '  a <= b & ')

    def test_fix_011(self):
        oRule = whitespace.rule_011()

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = []
        oFile.lines.append(line.line('  a <= b+ c'))   #1
        oFile.lines.append(line.line('  a <= b +c'))   #2
        oFile.lines.append(line.line('  a <= b + c'))  #3
        oFile.lines.append(line.line('  a <= b+c'))    #4
        oFile.lines.append(line.line('  a <= b- c'))   #5
        oFile.lines.append(line.line('  a <= b -c'))   #6
        oFile.lines.append(line.line('  a <= b - c'))  #7
        oFile.lines.append(line.line('  a <= b-c'))    #8
        oFile.lines.append(line.line('  a <= b/ c'))   #9
        oFile.lines.append(line.line('  a <= b /c'))   #10
        oFile.lines.append(line.line('  a <= b / c'))  #11
        oFile.lines.append(line.line('  a <= b/c'))    #12
        oFile.lines.append(line.line('  a <= b* c'))   #13
        oFile.lines.append(line.line('  a <= b *c'))   #14
        oFile.lines.append(line.line('  a <= b * c'))  #15
        oFile.lines.append(line.line('  a <= b*c'))    #16
        oFile.lines.append(line.line('  a <= b** c'))   #17
        oFile.lines.append(line.line('  a <= b **c'))   #18
        oFile.lines.append(line.line('  a <= b ** c'))  #19
        oFile.lines.append(line.line('  a <= b**c'))    #20
        oFile.lines.append(line.line('  a <= b**c -- This**is fine'))    #21
        oFile.lines.append(line.line('  a <= b ** c -- This**is fine'))    #22
        oFile.lines.append(line.line('  a <= )+ ('))   #23
        oFile.lines.append(line.line('  a <= ) +('))   #24
        oFile.lines.append(line.line('  a <= ) + ('))  #25
        oFile.lines.append(line.line('  a <= )+('))    #26
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFile.lines[1].line, '  a <= b + c')
        self.assertEqual(oFile.lines[2].line, '  a <= b + c')
        self.assertEqual(oFile.lines[3].line, '  a <= b + c')
        self.assertEqual(oFile.lines[4].line, '  a <= b + c')
        self.assertEqual(oFile.lines[5].line, '  a <= b - c')
        self.assertEqual(oFile.lines[6].line, '  a <= b - c')
        self.assertEqual(oFile.lines[7].line, '  a <= b - c')
        self.assertEqual(oFile.lines[8].line, '  a <= b - c')
        self.assertEqual(oFile.lines[9].line, '  a <= b / c')
        self.assertEqual(oFile.lines[10].line, '  a <= b / c')
        self.assertEqual(oFile.lines[11].line, '  a <= b / c')
        self.assertEqual(oFile.lines[12].line, '  a <= b / c')
        self.assertEqual(oFile.lines[13].line, '  a <= b * c')
        self.assertEqual(oFile.lines[14].line, '  a <= b * c')
        self.assertEqual(oFile.lines[15].line, '  a <= b * c')
        self.assertEqual(oFile.lines[16].line, '  a <= b * c')
        self.assertEqual(oFile.lines[17].line, '  a <= b ** c')
        self.assertEqual(oFile.lines[18].line, '  a <= b ** c')
        self.assertEqual(oFile.lines[19].line, '  a <= b ** c')
        self.assertEqual(oFile.lines[20].line, '  a <= b ** c')
        self.assertEqual(oFile.lines[21].line, '  a <= b ** c -- This**is fine')
        self.assertEqual(oFile.lines[22].line, '  a <= b ** c -- This**is fine')
        self.assertEqual(oFile.lines[23].line, '  a <= ) + (')
        self.assertEqual(oFile.lines[24].line, '  a <= ) + (')
        self.assertEqual(oFile.lines[25].line, '  a <= ) + (')
        self.assertEqual(oFile.lines[26].line, '  a <= ) + (')

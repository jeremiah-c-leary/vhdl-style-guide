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

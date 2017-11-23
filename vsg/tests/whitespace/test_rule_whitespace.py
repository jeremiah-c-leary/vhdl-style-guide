import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import whitespace
from vsg import vhdlFile
from vsg import line

sFileName = os.path.join(os.path.dirname(__file__),'..','whitespace','whitespace_test_input.txt')

class testRuleWhitespaceMethods(unittest.TestCase):

    def test_001(self):
        oRule = whitespace.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '001')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = [2,4]
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oFile.lines.append(line.line('  This is a test of ending whitespace '))
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oFile.lines.append(line.line('  This is a test of ending whitespace  '))
        oFile.lines.append(line.line('  This is a test of ending whitespace'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_002(self):
        oRule = whitespace.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '002')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = [1,2,5]
        oFile.lines.append(line.line('  This is a test of tabs\t'))
        oFile.lines.append(line.line('\tThis is a test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oFile.lines.append(line.line('  This is a \t test of tabs'))
        oFile.lines.append(line.line('  This is a test of tabs'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_003(self):
        oRule = whitespace.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '003')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = [2,4,6]
        oFile.lines.append(line.line('  This is a test of tabs;'))
        oFile.lines.append(line.line('  This is a test of tabs ;'))
        oFile.lines.append(line.line('  This is a test of tabs;'))
        oFile.lines.append(line.line('  This is a test of tabs    ;'))
        oFile.lines.append(line.line('  This is a test; of tabs'))
        oFile.lines.append(line.line('  This is a test ; of tabs'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_004(self):
        oRule = whitespace.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '004')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = [2,4,6]
        oFile.lines.append(line.line('  This is a test of tabs,'))
        oFile.lines.append(line.line('  This is a test of tabs ,'))
        oFile.lines.append(line.line('  This is a test of tabs,'))
        oFile.lines.append(line.line('  This is a test of tabs    ,'))
        oFile.lines.append(line.line('  This is a test, of tabs'))
        oFile.lines.append(line.line('  This is a test , of tabs'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_005(self):
        oRule = whitespace.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '005')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = [1,3,5]
        oFile.lines.append(line.line('  This is a test of parenthesis ( failure'))
        oFile.lines.append(line.line('  This is a test of parenthesis (pass'))
        oFile.lines.append(line.line('  This is a test of parentehsis (  failure'))
        oFile.lines.append(line.line('  This is a test of parentehsis (  7 pass'))
        oFile.lines.append(line.line('  This is a test of parenthesis ( pass) --  ( pass'))
        oFile.lines[5].hasComment = True
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[1].line, '  This is a test of parenthesis (failure')
        self.assertEqual(oFile.lines[2].line, '  This is a test of parenthesis (pass')
        self.assertEqual(oFile.lines[3].line, '  This is a test of parentehsis (failure')
        self.assertEqual(oFile.lines[4].line, '  This is a test of parentehsis (  7 pass')
        self.assertEqual(oFile.lines[5].line, '  This is a test of parenthesis (pass) --  ( pass')

    def test_006(self):
        oRule = whitespace.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '006')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = [1,3,5]
        oFile.lines.append(line.line('  This is a test of parenthesis (failure )'))
        oFile.lines.append(line.line('  This is a test of parenthesis (pass)'))
        oFile.lines.append(line.line('  This is a test of parentehsis (failure   )'))
        oFile.lines.append(line.line('   ) pass'))
        oFile.lines.append(line.line('  This is a test of parentehsis (pass ) --  ) pass'))
        oFile.lines[5].hasComment = True
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[1].line, '  This is a test of parenthesis (failure)')
        self.assertEqual(oFile.lines[2].line, '  This is a test of parenthesis (pass)')
        self.assertEqual(oFile.lines[3].line, '  This is a test of parentehsis (failure)')
        self.assertEqual(oFile.lines[4].line, '   ) pass')
        self.assertEqual(oFile.lines[5].line, '  This is a test of parentehsis (pass) --  ) pass')

    def test_007(self):
        oRule = whitespace.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'whitespace')
        self.assertEqual(oRule.identifier, '007')

        oFile = vhdlFile.vhdlFile(sFileName)

        dExpected = [1,3]
        oFile.lines.append(line.line('  This is a test,of commas (failure )'))
        oFile.lines.append(line.line('  This is a test, of commas (pass)'))
        oFile.lines.append(line.line('  This is a test of commas,(failure   )'))
        oFile.lines.append(line.line('  This is a test of commas -- 1,2,3,4 (PASS)'))
        oFile.lines.append(line.line('   ) pass'))
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

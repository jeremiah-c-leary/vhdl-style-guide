import os

import unittest

from vsg.rules import port
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input.vhd'))
oFile_rule_016 = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','port','port_test_input.vhd'))


class testFixRulePortMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = port.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = port.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = port.rule_003()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = port.rule_004()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = port.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = port.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = port.rule_007()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = port.rule_008()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = port.rule_009()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = port.rule_010()
        oRule.fix(oFile)
        self.assertEqual(oFile.lines[27].line, '    IO_PORT3(c_index) : inout NATURAL;')
        self.assertEqual(oFile.lines[28].line, '    PORT4(c_index) : in    INTEGER;')
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

#### RULE 11 and RULE 12 will be fixed as they would modify code.
#    def test_fix_rule_011_prefix(self):
#        oRule = port.rule_011()
#        oRule.fix(oFile)
#        dExpected = [12,13,14,29,30,31,43,44,45,60,61,62,74,75,76,99,100,101]
#        oRule.anal[](oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
#    def test_fix_rule_011_none(self):
#        oRule = port.rule_011()
#        oRule.fix(oFile)
#
#    def test_fix_rule_011_suf[](self):
#        oRule = port.rule_011()
#        oRule.port_direction = 'Suffix'
#
#        dExpected = [9,10,11,12,13,14,26,27,28,29,30,31,40,41,42,43,44,45,57,58,59,60,61,62,71,72,73,74,75,76,87,88,89,119,120,121,129,130,131,141,142]
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)

#    def test_fix_rule_012(self):
#        oRule = port.rule_012()
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = port.rule_013()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = port.rule_014()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertFalse(oFile.lines[30].isEndPortMap)
        self.assertTrue(oFile.lines[30].isPortDeclaration)
        self.assertEqual(oFile.lines[30].indentLevel, oFile.lines[29].indentLevel)
        self.assertTrue(oFile.lines[31].insidePortMap)
        self.assertTrue(oFile.lines[31].isEndPortMap)
        self.assertEqual(oFile.lines[31].insideEntity, oFile.lines[30].insideEntity)
        self.assertFalse(oFile.lines[31].isPortDeclaration)
        self.assertEqual(oFile.lines[31].indentLevel, oFile.lines[29].indentLevel - 1)

    def test_fix_rule_015(self):
        oRule = port.rule_015()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016(self):
        oRule = port.rule_016()
        oRule.fix(oFile_rule_016)
        oRule.analyze(oFile_rule_016)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile_rule_016.lines[140].indentLevel + 1, oFile_rule_016.lines[141].indentLevel)

    def test_fix_rule_017(self):
        oRule = port.rule_017()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = port.rule_018()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_019(self):
        oRule = port.rule_019()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_020(self):
        oRule = port.rule_020()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_021(self):
        oRule = port.rule_021()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[152].line, '  port (')
        self.assertEqual(oFile.lines[153].line, '    PORT1 : in    std_logic')

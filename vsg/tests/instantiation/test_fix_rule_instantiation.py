import os

import unittest

from vsg.rules import instantiation
from vsg import vhdlFile

oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_test_input.vhd'))
oFileGeneric = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','instantiation','instantiation_generic_test_input.vhd'))
oFileComment = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'instantiation_comment_test_input.vhd'))
oFileDirect = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'instantiation_direct_test_input.vhd'))

class testFixRuleInstantiationMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = instantiation.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_002(self):
        oRule = instantiation.rule_002()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_003(self):
        oRule = instantiation.rule_003()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_004(self):
        oRule = instantiation.rule_004()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005(self):
        oRule = instantiation.rule_005()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006(self):
        oRule = instantiation.rule_006()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_007(self):
        oRule = instantiation.rule_007()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_008(self):
        oRule = instantiation.rule_008()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_009(self):
        oRule = instantiation.rule_009()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_010(self):
        oRule = instantiation.rule_010()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_011(self):
        oRule = instantiation.rule_011()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        # Note: the line below can change if this test is ran individually
        self.assertEqual(oFile.lines[76].line, '      PORT_1(c_index)     => w_port_1,')

    def test_fix_rule_012(self):
        oRule = instantiation.rule_012()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013(self):
        oRule = instantiation.rule_013()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_014(self):
        oRule = instantiation.rule_014()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015(self):
        oRule = instantiation.rule_015()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016(self):
        oRule = instantiation.rule_016()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_017(self):
        oRule = instantiation.rule_017()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_001_generics(self):
        oRule = instantiation.rule_001()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018(self):
        oRule = instantiation.rule_018()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_019(self):
        oRule = instantiation.rule_019()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_020(self):
        oRule = instantiation.rule_020()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[64].indentLevel, oFile.lines[63].indentLevel + 1)

    def test_fix_rule_021(self):
        oRule = instantiation.rule_021()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFile.lines[85].line,'      PORT_1 => w_port_1,')
        self.assertEqual(oFile.lines[86].line,' PORT_2 => w_port_2,')
        self.assertEqual(oFile.lines[87].line,'      PORT_3 => w_port_3,')

    def test_fix_rule_022(self):
        oRule = instantiation.rule_022()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_023(self):
        oRule = instantiation.rule_023()
        oRule.fix(oFileComment)
        oRule.analyze(oFileComment)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileComment.lines[24].line,'      generic_1 => \'0\',')
        self.assertFalse(oFileComment.lines[24].hasComment)
        self.assertFalse(oFileComment.lines[24].hasInlineComment)
        self.assertEqual(oFileComment.lines[29].line,'      port_2 => \'1\',')
        self.assertFalse(oFileComment.lines[29].hasComment)
        self.assertFalse(oFileComment.lines[29].hasInlineComment)
        self.assertEqual(oFileComment.lines[31].line,'      port_4 => \'1\'')
        self.assertFalse(oFileComment.lines[31].hasComment)
        self.assertFalse(oFileComment.lines[31].hasInlineComment)

    def test_fix_fule_025(self):
        oRule = instantiation.rule_025()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileGeneric.lines[81].line, '    generic map (')
        self.assertEqual(oFileGeneric.lines[82].line, '      GENERIC_1 => generic_1,')

    def test_fix_fule_026(self):
        oRule = instantiation.rule_026()
        oRule.fix(oFileGeneric)
        oRule.analyze(oFileGeneric)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileGeneric.lines[85].line, '    port map (')
        self.assertEqual(oFileGeneric.lines[86].line, '      PORT_1 => w_port_1,')

    def test_fix_fule_027(self):
        oRule = instantiation.rule_027()
        oRule.fix(oFileDirect)
        oRule.analyze(oFileDirect)
        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileDirect.lines[13].line, '  U_INST1 : entity library.INST1')
        self.assertEqual(oFileDirect.lines[13].line, '  U_INST1 : entity library.INST1')

    def test_fix_fule_028(self):
        oRule = instantiation.rule_028()
        oRule.fix(oFileDirect)
        oRule.analyze(oFileDirect)
#        self.assertEqual(oRule.violations, [])
        self.assertEqual(oFileDirect.lines[20].line, '  U_INST1 : entity library.INST1')


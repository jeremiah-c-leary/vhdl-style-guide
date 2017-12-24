import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'architecture_test_input.vhd'))
oFileRule010 = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'architecture_test_input.vhd'))
oFileIs = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'architecture_is_test_input.vhd'))


class testFixRuleArchitectureMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = architecture.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = architecture.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = architecture.rule_003()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = architecture.rule_004()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

#    def test_fix_rule_005(self):
#        oRule = architecture.rule_005()
#        dExpected = []
#        oRule.fix(oFile)
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, dExpected)
#
    def test_fix_rule_006(self):
        oRule = architecture.rule_006()
        dExpected = []
        oRule.fix(oFileIs)
        oRule.analyze(oFileIs)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(oFileIs.lines[2].line, 'architecture RTL of FIFO is')
        self.assertEqual(oFileIs.lines[3].line, '')
        self.assertEqual(oFileIs.lines[3].isBlank, True)
        self.assertEqual(oFileIs.lines[9].line, 'architecture RTL of FIFO is')

    def test_fix_rule_007(self):
        oRule = architecture.rule_007()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = architecture.rule_008()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = architecture.rule_009()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = architecture.rule_010()
        dExpected = []
        oRule.fix(oFileRule010)
        oRule.analyze(oFileRule010)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_011(self):
        oRule = architecture.rule_011()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_012(self):
        oRule = architecture.rule_012()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = architecture.rule_013()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_014(self):
        oRule = architecture.rule_014()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_015(self):
        oRule = architecture.rule_015()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_016(self):
        oRule = architecture.rule_016()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_017(self):
        oRule = architecture.rule_017()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_018(self):
        oRule = architecture.rule_018()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_019(self):
        oRule = architecture.rule_019()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_020(self):
        oRule = architecture.rule_020()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_021(self):
        oRule = architecture.rule_021()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_022(self):
        oRule = architecture.rule_022()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_023(self):
        oRule = architecture.rule_023()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_024(self):
        oRule = architecture.rule_024()
        dExpected = [13,71]
        oRule.fix(oFile)
        oRule.analyze(oFileRule010)
        self.assertEqual(oRule.violations, dExpected)


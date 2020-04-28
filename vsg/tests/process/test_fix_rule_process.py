import os

import unittest
from vsg.rules import process
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'process_test_input.vhd'))
lFileEvent = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'process_event_test_input.vhd'))


class testFixRuleProcessMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.oFileEvent = vhdlFile.vhdlFile(lFileEvent)

    def test_fix_rule_001(self):
        oRule = process.rule_001()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = process.rule_002()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_003(self):
        oRule = process.rule_003()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_004(self):
        oRule = process.rule_004()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_005(self):
        oRule = process.rule_005()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_006(self):
        oRule = process.rule_006()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_007(self):
        oRule = process.rule_007()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_008(self):
        oRule = process.rule_008()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_009(self):
        oRule = process.rule_009()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_010(self):
        oRule = process.rule_010()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)
        self.assertFalse(self.oFile.lines[6].isProcessBegin)
        self.assertTrue(self.oFile.lines[6].isProcessKeyword)
        self.assertTrue(self.oFile.lines[7].isProcessBegin)
        self.assertFalse(self.oFile.lines[7].isProcessKeyword)
        self.assertEqual(self.oFile.lines[7].indentLevel, self.oFile.lines[6].indentLevel)

    def test_fix_rule_011(self):
        oRule = process.rule_011()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_012(self):
        oRule = process.rule_012()
        dExpected = []
        self.assertFalse(self.oFile.lines[51].isProcessIs)
        self.assertFalse(self.oFile.lines[57].isProcessIs)
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[51].line, '  process (one, two, three) is ')
        self.assertEqual(self.oFile.lines[57].line, '           three) is ')
        self.assertTrue(self.oFile.lines[51].isProcessIs)
        self.assertTrue(self.oFile.lines[57].isProcessIs)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_013(self):
        oRule = process.rule_013()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_014(self):
        oRule = process.rule_014()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_015(self):
        oRule = process.rule_015()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_017(self):
        oRule = process.rule_017()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_019(self):
        oRule = process.rule_019()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_020(self):
        oRule = process.rule_020()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_021(self):
        oRule = process.rule_021()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_022(self):
        oRule = process.rule_022()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_023(self):
        oRule = process.rule_023()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_024(self):
        oRule = process.rule_024()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_025(self):
        oRule = process.rule_025()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_026(self):
        oRule = process.rule_026()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_027(self):
        oRule = process.rule_027()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_028(self):
        oRule = process.rule_028()
        dExpected = []
        oRule.fix(self.oFile)
        self.assertEqual(self.oFile.lines[27].line, '             ) iS')
        self.assertEqual(self.oFile.lines[33].line, '        )   Is -- This is a comment')

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_029_event(self):
        oRule = process.rule_029()
        dExpected = []
        oRule.fix(self.oFileEvent)
        oRule.analyze(self.oFileEvent)
        self.assertEqual(oRule.violations, dExpected)
        self.assertEqual(self.oFileEvent.lines[9].line, '    if (CLK\'event and CLK = \'1\') then')
        self.assertEqual(self.oFileEvent.lines[13].line, '    if (CLK\'event and CLK = \'0\') then')
        self.assertEqual(self.oFileEvent.lines[34].line, '    if (q_ff.some_flop\'event and q_ff.some_flop = \'1\') then')
        self.assertEqual(self.oFileEvent.lines[44].line, '    elsif (q_ff.some_flop\'event and q_ff.some_flop = \'0\') then')

    def test_fix_rule_029_edge(self):
        oRule = process.rule_029()
        oRule.clock = 'edge'
        dExpected = []
        oRule.fix(self.oFileEvent)
        self.assertEqual(self.oFileEvent.lines[17].line, '    if (rising_edge(CLK)) then')
        self.assertEqual(self.oFileEvent.lines[21].line, '    if (falling_edge(CLK)) then')
        self.assertEqual(self.oFileEvent.lines[38].line, '    if (rising_edge(q_ff.some_flop)) then')
        self.assertEqual(self.oFileEvent.lines[50].line, '    elsif (falling_edge(q_ff.some_flop)) then')

        oRule.analyze(self.oFileEvent)
        self.assertEqual(oRule.violations, dExpected)

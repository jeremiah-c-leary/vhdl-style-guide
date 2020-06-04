import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'multi_line_signal_test_input.vhd'))

class testGeneralRule(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_015_consecutive_default(self):
        oRule = signal.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [5,8,79]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_consecutive_1(self):
        oRule = signal.rule_015()
        oRule.consecutive = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '015')
        dExpected = [5,8,40,42,45,49,54,60,67,75,79]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_015_default(self):
        oRule = signal.rule_015()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[5].line, '  signal sig1 : std_logic;')
        self.assertTrue(self.oFile.lines[5].isSignal)
        self.assertTrue(self.oFile.lines[5].insideSignal)
        self.assertTrue(self.oFile.lines[5].isEndSignal)
        self.assertFalse(self.oFile.lines[5].isComment)
        self.assertFalse(self.oFile.lines[5].hasComment)
        self.assertFalse(self.oFile.lines[5].hasInlineComment)
        self.assertEqual(self.oFile.lines[5].commentColumn, None)
        self.assertFalse(self.oFile.lines[5].isBlank)
        self.assertEqual(self.oFile.lines[6].line, '  signal sig2 : std_logic;')
        self.assertEqual(self.oFile.lines[7].line, '  signal sig3 : std_logic;')
        self.assertEqual(self.oFile.lines[8].line, '  signal sig4 : std_logic;')
        self.assertEqual(self.oFile.lines[9].line, '  signal sig5 : std_logic;')
        self.assertEqual(self.oFile.lines[10].line, '  signal sig6 : std_logic;')

        self.assertEqual(self.oFile.lines[12].line, '  signal siga : std_logic; -- This is a comment')
        self.assertFalse(self.oFile.lines[12].isComment)
        self.assertTrue(self.oFile.lines[12].hasComment)
        self.assertTrue(self.oFile.lines[12].hasInlineComment)
        self.assertEqual(self.oFile.lines[12].commentColumn, 27)
        self.assertEqual(self.oFile.lines[13].line, '  signal sigb : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[14].line, '  signal sigc : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[15].line, '  signal sigd : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[16].line, '  signal sige : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[17].line, '  signal sigf : std_logic; -- This is a comment')

        self.assertEqual(self.oFile.lines[83].line, '  signal foo : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);')
        self.assertEqual(self.oFile.lines[84].line, '  signal bar : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);')
        self.assertEqual(self.oFile.lines[85].line, '  signal mine : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);')
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_015_default_consecutive_1(self):
        oRule = signal.rule_015()
        oRule.consecutive = 1
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[5].line, '  signal sig1 : std_logic;')
        self.assertEqual(self.oFile.lines[6].line, '  signal sig2 : std_logic;')
        self.assertEqual(self.oFile.lines[7].line, '  signal sig3 : std_logic;')
        self.assertEqual(self.oFile.lines[8].line, '  signal sig4 : std_logic;')
        self.assertEqual(self.oFile.lines[9].line, '  signal sig5 : std_logic;')
        self.assertEqual(self.oFile.lines[10].line, '  signal sig6 : std_logic;')

        self.assertEqual(self.oFile.lines[12].line, '  signal siga : std_logic; -- This is a comment')
        self.assertFalse(self.oFile.lines[12].isComment)
        self.assertTrue(self.oFile.lines[12].hasComment)
        self.assertTrue(self.oFile.lines[12].hasInlineComment)
        self.assertEqual(self.oFile.lines[12].commentColumn, 27)
        self.assertEqual(self.oFile.lines[13].line, '  signal sigb : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[14].line, '  signal sigc : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[15].line, '  signal sigd : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[16].line, '  signal sige : std_logic; -- This is a comment')
        self.assertEqual(self.oFile.lines[17].line, '  signal sigf : std_logic; -- This is a comment')

        self.assertEqual(self.oFile.lines[44].line, '  signal sig1 : std_logic;')
        self.assertEqual(self.oFile.lines[45].line, '  signal sig2 : std_logic;')

        self.assertEqual(self.oFile.lines[47].line, '  signal sig1 : std_logic    ;')
        self.assertEqual(self.oFile.lines[48].line, '  signal sig2 : std_logic    ;')

        self.assertEqual(self.oFile.lines[50].line, '  signal sig1 : std_logic    ;')
        self.assertEqual(self.oFile.lines[51].line, '  signal sig2 : std_logic    ;')

        self.assertEqual(self.oFile.lines[53].line, '  signal sig1 : std_logic    ;')
        self.assertEqual(self.oFile.lines[54].line, '  signal sig2 : std_logic    ;')

        self.assertEqual(self.oFile.lines[56].line, '  signal sig1 : std_logic    ;')
        self.assertEqual(self.oFile.lines[57].line, '  signal sig2 : std_logic    ;')

        self.assertEqual(self.oFile.lines[59].line, '  signal sig1 : std_logic    ;')
        self.assertEqual(self.oFile.lines[60].line, '  signal sig2 : std_logic    ;')

        self.assertEqual(self.oFile.lines[62].line, '  signal sig1 : std_logic    ;')
        self.assertEqual(self.oFile.lines[63].line, '  signal sig2 : std_logic    ;')

        self.assertEqual(self.oFile.lines[65].line, '  signal sig1 : std_logic; -- Comma, should not induce a failure')
        self.assertEqual(self.oFile.lines[66].line, '  signal sig2 : std_logic; -- Comma, should not induce a failure')

        self.assertEqual(oRule.violations, [])

    def test_rule_016(self):
        oRule = signal.rule_016()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '016')
        dExpected = [5,8,20,23,27,32,42,45,49,54,60,67]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_016(self):
        oRule = signal.rule_016()
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual(self.oFile.lines[5].line, '  signal sig1, sig2, sig3,     sig4, sig5, sig6 : std_logic;')
        self.assertTrue(self.oFile.lines[5].isSignal)
        self.assertTrue(self.oFile.lines[5].insideSignal)
        self.assertTrue(self.oFile.lines[5].isEndSignal)
        self.assertEqual(self.oFile.lines[7].line, '  signal siga, sigb,     sigc,     sigd,     sige,     sigf     : std_logic; -- This is a comment')
        self.assertTrue(self.oFile.lines[7].isSignal)
        self.assertTrue(self.oFile.lines[7].insideSignal)
        self.assertTrue(self.oFile.lines[7].isEndSignal)
        self.assertFalse(self.oFile.lines[7].isComment)
        self.assertTrue(self.oFile.lines[7].hasComment)
        self.assertTrue(self.oFile.lines[7].hasInlineComment)
        self.assertEqual(self.oFile.lines[7].commentColumn, 77)

        self.assertEqual(self.oFile.lines[12].line, '  signal sig1 : std_logic;')
        self.assertEqual(self.oFile.lines[14].line, '  signal sig1 : std_logic    ;')
        self.assertEqual(self.oFile.lines[16].line, '  signal sig1 :    std_logic    ;')
        self.assertEqual(self.oFile.lines[18].line, '  signal sig1    :    std_logic    ;')
        self.assertEqual(self.oFile.lines[20].line, '  signal    sig1    :    std_logic    ;')
        self.assertEqual(self.oFile.lines[24].line, '  signal sig1, sig2 : std_logic;')
        self.assertEqual(self.oFile.lines[26].line, '  signal sig1, sig2 : std_logic    ;')
        self.assertEqual(self.oFile.lines[28].line, '  signal sig1, sig2 :    std_logic    ;')
        self.assertEqual(self.oFile.lines[30].line, '  signal sig1, sig2    :    std_logic    ;')
        self.assertEqual(self.oFile.lines[32].line, '  signal sig1,    sig2    :    std_logic    ;')
        self.assertEqual(self.oFile.lines[34].line, '  signal sig1    ,    sig2    :    std_logic    ;')
        self.assertEqual(self.oFile.lines[36].line, '  signal    sig1    ,    sig2    :    std_logic    ;')

        self.assertEqual(oRule.violations, [])

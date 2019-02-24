import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

class testFixRuleSignalMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'multi_signal_test_input.vhd'))
        self.oFile = vhdlFile.vhdlFile(self.lFile) 

    def test_rule_012(self):
        oRule = signal.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '012')
        dExpected = [5,6,7,8]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_012(self):
        oRule = signal.rule_012()
        dExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[5].line,'  signal e_sig1,      d_sig2 : std_logic;')
        self.assertEqual(self.oFile.lines[6].line,'  signal a_sig10,     c_sig2 : std_logic;')
        self.assertEqual(self.oFile.lines[7].line,'  signal b_sig100,    b_sig2 : std_logic_vector (31 downto 0);')
        self.assertEqual(self.oFile.lines[8].line,'  signal c_sig1000,   a_sig2 : std_logic;')
        self.assertEqual(oRule.violations, dExpected)

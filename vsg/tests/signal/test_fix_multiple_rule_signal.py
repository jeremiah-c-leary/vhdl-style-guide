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
        lExpected = []
 
        dViolation = utils.add_violation(5)
        dViolation['comma'] = 16
        dViolation['max'] = 23
        dViolation['signal'] = 18
        lExpected.append(dViolation)

        dViolation = utils.add_violation(6)
        dViolation['comma'] = 17
        dViolation['max'] = 23
        dViolation['signal'] = 19
        lExpected.append(dViolation)

        dViolation = utils.add_violation(7)
        dViolation['comma'] = 18
        dViolation['max'] = 23
        dViolation['signal'] = 20
        lExpected.append(dViolation)

        dViolation = utils.add_violation(8)
        dViolation['comma'] = 19
        dViolation['max'] = 23
        dViolation['signal'] = 21
        lExpected.append(dViolation)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

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

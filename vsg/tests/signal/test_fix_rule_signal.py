import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','signal','signal_test_input.vhd'))

class testFixRuleSignalMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(lFile)


    def test_fix_rule_010(self):
        oRule = signal.rule_010()
        lExpected = []
        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)
        self.assertEqual(self.oFile.lines[12].line, '  signal   SIg : std_logic_vector(31 downto 0);')
        self.assertEqual(self.oFile.lines[16].line, '  signal sig :   std_logic_vector (31 downto 0) := (others => \'0\');')
        self.assertEqual(self.oFile.lines[20].line, '  signal b_siG100, b_Sig2 :std_logic_vector (31 downto 0);')
        self.assertEqual(self.oFile.lines[23].line, '  signal w_sig1 : t_User_Defined_Type;')
        self.assertEqual(oRule.violations, lExpected)


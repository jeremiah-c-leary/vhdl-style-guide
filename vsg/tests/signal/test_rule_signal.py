import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'signal_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleSignalMethods(unittest.TestCase):


    def test_rule_010(self):
        oRule = signal.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '010')
        lExpected = []
        dViolation = utils.add_violation(12)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(16)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

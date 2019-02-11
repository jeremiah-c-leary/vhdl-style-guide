import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile

class testFixRuleSignalMethods(unittest.TestCase):

    def setUp(self):
        # Read in test file used for all tests
        self.oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'multi_signal_test_input.vhd'))

    def test_rule_012(self):
        oRule = signal.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '012')
        dExpected = [5,6,7,8]
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, dExpected)

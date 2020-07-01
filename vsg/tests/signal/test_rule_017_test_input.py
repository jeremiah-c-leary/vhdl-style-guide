import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'rule_017_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRule(unittest.TestCase):

    def test_rule_017(self):
        oRule = signal.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '017')
        lExpected = utils.add_violation_list([6, 17, 20])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

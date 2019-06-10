import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import after
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'after_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleAfterMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = signal.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'after')
        self.assertEqual(oRule.identifier, '001')
        lExpected = [32, 33]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

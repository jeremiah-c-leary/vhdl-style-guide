import os
import unittest

from vsg.rules import sequential
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','sequential','sequential_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleSequentialMethods(unittest.TestCase):

    def test_rule_004(self):
        oRule = sequential.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([54,55,74])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

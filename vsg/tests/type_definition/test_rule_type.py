import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import type_definition
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'type_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)


class testRuleTypeMethods(unittest.TestCase):

    def test_rule_005(self):
        oRule = type_definition.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [utils.add_violation(32)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = type_definition.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '008')
        dExpected = utils.add_violation_list([9,32])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = type_definition.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '009')
        dExpected = utils.add_violation_list([6,29])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)


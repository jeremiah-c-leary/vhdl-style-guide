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

    def test_rule_001(self):
        oRule = type_definition.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([6,11])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = type_definition.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '002')
        lExpected = []
        dViolation = utils.add_violation(34)
        dViolation['words_to_fix'] = {'TYPE'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_004(self):
        oRule = type_definition.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '004')
        lExpected = []
        dViolation = utils.add_violation(27)
        dViolation['words_to_fix'] = {'A'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = type_definition.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [utils.add_violation(32)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = type_definition.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '006')
        dExpected = utils.add_violation_list([36,134])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = type_definition.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [utils.add_violation(29)]
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

    def test_rule_010(self):
        oRule = type_definition.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '010')
        dExpected = [utils.add_violation(43)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_011(self):
        oRule = type_definition.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '011')
        dExpected = [utils.add_violation(48)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = type_definition.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '012')
        dExpected = utils.add_violation_list([60,61])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = type_definition.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '013')
        lExpected = []
        dViolation = utils.add_violation(13)
        dViolation['words_to_fix'] = {'IS'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_015_with_default(self):
        oRule = type_definition.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '015')
        self.assertTrue(oRule.disable)
        dExpected = utils.add_violation_list([4,6,11,13,27,29,34,36,43,54,57,69,122,134])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_with_single_override(self):
        oRule = type_definition.rule_015()
        oRule.prefixes = ['mem']
        dExpected = utils.add_violation_list([4,6,11,13,27,29,34,36,43,57,69,122])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_with_multiple_override(self):
        oRule = type_definition.rule_015()
        oRule.prefixes = ['mem', 'a']
        dExpected = utils.add_violation_list([13,57,69])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

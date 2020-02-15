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
        dExpected = [6,11]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = type_definition.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [{'line_number': 34, 'words_to_fix': {'TYPE'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = type_definition.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [29]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_w_2_spaces(self):
        oRule = type_definition.rule_003()
        oRule.spaces = 2
        dExpected = [4,6,11,13,27,34,36,43,54,57,69,122,134]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = type_definition.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [{'line_number': 27, 'words_to_fix': {'A'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = type_definition.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [32]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = type_definition.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [36,134]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = type_definition.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [29]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = type_definition.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [9,32]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = type_definition.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [6,29]
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
        dExpected = [48]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012(self):
        oRule = type_definition.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '012')
        dExpected = [60,61]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_013(self):
        oRule = type_definition.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '013')
        dExpected = [{'line_number': 13, 'words_to_fix': {'IS'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_with_default(self):
        oRule = type_definition.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '015')
        self.assertTrue(oRule.disable)
        dExpected = [4,6,11,13,27,29,34,36,43,54,57,69,122,134]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_with_single_override(self):
        oRule = type_definition.rule_015()
        oRule.prefixes = ['mem']
        dExpected = [4,6,11,13,27,29,34,36,43,57,69,122]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_015_with_multiple_override(self):
        oRule = type_definition.rule_015()
        oRule.prefixes = ['mem', 'a']
        dExpected = [13,57,69]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

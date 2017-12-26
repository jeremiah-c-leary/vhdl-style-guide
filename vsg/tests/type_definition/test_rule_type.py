import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import type_definition
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'type_test_input.vhd'))


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
        dExpected = [34]
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

    def test_rule_004(self):
        oRule = type_definition.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [27]
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
        dExpected = [36]
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
        dExpected = [43]
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


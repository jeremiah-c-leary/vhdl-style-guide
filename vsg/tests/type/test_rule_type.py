import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import type
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','type','type_test_input.vhd'))

class testRuleSignalMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = type.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [6,11]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = type.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [26]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = type.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = type.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [19]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = type.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = type.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [28]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = type.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '007')
        dExpected = [21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_008(self):
        oRule = type.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [9,24]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = type.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'type')
        self.assertEqual(oRule.identifier, '009')
        dExpected = [6,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

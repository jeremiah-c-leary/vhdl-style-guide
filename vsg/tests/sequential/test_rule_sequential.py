import os
import unittest

from vsg.rules import sequential
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','sequential','sequential_test_input.vhd'))

class testRuleSequentialMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = sequential.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [14,20,28,56,66,73,81,89,90]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = sequential.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [26,33,65,83]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = sequential.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [38,40,81,89]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = sequential.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '004')
        dExpected = [54,55,74]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = sequential.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '005')
        dExpected = ['13-15','20-22', '26-28','38-40','53-58','65-66','73-75','80-81','88-90']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = sequential.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [93,94]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

import os
import unittest

from vsg.rules import sequential
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','sequential','sequential_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleSequentialMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = sequential.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([14,20,28,56,66,73,81,89,90])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = sequential.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '002')
        dExpected = utils.add_violation_list([26,33,65,83])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = sequential.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '003')
        dExpected = utils.add_violation_list([38,40,81,89])
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
        dExpected = [{'lines': [{'number': 13, 'keyword_column': 6, 'before_keyword_column': 4},
                                {'number': 14, 'keyword_column': 4, 'before_keyword_column': 2},
                                {'number': 15, 'keyword_column': 6, 'before_keyword_column': 4}],
                      'max_keyword_column': 6, 'max_before_keyword_column': 4},
                     {'lines': [{'number': 20, 'keyword_column': 11, 'before_keyword_column': 9},
                                {'number': 21, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 22, 'keyword_column': 10, 'before_keyword_column': 8}],
                      'max_keyword_column': 11, 'max_before_keyword_column': 9},
                     {'lines': [{'number': 26, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 27, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 28, 'keyword_column': 8, 'before_keyword_column': 6}],
                      'max_keyword_column': 10, 'max_before_keyword_column': 8},
                     {'lines': [{'number': 38, 'keyword_column': 9, 'before_keyword_column': 8},
                                {'number': 39, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 40, 'keyword_column': 9, 'before_keyword_column': 8}],
                      'max_keyword_column': 10, 'max_before_keyword_column': 8},
                     {'lines': [{'number': 53, 'keyword_column': 8, 'before_keyword_column': 4},
                                {'number': 56, 'keyword_column': 7, 'before_keyword_column': 4},
                                {'number': 57, 'keyword_column': 8, 'before_keyword_column': 6}],
                      'max_keyword_column': 8, 'max_before_keyword_column': 6},
                     {'lines': [{'number': 65, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 66, 'keyword_column': 13, 'before_keyword_column': 11}],
                      'max_keyword_column': 13, 'max_before_keyword_column': 11},
                     {'lines': [{'number': 73, 'keyword_column': 15, 'before_keyword_column': 13},
                                {'number': 75, 'keyword_column': 14, 'before_keyword_column': 11}],
                      'max_keyword_column': 15, 'max_before_keyword_column': 13},
                     {'lines': [{'number': 80, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 81, 'keyword_column': 8, 'before_keyword_column': 7}],
                      'max_keyword_column': 10, 'max_before_keyword_column': 8},
                     {'lines': [{'number': 88, 'keyword_column': 10, 'before_keyword_column': 8},
                                {'number': 89, 'keyword_column': 8, 'before_keyword_column': 7},
                                {'number': 90, 'keyword_column': 11, 'before_keyword_column': 9}],
                      'max_keyword_column': 11, 'max_before_keyword_column': 9}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = sequential.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'sequential')
        self.assertEqual(oRule.identifier, '006')
        dExpected = utils.add_violation_list([93,94])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

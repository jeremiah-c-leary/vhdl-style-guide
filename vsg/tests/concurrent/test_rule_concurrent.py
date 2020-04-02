import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','concurrent','concurrent_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleConcurrentMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = concurrent.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([7,11,24,32,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = concurrent.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '002')
        dExpected = utils.add_violation_list([7,8,24,32,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = concurrent.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '003')
        dExpected = utils.add_violation_list([28,29,30])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = concurrent.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([7,8,32,33])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = concurrent.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '005')
        lExpected = []

        dViolation = utils.add_violation(32)
        dViolation['label'] = 'label'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['label'] = 'label'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(34)
        dViolation['label'] = 'label'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(35)
        dViolation['label'] = 'label'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_006(self):
        oRule = concurrent.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '006')
        dExpected = [{'lines': [{'number': 6, 'keyword_column': 16, 'before_keyword_column': 14},
                                {'number': 7, 'keyword_column': 2, 'before_keyword_column': 0},
                                {'number': 8, 'keyword_column': 3, 'before_keyword_column': 2},
                                {'number': 9, 'keyword_column': 4, 'before_keyword_column': 2},
                                {'number': 11, 'keyword_column': 6, 'before_keyword_column': 4}],
                      'max_keyword_column': 16, 'max_before_keyword_column': 14},
                     {'lines': [{'number': 23, 'keyword_column': 4, 'before_keyword_column': 2},
                                {'number': 24, 'keyword_column': 3, 'before_keyword_column': 1}],
                      'max_keyword_column': 4, 'max_before_keyword_column': 2},
                     {'lines': [{'number': 32, 'keyword_column': 7, 'before_keyword_column': 6},
                                {'number': 33, 'keyword_column': 9, 'before_keyword_column': 8},
                                {'number': 34, 'keyword_column': 12, 'before_keyword_column': 10},
                                {'number': 35, 'keyword_column': 12, 'before_keyword_column': 10}],
                      'max_keyword_column': 12, 'max_before_keyword_column': 10},
                     {'lines': [{'number': 50, 'keyword_column': 4, 'before_keyword_column': 2},
                                {'number': 52, 'keyword_column': 16, 'before_keyword_column': 14}],
                      'max_keyword_column': 16, 'max_before_keyword_column': 14}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = concurrent.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '007')
        lExpected = []
        dViolation = utils.add_violation(44)
        dViolation['slice_index'] = [26]
        lExpected.append(dViolation)

        dViolation = utils.add_violation(48)
        dViolation['slice_index'] = [26]
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_008(self):
        oRule = concurrent.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '008')
        dExpected = [{'lines': [{'number': 6, 'keyword_column': 27, 'before_keyword_column': 20},
                                {'number': 7, 'keyword_column': 19, 'before_keyword_column': 5},
                                {'number': 8, 'keyword_column': 14, 'before_keyword_column': 12},
                                {'number': 9, 'keyword_column': 23, 'before_keyword_column': 5},
                                {'number': 11, 'keyword_column': 18, 'before_keyword_column': 10}],
                      'max_keyword_column': 27, 'max_before_keyword_column': 20},
                     {'lines': [{'number': 34, 'keyword_column': 19, 'before_keyword_column': 16}],
                      'max_keyword_column': 19, 'max_before_keyword_column': 16}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import variable
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','variable','variable_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleVariableMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = variable.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([6,8,15])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = variable.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '002')
        lExpected = []
        dViolation = utils.add_violation(7)
        dViolation['words_to_fix'] = {'Variable'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(11)
        dViolation['words_to_fix'] = {'varIAble'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(13)
        dViolation['words_to_fix'] = {'variabLE'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_004(self):
        oRule = variable.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '004')
        lExpected = []
        dViolation = utils.add_violation(6)
        dViolation['words_to_fix'] = {'a_SIg'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(9)
        dViolation['words_to_fix'] = {'siG'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(12)
        dViolation['words_to_fix'] = {'SIg'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(15)
        dViolation['words_to_fix'] = {'sIg'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = variable.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '005')
        dExpected = utils.add_violation_list([6,10,13,14,16,20,21])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_006(self):
        oRule = variable.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '006')
        dExpected = utils.add_violation_list([7,11,19,21])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_007(self):
        oRule = variable.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '007')
        dExpected = utils.add_violation_list([11,16])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_010(self):
        oRule = variable.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '010')
        lExpected = []
        dViolation = utils.add_violation(12)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(18)
        dViolation['words_to_fix'] = {'STD_LOGIC'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_012_with_default(self):
        oRule = variable.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '012')
        self.assertTrue(oRule.disable)
        dExpected = utils.add_violation_list([5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,27,28,29,37,38,39,47,48,49,57,66,71])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_with_single_override(self):
        oRule = variable.rule_012()
        oRule.prefixes = ['a_']
        dExpected = utils.add_violation_list([7,8,9,10,11,12,13,14,15,16,18,19,20,21,27,28,29,37,38,39,47,48,49,57,66,71])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_012_with_multiple_override(self):
        oRule = variable.rule_012()
        oRule.prefixes = ['a_','c_','p1_']
        dExpected = utils.add_violation_list([7,8,9,10,11,12,13,14,15,16,18,20,47,48,49,57,66,71])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

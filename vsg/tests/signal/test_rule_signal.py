import os

import unittest
import sys
sys.path.append('vsg')

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'signal_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleSignalMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = signal.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '001')
        lExpected = utils.add_violation_list([6,8,15])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_002(self):
        oRule = signal.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '002')
        lExpected = []
        dViolation = utils.add_violation(7)
        dViolation['words_to_fix'] = {'Signal'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(11)
        dViolation['words_to_fix'] = {'siGNal'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(13)
        dViolation['words_to_fix'] = {'signAL'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_004(self):
        oRule = signal.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '004')
        lExpected = []
        dViolation = utils.add_violation(6,)
        dViolation['words_to_fix'] = {'a_SIg'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(9,)
        dViolation['words_to_fix'] = {'siG'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(12)
        dViolation['words_to_fix'] = {'SIg'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(15)
        dViolation['words_to_fix'] = {'sIg'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(20)
        dViolation['words_to_fix'] = {'b_Sig2', 'b_siG100'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['words_to_fix'] = {'a_sIg2'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = signal.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '005')
        lExpected = utils.add_violation_list([6,10,13,14,16,20,21])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_006(self):
        oRule = signal.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '006')
        lExpected = utils.add_violation_list([7,11,19,21])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_007(self):
        oRule = signal.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '007')
        lExpected = utils.add_violation_list([11,16])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_008(self):
        oRule = signal.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '008')
        self.assertTrue(oRule.disable)
        lExpected = utils.add_violation_list([9,12,13,14,15,16,19,21,23])
        oRule.prefixes = ['a_','b_','d_','e_']
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_010(self):
        oRule = signal.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '010')
        lExpected = []
        dViolation = utils.add_violation(12)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(16)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_011(self):
        oRule = signal.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '011')
        lExpected = []
        dViolation = utils.add_violation(12)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(16)
        dViolation['words_to_fix'] = {'STD_LOGIC_VECTOR'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(23)
        dViolation['words_to_fix'] = {'t_User_Defined_Type'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

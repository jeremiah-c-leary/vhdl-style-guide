import os
import unittest

from vsg.rules import ranges
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'range_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleRange(unittest.TestCase):

    def test_rule_001_with_default(self):
        oRule = ranges.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'range')
        self.assertEqual(oRule.identifier, '001')
        lExpected = []
        dViolation = utils.add_violation(17)
        dViolation['words_to_fix'] = {'downTo'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['words_to_fix'] = {'Downto'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(28)
        dViolation['words_to_fix'] = {'DOWNTO'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['words_to_fix'] = {'dOWnto'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_001_with_uppercase(self):
        oRule = ranges.rule_001()
        oRule.case = 'upper'
        lExpected = []
        dViolation = utils.add_violation(5,)
        dViolation['words_to_fix'] = {'downto'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(9,)
        dViolation['words_to_fix'] = {'downto'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(17)
        dViolation['words_to_fix'] = {'downTo'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(21)
        dViolation['words_to_fix'] = {'Downto'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(29)
        dViolation['words_to_fix'] = {'downto'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(33)
        dViolation['words_to_fix'] = {'dOWnto'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(34)
        dViolation['words_to_fix'] = {'downto'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_002_with_default(self):
        oRule = ranges.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'range')
        self.assertEqual(oRule.identifier, '002')
        lExpected = []
        dViolation = utils.add_violation(18)
        dViolation['words_to_fix'] = {'TO'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(22)
        dViolation['words_to_fix'] = {'tO'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['words_to_fix'] = {'To'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(35)
        dViolation['words_to_fix'] = {'TO'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_002_with_uppercase(self):
        oRule = ranges.rule_002()
        oRule.case = 'upper'
        lExpected = []
        dViolation = utils.add_violation(6,)
        dViolation['words_to_fix'] = {'to'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(10)
        dViolation['words_to_fix'] = {'to'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(22)
        dViolation['words_to_fix'] = {'tO'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(30)
        dViolation['words_to_fix'] = {'To'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(31)
        dViolation['words_to_fix'] = {'to'}
        lExpected.append(dViolation)

        dViolation = utils.add_violation(36)
        dViolation['words_to_fix'] = {'to'}
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

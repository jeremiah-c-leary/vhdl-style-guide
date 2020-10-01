import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','constant','constant_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleConstantMethods(unittest.TestCase):

    def test_rule_007(self):
        oRule = constant.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '007')
        lExpected = [utils.add_violation(10)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_012(self):
        oRule = constant.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '012')
        lExpected = utils.add_violation_list([31,32,34,36])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_014(self):
        oRule = constant.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '014')

        lExpected = []
        dViolation = utils.add_violation(44)
        dViolation['column'] = 42
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

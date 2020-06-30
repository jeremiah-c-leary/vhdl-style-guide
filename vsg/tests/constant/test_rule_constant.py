import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils


# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','constant','constant_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleConstantMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = constant.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '001')
        lExpected = utils.add_violation_list([8,9,10])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_002(self):
        oRule = constant.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '002')
        lExpected = [{'lines':[{'number': 7}], 'words_to_fix': {'COnstant'}},
                     {'lines':[{'number': 8}], 'words_to_fix': {'Constant'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_004(self):
        oRule = constant.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '004')
        lExpected = [{'lines':[{'number': 8}], 'words_to_fix': {'c_coNST'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = constant.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '005')
        lExpected = utils.add_violation_list([8,9])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_006(self):
        oRule = constant.rule_006()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '006')
        lExpected = [utils.add_violation(10)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_007(self):
        oRule = constant.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '007')
        lExpected = [utils.add_violation(10)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_010(self):
        oRule = constant.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '010')
        lExpected = utils.add_violation_list([9])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_011(self):
        oRule = constant.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '011')
        lExpected = [{'lines':[{'number': 9}], 'words_to_fix': {'STD_LOGIC'}}]
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

    def test_rule_015_with_default(self):
        oRule = constant.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '015')
        lExpected = utils.add_violation_list([6,9,18,28,30,38])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_015_with_override(self):
        oRule = constant.rule_015()
        oRule.prefixes = ['c_', 'ro']
        lExpected = utils.add_violation_list([6,9,18,28,38])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

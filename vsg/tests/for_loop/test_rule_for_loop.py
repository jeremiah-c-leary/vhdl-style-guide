import os

import unittest

from vsg.rules import for_loop
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'for_loop_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleForLoopMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = for_loop.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '001')
        dExpected = utils.add_violation_list([19,21])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = for_loop.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [utils.add_violation(23)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_uppercase(self):
        oRule = for_loop.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [{'lines':[{'number': 36}], 'words_to_fix': {'label'}},
                     {'lines':[{'number': 40}], 'words_to_fix': {'Label'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003_lowercase(self):
        oRule = for_loop.rule_003()
        oRule.case = 'lower'
        dExpected = [{'lines':[{'number': 40}], 'words_to_fix': {'Label'}},
                     {'lines':[{'number': 44}], 'words_to_fix': {'LABEL'}},
                     {'lines':[{'number': 48}], 'words_to_fix': {'LABEL'}},
                     {'lines':[{'number': 52}], 'words_to_fix': {'LABEL'}},
                     {'lines':[{'number': 56}], 'words_to_fix': {'LABEL'}}]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = for_loop.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '004')
        lExpected = []
        dViolation = utils.add_violation(40)
        dViolation['label'] = 'Label'
        lExpected.append(dViolation)

        dViolation = utils.add_violation(48)
        dViolation['label'] = 'LABEL'
        lExpected.append(dViolation)

        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_rule_005(self):
        oRule = for_loop.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '005')
        dExpected = utils.add_violation_list([44,52])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

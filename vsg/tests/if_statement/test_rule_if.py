import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)
lFileCase = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(lFileCase)
lFileIf = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'comment_if_input.vhd'))
oFileIf = vhdlFile.vhdlFile(lFileIf)

class testRuleIfMethods(unittest.TestCase):

    def test_rule_002(self):
        oRule = if_statement.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '002')
        dExpected = utils.add_violation_list([8,13,24,33,41,46,52])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_003(self):
        oRule = if_statement.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '003')
        dExpected = [utils.add_violation(57)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_004(self):
        oRule = if_statement.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '004')
        dExpected = utils.add_violation_list([32,57,73])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_005(self):
        oRule = if_statement.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '005')
        dExpected = [utils.add_violation(73)]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_009(self):
        oRule = if_statement.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '009')
        dExpected = utils.add_violation_list([20,21,67,68,115])
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

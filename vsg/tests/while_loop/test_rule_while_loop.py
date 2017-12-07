import os

import unittest

from vsg.rules import while_loop
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','while_loop','while_loop_test_input.vhd'))

class testRuleWhileLoopMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = while_loop.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'while_loop')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [13]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = while_loop.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'while_loop')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [19]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

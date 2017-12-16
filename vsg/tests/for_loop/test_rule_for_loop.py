import os

import unittest

from vsg.rules import for_loop
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'for_loop_test_input.vhd'))

class testRuleForLoopMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = for_loop.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '001')
        dExpected = [19,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_rule_002(self):
        oRule = for_loop.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'for_loop')
        self.assertEqual(oRule.identifier, '002')
        dExpected = [23]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

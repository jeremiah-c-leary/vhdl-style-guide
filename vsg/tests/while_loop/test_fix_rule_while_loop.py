import os

import unittest

from vsg.rules import while_loop
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','while_loop','while_loop_test_input.vhd'))

class testFixRuleWhileLoopMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = while_loop.rule_001()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

    def test_fix_rule_002(self):
        oRule = while_loop.rule_002()
        dExpected = []
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

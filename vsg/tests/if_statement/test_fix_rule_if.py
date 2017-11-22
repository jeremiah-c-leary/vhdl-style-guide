import os

import unittest

from vsg.rules import if_statement
from vsg import vhdlFile

# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_test_input.vhd'))
oFileCase = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'..','if_statement','if_case_test_input.vhd'))


class testRuleIfMethods(unittest.TestCase):

    def test_fix_rule_001(self):
        oRule = if_statement.rule_001()
        oRule.fix(oFile)
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, [])

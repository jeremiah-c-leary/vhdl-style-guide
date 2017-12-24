import os

import unittest

from vsg.rules import with_statement
from vsg import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'with_test_input.vhd'))

class testRuleWithMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = with_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'with')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [6]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

import os

import unittest

from vsg.rules import assert_statement
from vsg import vhdlFile


# Read in test file used for all tests
oFile = vhdlFile.vhdlFile(os.path.join(os.path.dirname(__file__),'assert_test_input.vhd'))

class testRuleAssertMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = assert_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'assert')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [10,16,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

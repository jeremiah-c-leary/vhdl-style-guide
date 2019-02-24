import os

import unittest

from vsg.rules import assert_statement
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'assert_test_input.vhd'))
oFile = vhdlFile.vhdlFile(lFile)

class testRuleAssertMethods(unittest.TestCase):

    def test_rule_001(self):
        oRule = assert_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'assert')
        self.assertEqual(oRule.identifier, '001')

        dExpected = [10,16,21]
        oRule.analyze(oFile)
        self.assertEqual(oRule.violations, dExpected)

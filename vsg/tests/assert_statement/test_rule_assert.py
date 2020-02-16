import os

import unittest

from vsg.rules import assert_statement
from vsg import vhdlFile
from vsg.tests import utils

# Read in test file used for all tests
lFile = utils.read_vhdlfile(os.path.join(os.path.dirname(__file__),'assert_test_input.vhd'))

class testRuleAssertMethods(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)

    def test_rule_001(self):
        oRule = assert_statement.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'assert')
        self.assertEqual(oRule.identifier, '001')

        lExpected = utils.add_violation_list([10,11,16,17,20,21])
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

    def test_fix_rule_001(self):
        oRule = assert_statement.rule_001()
        oRule.fix(self.oFile)

        self.assertEqual(self.oFile.lines[10].line, '  assert boolean')
        self.assertEqual(self.oFile.lines[11].line, '    report "Something"')
        self.assertEqual(self.oFile.lines[12].line, '    severity FAILURE;')

        self.assertEqual(self.oFile.lines[15].line, '  assert boolean')
        self.assertEqual(self.oFile.lines[16].line, '    report "Something"')
        self.assertEqual(self.oFile.lines[17].line, '    severity FAILURE;')

        self.assertEqual(self.oFile.lines[19].line, '  assert boolean')
        self.assertEqual(self.oFile.lines[20].line, '    report "Something"')
        self.assertEqual(self.oFile.lines[21].line, '    severity FAILURE;')

        lExpected = []
        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, lExpected)

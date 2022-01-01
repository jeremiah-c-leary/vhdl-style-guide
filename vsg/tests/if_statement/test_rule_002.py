
import os
import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_002_test_input.vhd'))

lExpected_parenthesis_insert = []
lExpected_parenthesis_insert.append('')
utils.read_file(os.path.join(sTestDir, 'rule_002_test_input.fixed_parenthesis_insert.vhd'), lExpected_parenthesis_insert)

lExpected_parenthesis_remove = []
lExpected_parenthesis_remove.append('')
utils.read_file(os.path.join(sTestDir, 'rule_002_test_input.fixed_parenthesis_remove.vhd'), lExpected_parenthesis_remove)


class test_if_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_002_parenthesis_insert(self):
        oRule = if_statement.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '002')
        oRule.parenthesis = 'insert'
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [24, 26, 28, 30, 32, 40, 44, 52, 84, 86]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_parenthesis_insert(self):
        oRule = if_statement.rule_002()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_parenthesis_insert, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_002_parenthesis_remove(self):
        oRule = if_statement.rule_002()
        oRule.parenthesis = 'remove'

        lExpected = [10, 12, 14, 16, 18, 56, 60, 64, 68, 72, 76, 90, 92]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_parenthesis_remove(self):
        oRule = if_statement.rule_002()
        oRule.parenthesis = 'remove'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_parenthesis_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

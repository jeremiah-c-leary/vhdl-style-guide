
import os
import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_031_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_031_test_input.fixed.vhd'), lExpected)

lExpected_require_blank_line_ignore_hierarchy = []
lExpected_require_blank_line_ignore_hierarchy.append('')
utils.read_file(os.path.join(sTestDir, 'rule_031_test_input.fixed_require_blank_line_ignore_hierarchy.vhd'), lExpected_require_blank_line_ignore_hierarchy)


class test_if_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_031(self):
        oRule = if_statement.rule_031()

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '031')

        lExpected = [36, 49, 56]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_031(self):
        oRule = if_statement.rule_031()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_031_require_blank_line_ignore_hierarchy(self):
        oRule = if_statement.rule_031()
        oRule.ignore_hierarchy = True
        oRule.except_if_statement = True

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '031')

        lExpected = [14, 16, 25, 27, 36, 38, 40, 49, 56, 59]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_031_require_blank_line_ignore_hierarchy(self):
        oRule = if_statement.rule_031()
        oRule.ignore_hierarchy = True
        oRule.except_if_statement = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_line_ignore_hierarchy, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

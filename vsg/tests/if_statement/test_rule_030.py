
import os
import unittest

from vsg.rules import if_statement
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_030_test_input.vhd'))

lExpected_require_blank = []
lExpected_require_blank.append('')
utils.read_file(os.path.join(sTestDir, 'rule_030_test_input.fixed_require_blank.vhd'), lExpected_require_blank)

lExpected_require_blank_ignore_hierarchy_true  = []
lExpected_require_blank_ignore_hierarchy_true .append('')
utils.read_file(os.path.join(sTestDir, 'rule_030_test_input.fixed_require_blank_ignore_hierarchy_true.vhd'), lExpected_require_blank_ignore_hierarchy_true)

lExpected_require_blank_ignore_hierarchy_true_allow_end_ifs_true  = []
lExpected_require_blank_ignore_hierarchy_true_allow_end_ifs_true .append('')
utils.read_file(os.path.join(sTestDir, 'rule_030_test_input.fixed_require_blank_ignore_hierarchy_true_allow_end_ifs_true.vhd'), lExpected_require_blank_ignore_hierarchy_true_allow_end_ifs_true)

lExpected_no_blank = []
lExpected_no_blank.append('')
utils.read_file(os.path.join(sTestDir, 'rule_030_test_input.fixed_no_blank.vhd'), lExpected_no_blank)


class test_if_statement_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_030_w_require_blank_enforce_hierarchy(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '030')

        lExpected = [32, 53]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_require_blank_enforce_hierarchy(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_030_w_require_blank_ignore_hierarchy(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = True

        lExpected = [14, 16, 28, 30, 32, 51, 52, 53]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_require_blank_ignore_hierarchy(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_ignore_hierarchy_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_030_w_require_blank_ignore_hierarchy_allow_end_ifs(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = True
        oRule.allow_end_ifs = True

        lExpected = [14, 16, 28, 30, 32, 53]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_require_blank_ignore_hierarchy_allow_end_ifs(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = True
        oRule.allow_end_ifs = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_ignore_hierarchy_true_allow_end_ifs_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])




    def test_rule_030_w_no_blank(self):
        oRule = if_statement.rule_030()
        oRule.style = 'no_blank_line'
        oRule.ignore_hierarchy = False
        oRule.allow_end_if = False
        oRule.allow_other_ends = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '030')

        lExpected = [19]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_no_blank(self):
        oRule = if_statement.rule_030()
        oRule.style = 'no_blank_line'
        oRule.ignore_hierarchy = False
        oRule.allow_end_if = False
        oRule.allow_other_ends = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

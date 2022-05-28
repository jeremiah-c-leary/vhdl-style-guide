
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

lExpected_require_blank_allow_end_process  = []
lExpected_require_blank_allow_end_process .append('')
utils.read_file(os.path.join(sTestDir, 'rule_030_test_input.fixed_require_blank_allow_end_process.vhd'), lExpected_require_blank_allow_end_process)

lExpected_require_blank_allow_end_case = []
lExpected_require_blank_allow_end_case .append('')
utils.read_file(os.path.join(sTestDir, 'rule_030_test_input.fixed_require_blank_allow_end_case.vhd'), lExpected_require_blank_allow_end_case)

lExpected_require_blank_end_case_no_blank_line = []
lExpected_require_blank_end_case_no_blank_line .append('')
utils.read_file(os.path.join(sTestDir, 'rule_030_test_input.fixed_require_blank_end_case_no_blank_line.vhd'), lExpected_require_blank_end_case_no_blank_line)

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

        lExpected = [32, 53, 78, 83]

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

    def test_rule_030_w_require_blank_allow_end_process(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = False
        oRule.except_end_process = True

        lExpected = [32, 78, 83]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_require_blank_allow_end_process(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = False
        oRule.except_end_process = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_allow_end_process, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_030_w_require_blank_true_except_end_case_true(self):
        oRule = if_statement.rule_030()
        oRule.style = 'require_blank_line'
        oRule.ignore_hierarchy = False
        oRule.except_end_case = True

        lExpected = [32, 53, 97, 103]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_require_blank_true_except_end_case_true(self):
        oRule = if_statement.rule_030()
        oRule.style = 'require_blank_line'
        oRule.ignore_hierarchy = False
        oRule.except_end_case = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_allow_end_case, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

#    def test_rule_030_w_require_blank_true_end_case_no_blank_line(self):
#        oRule = if_statement.rule_030()
#        oRule.ignore_hierarchy = False
#        oRule.end_case = 'no_blank_line'
#
#        lExpected = [32, 53, 97, 103]
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
#
#    def test_fix_rule_030_w_require_true_end_case_no_blank_line(self):
#        oRule = if_statement.rule_030()
#        oRule.ignore_hierarchy = False
#        oRule.end_case = 'no_blank_line'
#
#        oRule.fix(self.oFile)
#
#        lActual = self.oFile.get_lines()
#
#        self.assertEqual(lExpected_require_blank_end_case_no_blank_line, lActual)
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, [])

    def test_rule_030_w_require_blank_ignore_hierarchy(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = True
        lExpected = [14, 16, 28, 30, 32, 51, 52, 53, 78, 81, 82, 83, 101, 102]

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
        oRule.except_end_if = True

        lExpected = [14, 16, 28, 30, 32, 53, 78, 83]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_require_blank_ignore_hierarchy_allow_end_ifs(self):
        oRule = if_statement.rule_030()
        oRule.ignore_hierarchy = True
        oRule.except_end_if = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_ignore_hierarchy_true_allow_end_ifs_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_030_w_no_blank(self):
        oRule = if_statement.rule_030()
        oRule.style = 'no_blank_line'
        oRule.ignore_hierarchy = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'if')
        self.assertEqual(oRule.identifier, '030')

        lExpected = [18, 97, 103]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_030_w_no_blank(self):
        oRule = if_statement.rule_030()
        oRule.style = 'no_blank_line'
        oRule.ignore_hierarchy = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_blank, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

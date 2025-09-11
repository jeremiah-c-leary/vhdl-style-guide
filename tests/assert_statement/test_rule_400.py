# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import assert_statement

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_400_test_input.vhd"))

dIndentMap = utils.read_indent_file()

dIndentMap = utils.read_indent_file()

lExpected_report_aligned = []
lExpected_report_aligned.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_report_aligned.vhd"), lExpected_report_aligned)

lExpected_left_aligned = []
lExpected_left_aligned.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_left_aligned.vhd"), lExpected_left_aligned)

lExpected_report_aligned_smart_tabs = []
lExpected_report_aligned_smart_tabs.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_report_aligned__smart_tabs.vhd"), lExpected_report_aligned_smart_tabs)

lExpected_left_aligned_smart_tabs = []
lExpected_left_aligned_smart_tabs.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_left_aligned__smart_tabs.vhd"), lExpected_left_aligned_smart_tabs)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_400_w_report_align(self):
        oRule = assert_statement.rule_400()
        oRule.alignment = "report"
        oRule.indent_style = "spaces"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "assert")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [9, 14, 29, 34]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_w_report_align(self):
        oRule = assert_statement.rule_400()
        oRule.alignment = "report"
        oRule.indent_style = "spaces"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_report_aligned, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400_w_left_align(self):
        oRule = assert_statement.rule_400()
        oRule.alignment = "left"
        oRule.indent_style = "spaces"

        lExpected = [19, 24, 29, 34]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_w_left_align(self):
        oRule = assert_statement.rule_400()
        oRule.alignment = "left"
        oRule.indent_style = "spaces"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_left_aligned, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400_w_report_align_smart_tabs(self):
        oRule = assert_statement.rule_400()
        oRule.alignment = "report"
        oRule.indent_style = "smart_tabs"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "assert")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [9, 14, 19, 24, 29, 34]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_w_report_align_smart_tabs(self):
        self.maxDiff = None
        oRule = assert_statement.rule_400()
        oRule.alignment = "report"
        oRule.indent_style = "smart_tabs"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_report_aligned_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400_w_left_align_smart_tabs(self):
        oRule = assert_statement.rule_400()
        oRule.alignment = "left"
        oRule.indent_style = "smart_tabs"

        lExpected = [9, 14, 19, 24, 29, 34]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_w_left_align_smart_tabs(self):
        oRule = assert_statement.rule_400()
        oRule.alignment = "left"
        oRule.indent_style = "smart_tabs"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_left_aligned_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

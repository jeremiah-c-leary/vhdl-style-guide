# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import generate

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_402_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    ###############################################################################
    def test_rule_402_yes_yes_yes_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "402")

        lExpected = [22, 23, 25, 26, 28, 34, 35, 37, 38, 40, 46, 50]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_402_true_true_true_false_false(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        lExpected = [22, 23, 25, 26, 28, 34, 35, 37, 38, 40, 46, 50]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_402_yes_yes_yes_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_402_test_input.fixed_yes_yes_yes_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_402_yes_yes_no_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "402")

        lExpected = [22, 23, 25, 26, 28, 34, 37, 38, 40, 46, 47, 50]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_402_true_true_false_false_false(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = False
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        lExpected = [22, 23, 25, 26, 28, 34, 37, 38, 40, 46, 47, 50]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_402_yes_yes_no_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_402_test_input.fixed_yes_yes_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_402_yes_no_no_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "402")

        lExpected = [22, 23, 25, 26, 28, 34, 37, 38, 40, 46, 47, 50, 52]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_402_true_false_false_false_false(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        lExpected = [22, 23, 25, 26, 28, 34, 37, 38, 40, 46, 47, 50, 52]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_402_yes_no_no_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_402_test_input.fixed_yes_no_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_402_no_no_no_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "402")

        lExpected = [22, 23, 26, 28, 34, 35, 38, 40, 46, 47, 50, 52]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_402_false_false_false_false_false(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        lExpected = [22, 23, 26, 28, 34, 35, 38, 40, 46, 47, 50, 52]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_402_no_no_no_no_no(self):
        oRule = generate.rule_402()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_402_test_input.fixed_no_no_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

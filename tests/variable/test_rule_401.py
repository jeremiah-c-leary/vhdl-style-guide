# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import variable

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_401_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_401_options(self):
        oRule = variable.rule_401()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable")
        self.assertEqual(oRule.identifier, "401")
        self.assertEqual(len(oRule.configuration), 12)

    def test_rule_401_yes_no_no_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [8, 9, 11, 12, 14]
        lExpected.extend([20, 21, 24, 25, 28, 29])
        lExpected.extend([34, 35, 37, 38, 40, 41])
        lExpected.extend([45, 46, 47, 49, 51, 53, 54, 55])
        lExpected.extend([61, 62, 63, 64])
        lExpected.extend([67, 68, 69])
        lExpected.extend([75, 76, 77, 78])
        lExpected.extend([80, 81, 82, 83])
        lExpected.extend([89, 90, 91, 92, 94, 97])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_no_no_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed_yes_no_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_401_no_no_no_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [8, 9, 11, 12, 14]
        lExpected.extend([20, 21, 24, 25, 28, 29])
        lExpected.extend([34, 37, 38, 40, 41])
        lExpected.extend([45, 46, 49, 50, 51, 53, 54, 55])
        lExpected.extend([61, 62, 63, 64])
        lExpected.extend([67, 68, 69])
        lExpected.extend([76, 77, 78])
        lExpected.extend([80, 81, 83])
        lExpected.extend([89, 90, 91, 92, 94, 97])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_no_no_no_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed_no_no_no_no_no.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_401_yes_no_yes_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [8, 9, 11, 14]
        lExpected.extend([20, 21, 24, 25, 28, 29])
        lExpected.extend([34, 35, 37, 38, 40, 41])
        lExpected.extend([45, 46, 47, 49, 51, 53, 54, 55])
        lExpected.extend([61, 62, 63, 64])
        lExpected.extend([67, 68, 69])
        lExpected.extend([75, 76, 77, 78])
        lExpected.extend([80, 81, 82, 83])
        lExpected.extend([89, 90, 91, 92, 94, 97])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_no_yes_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed_yes_no_yes_no_no.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_401_yes_yes_no_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [8, 11, 12, 14]
        lExpected.extend([20, 21, 24, 25, 28, 29])
        lExpected.extend([34, 35, 37, 38, 40, 41])
        lExpected.extend([45, 46, 47, 49, 51, 53, 54, 55])
        lExpected.extend([61, 62, 63, 64])
        lExpected.extend([67, 68, 69])
        lExpected.extend([75, 76, 77, 78])
        lExpected.extend([80, 81, 82, 83])
        lExpected.extend([89, 90, 91, 92, 94, 97])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_yes_no_no_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed_yes_yes_no_no_no.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_401_yes_yes_yes_yes_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [8, 11, 14]
        lExpected.extend([20, 21, 24, 25, 28, 29])
        lExpected.extend([34, 35, 37, 38, 40, 41])
        lExpected.extend([45, 46, 47, 49, 51, 53, 54, 55])
        lExpected.extend([75, 76, 77, 78])
        lExpected.extend([80, 81, 82, 83])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_yes_yes_yes_no(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed_yes_yes_yes_yes_no.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_401_yes_yes_yes_yes_yes(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "yes"

        lExpected = [8, 11, 14]
        lExpected.extend([20, 21, 24, 25, 28, 29])
        lExpected.extend([34, 35, 37, 38, 40, 41])
        lExpected.extend([45, 46, 47, 49, 51, 53, 54, 55])
        lExpected.extend([75, 76, 77, 78])
        lExpected.extend([80, 81, 82, 83])
        lExpected.extend([97])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_yes_yes_yes_yes(self):
        oRule = variable.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed_yes_yes_yes_yes_yes.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

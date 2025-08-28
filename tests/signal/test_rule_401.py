# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import signal

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_401_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_401_options(self):
        oRule = signal.rule_401()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "signal")
        self.assertEqual(oRule.identifier, "401")
        self.assertEqual(len(oRule.configuration), 12)

    def test_rule_401_yes_no_no_no_no(self):
        oRule = signal.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [5, 6, 8, 9, 11]
        lExpected.extend([17, 18, 21, 22, 25, 26])
        lExpected.extend([31, 32, 34, 35, 37, 38])
        lExpected.extend([42, 43, 44, 46, 48, 50, 51, 52])
        lExpected.extend([58, 59, 60, 61])
        lExpected.extend([64, 65, 66])
        lExpected.extend([72, 73, 74, 75])
        lExpected.extend([77, 78, 79, 80])
        lExpected.extend([86, 87, 88, 89, 91, 94])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_no_no_no_no(self):
        oRule = signal.rule_401()
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
        oRule = signal.rule_401()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [5, 6, 8, 9, 11]
        lExpected.extend([17, 18, 21, 22, 25, 26])
        lExpected.extend([31, 34, 35, 37, 38])
        lExpected.extend([42, 43, 46, 47, 48, 50, 51, 52])
        lExpected.extend([58, 59, 60, 61])
        lExpected.extend([64, 65, 66])
        lExpected.extend([73, 74, 75])
        lExpected.extend([77, 78, 80])
        lExpected.extend([86, 87, 88, 89, 91, 94])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_no_no_no_no_no(self):
        oRule = signal.rule_401()
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
        oRule = signal.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [5, 6, 8, 11]
        lExpected.extend([17, 18, 21, 22, 25, 26])
        lExpected.extend([31, 32, 34, 35, 37, 38])
        lExpected.extend([42, 43, 44, 46, 48, 50, 51, 52])
        lExpected.extend([58, 59, 60, 61])
        lExpected.extend([64, 65, 66])
        lExpected.extend([72, 73, 74, 75])
        lExpected.extend([77, 78, 79, 80])
        lExpected.extend([86, 87, 88, 89, 91, 94])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_no_yes_no_no(self):
        oRule = signal.rule_401()
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
        oRule = signal.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [5, 8, 9, 11]
        lExpected.extend([17, 18, 21, 22, 25, 26])
        lExpected.extend([31, 32, 34, 35, 37, 38])
        lExpected.extend([42, 43, 44, 46, 48, 50, 51, 52])
        lExpected.extend([58, 59, 60, 61])
        lExpected.extend([64, 65, 66])
        lExpected.extend([72, 73, 74, 75])
        lExpected.extend([77, 78, 79, 80])
        lExpected.extend([86, 87, 88, 89, 91, 94])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_yes_no_no_no(self):
        oRule = signal.rule_401()
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
        oRule = signal.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "no"

        lExpected = [5, 8, 11]
        lExpected.extend([17, 18, 21, 22, 25, 26])
        lExpected.extend([31, 32, 34, 35, 37, 38])
        lExpected.extend([42, 43, 44, 46, 48, 50, 51, 52])
        lExpected.extend([72, 73, 74, 75])
        lExpected.extend([77, 78, 79, 80])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_yes_yes_yes_no(self):
        oRule = signal.rule_401()
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
        oRule = signal.rule_401()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "yes"

        lExpected = [5, 8, 11]
        lExpected.extend([17, 18, 21, 22, 25, 26])
        lExpected.extend([31, 32, 34, 35, 37, 38])
        lExpected.extend([42, 43, 44, 46, 48, 50, 51, 52])
        lExpected.extend([72, 73, 74, 75])
        lExpected.extend([77, 78, 79, 80])
        lExpected.extend([94])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401_yes_yes_yes_yes_yes(self):
        oRule = signal.rule_401()
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

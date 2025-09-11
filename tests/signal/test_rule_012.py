# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import signal

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_012_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_012_yes_no_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "signal")
        self.assertEqual(oRule.identifier, "012")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [4, 5, 9, 10, 12, 13, 17, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_yes_no_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_yes_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_no_no_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        lExpected = [4, 5, 9, 10, 13, 17, 19, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_no_no_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_yes_yes_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        lExpected = [4]
        lExpected.extend([9, 10, 12, 13])
        lExpected.extend([20])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_yes_no_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_yes_yes_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_yes_no_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"

        lExpected = [4, 5, 10]
        lExpected.extend([12, 13])
        lExpected.extend([17, 20])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_yes_no_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_yes_no_yes.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_yes_yes_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        lExpected = [4, 10, 12, 13, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_yes_yes_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_yes_yes_yes.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_no_yes_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        lExpected = [5, 9, 10, 13, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_no_yes_no(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_no_yes_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_no_no_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"

        lExpected = [4, 5, 9, 13, 17, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_no_no_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_no_no_yes.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_no_yes_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        lExpected = [5, 9, 13, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_no_yes_yes(self):
        oRule = signal.rule_012()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_no_yes_yes.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

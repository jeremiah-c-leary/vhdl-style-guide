# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import after

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_002_test_input.vhd"))

lExpected_yes_yes_yes = []
lExpected_yes_yes_yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_yes_yes_yes.vhd"), lExpected_yes_yes_yes)

lExpected_yes_yes_no = []
lExpected_yes_yes_no.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_yes_yes_no.vhd"), lExpected_yes_yes_no)

lExpected_yes_no_yes = []
lExpected_yes_no_yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_yes_no_yes.vhd"), lExpected_yes_no_yes)

lExpected_yes_no_no = []
lExpected_yes_no_no.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_yes_no_no.vhd"), lExpected_yes_no_no)

lExpected_no_no_yes = []
lExpected_no_no_yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_no_no_yes.vhd"), lExpected_no_no_yes)

lExpected_no_yes_no = []
lExpected_no_yes_no.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_no_yes_no.vhd"), lExpected_no_yes_no)

lExpected_no_yes_yes = []
lExpected_no_yes_yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_no_yes_yes.vhd"), lExpected_no_yes_yes)

lExpected_no_no_no = []
lExpected_no_no_no.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_no_no_no.vhd"), lExpected_no_no_no)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    ###############################################################################
    def test_rule_002_yes_yes_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_true_true_true(self):
        oRule = after.rule_002()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_yes_yes_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_yes_yes_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_yes_yes_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_true_true_false(self):
        oRule = after.rule_002()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = False

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_yes_yes_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_yes_yes_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_yes_no_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_true_false_true(self):
        oRule = after.rule_002()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = True

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_yes_no_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_yes_no_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_yes_no_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_true_false_false(self):
        oRule = after.rule_002()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_yes_no_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_yes_no_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_yes_no_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_true_false_false(self):
        oRule = after.rule_002()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False

        lExpected = [33, 34, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_yes_no_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_yes_no_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_no_no_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_false_true_true(self):
        oRule = after.rule_002()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True

        lExpected = [33]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_no_no_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_no_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_no_yes_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33, 36]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_false_true_false(self):
        oRule = after.rule_002()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = False

        lExpected = [33, 36]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_no_yes_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_yes_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_no_yes_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_false_true_true(self):
        oRule = after.rule_002()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True

        lExpected = [33]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_no_yes_yes(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_yes_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_002_no_no_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "after")
        self.assertEqual(oRule.identifier, "002")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [33, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_false_false_false(self):
        oRule = after.rule_002()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False

        lExpected = [33, 36, 38]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_no_no_no(self):
        oRule = after.rule_002()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_no_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

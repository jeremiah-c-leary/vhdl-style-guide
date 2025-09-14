# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import generate

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_404_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    ###############################################################################
    def test_rule_404_yes_yes_yes_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 65, 66, 68, 74, 75, 78]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_404_true_true_true_false_false(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 65, 66, 68, 74, 75, 78]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_404_yes_yes_yes_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_404_test_input.fixed_yes_yes_yes_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_404_yes_yes_no_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 65, 66, 68, 74, 75, 78]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_404_true_true_false_false_false(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = False
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 65, 66, 68, 74, 75, 78]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_404_yes_yes_no_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_404_test_input.fixed_yes_yes_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_404_yes_no_no_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 65, 66, 68, 74, 75, 78, 80]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_404_true_false_false_false_false(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 65, 66, 68, 74, 75, 78, 80]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_404_yes_no_no_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_404_test_input.fixed_yes_no_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_404_no_no_no_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 66, 68, 74, 75, 78, 80]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_404_false_false_false_false_false(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "404")

        lExpected = [62, 63, 66, 68, 74, 75, 78, 80]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_404_no_no_no_no_no(self):
        oRule = generate.rule_404()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "no"
        oRule.if_control_statements_ends_group = "no"
        oRule.case_control_statements_ends_group = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_404_test_input.fixed_no_no_no_no_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

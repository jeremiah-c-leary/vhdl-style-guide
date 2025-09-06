# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import constant

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_012_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected_align_left_true = []
lExpected_align_left_true.append("")
utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_true.vhd"), lExpected_align_left_true)

lExpected_align_left_true_align_paren_true = []
lExpected_align_left_true_align_paren_true.append("")
utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_true_align_paren_true.vhd"), lExpected_align_left_true_align_paren_true)

lExpected_align_left_false_align_paren_true = []
lExpected_align_left_false_align_paren_true.append("")
utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_false_align_paren_true.vhd"), lExpected_align_left_false_align_paren_true)

lExpected_align_left_false_align_paren_true_indent_step_2 = []
lExpected_align_left_false_align_paren_true_indent_step_2.append("")
utils.read_file(
    os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_false_align_paren_true_indent_step_2.vhd"),
    lExpected_align_left_false_align_paren_true_indent_step_2,
)

lExpected_align_left_true_indent_step_2 = []
lExpected_align_left_true_indent_step_2.append("")
utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_true_indent_step_2.vhd"), lExpected_align_left_true_indent_step_2)

lExpected_align_left_true_smart_tabs = []
lExpected_align_left_true_smart_tabs.append("")
utils.read_file(os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_true_smart_tabs.vhd"), lExpected_align_left_true_smart_tabs)

lExpected_align_left_false_align_paren_true_smart_tabs = []
lExpected_align_left_false_align_paren_true_smart_tabs.append("")
utils.read_file(
    os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_false_align_paren_true_smart_tabs.vhd"),
    lExpected_align_left_false_align_paren_true_smart_tabs,
)

lExpected_align_left_true_align_paren_true_smart_tabs = []
lExpected_align_left_true_align_paren_true_smart_tabs.append("")
utils.read_file(
    os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_true_align_paren_true_smart_tabs.vhd"),
    lExpected_align_left_true_align_paren_true_smart_tabs,
)

lExpected_align_left_false_align_paren_true_indent_step_2_smart_tabs = []
lExpected_align_left_false_align_paren_true_indent_step_2_smart_tabs.append("")
utils.read_file(
    os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_false_align_paren_true_indent_step_2_smart_tabs.vhd"),
    lExpected_align_left_false_align_paren_true_indent_step_2_smart_tabs,
)

lExpected_align_left_true_indent_step_2_smart_tabs = []
lExpected_align_left_true_indent_step_2_smart_tabs.append("")
utils.read_file(
    os.path.join(sTestDir, "rule_012_test_input.fixed_align_left_true_indent_step_2_smart_tabs.vhd"),
    lExpected_align_left_true_indent_step_2_smart_tabs,
)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_012_align_left_no_align_paren_yes(self):
        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = "no"
        oRule.align_paren = "yes"
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 110))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_align_left_false_align_paren_true(self):
        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = False
        oRule.align_paren = True
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 110))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_no_align_paren_yes(self):
        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = "no"
        oRule.align_paren = "yes"
        oRule.indent_size = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_false_align_paren_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_align_left_no_align_paren_yes_indent_step_2(self):
        oRule = constant.rule_012()
        oRule.align_left = "no"
        oRule.align_paren = "yes"
        oRule.indent_size = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_false_align_paren_true_indent_step_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_true_align_paren_false(self):
        oRule = constant.rule_012()
        oRule.align_left = True
        oRule.align_paren = False
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 109))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_align_left_yes_align_paren_no(self):
        oRule = constant.rule_012()
        oRule.align_left = "yes"
        oRule.align_paren = "no"
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 109))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_yes_align_paren_no(self):
        oRule = constant.rule_012()
        oRule.align_left = "yes"
        oRule.align_paren = "no"
        oRule.indent_size = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_true_align_paren_true(self):
        oRule = constant.rule_012()
        oRule.align_left = True
        oRule.align_paren = True
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 109))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_align_left_yes_align_paren_yes(self):
        oRule = constant.rule_012()
        oRule.align_left = "yes"
        oRule.align_paren = "yes"
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 109))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_yes_align_paren_yes(self):
        oRule = constant.rule_012()
        oRule.align_left = "yes"
        oRule.align_paren = "yes"
        oRule.indent_size = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_align_paren_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_align_left_yes_indent_step_2(self):
        oRule = constant.rule_012()
        oRule.align_left = "yes"
        oRule.align_paren = "no"
        oRule.indent_size = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_indent_step_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_true_align_paren_false_smart_tabs(self):
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "yes"
        oRule.align_paren = "no"
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.append(18)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 110))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_true_align_paren_false_smart_tabs(self):
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "yes"
        oRule.align_paren = "no"
        oRule.indent_size = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_false_align_paren_true_smart_tabs(self):
        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "no"
        oRule.align_paren = "yes"
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.append(18)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 110))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_false_align_paren_true_smart_tabs(self):
        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "no"
        oRule.align_paren = "yes"
        oRule.indent_size = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_false_align_paren_true_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_true_align_paren_true_smart_tabs(self):
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "yes"
        oRule.align_paren = "yes"
        oRule.indent_size = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "constant")
        self.assertEqual(oRule.identifier, "012")

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.append(18)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 33))
        lExpected.extend(range(34, 40))
        lExpected.extend(range(42, 56))
        lExpected.extend(range(58, 74))
        lExpected.extend(range(80, 96))
        lExpected.extend(range(105, 110))
        lExpected.extend(range(116, 127))
        lExpected.extend(range(129, 135))
        lExpected.extend(range(137, 140))
        lExpected.extend(range(142, 154))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_true_align_paren_true_smart_tabs(self):
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "yes"
        oRule.align_paren = "yes"
        oRule.indent_size = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_align_paren_true_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_align_left_false_align_paren_true_indent_step_2_smart_tabs(self):
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "no"
        oRule.align_paren = "yes"
        oRule.indent_size = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_false_align_paren_true_indent_step_2_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_align_left_true_indent_step_2_smart_tabs(self):
        oRule = constant.rule_012()
        oRule.indent_style = "smart_tabs"
        oRule.align_left = "yes"
        oRule.align_paren = "no"
        oRule.indent_size = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_indent_step_2_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_blank_line_indent(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

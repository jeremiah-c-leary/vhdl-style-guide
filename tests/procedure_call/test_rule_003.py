# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import procedure_call

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_003_test_input.vhd"))

lExpected_first_open_paren__add_new_line = []
lExpected_first_open_paren__add_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed_first_open_paren__add_new_line.vhd"), lExpected_first_open_paren__add_new_line)

lExpected_first_open_paren__remove_new_line = []
lExpected_first_open_paren__remove_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed_first_open_paren__remove_new_line.vhd"), lExpected_first_open_paren__remove_new_line)

lExpected_last_close_paren__add_new_line = []
lExpected_last_close_paren__add_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed_last_close_paren__add_new_line.vhd"), lExpected_last_close_paren__add_new_line)

lExpected_last_close_paren__remove_new_line = []
lExpected_last_close_paren__remove_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed_last_close_paren__remove_new_line.vhd"), lExpected_last_close_paren__remove_new_line)

lExpected_association_list_comma__remove_new_line = []
lExpected_association_list_comma__remove_new_line.append("")
utils.read_file(
    os.path.join(sTestDir, "rule_003_test_input.fixed_association_list_comma__remove_new_line.vhd"),
    lExpected_association_list_comma__remove_new_line,
)

lExpected_association_element__add_new_line = []
lExpected_association_element__add_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed_association_element__add_new_line.vhd"), lExpected_association_element__add_new_line)

lExpected_association_element__remove_new_line = []
lExpected_association_element__remove_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed_association_element__remove_new_line.vhd"), lExpected_association_element__remove_new_line)

lExpected_ignore_single_line__yes = []
lExpected_ignore_single_line__yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_003_test_input.fixed_ignore_single_line__yes.vhd"), lExpected_ignore_single_line__yes)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_003_first_open_paren__add_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertEqual(oRule.groups, ["structure"])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [6, 8, 11, 16, 19, 40, 51, 53]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_first_open_paren__add_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_open_paren__add_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_first_open_paren__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "remove_new_line"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_first_open_paren__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "remove_new_line"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_open_paren__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_last_close_paren__add_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "add_new_line"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [6, 9, 14, 51]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_last_close_paren__add_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "add_new_line"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_close_paren__add_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_last_close_paren__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "remove_new_line"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [17, 24, 34, 45, 58]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_last_close_paren__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "remove_new_line"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_close_paren__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_association_list_comma__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "remove_new_line"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [29, 32]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_association_list_comma__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "remove_new_line"
        oRule.association_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_association_list_comma__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_association_element__add_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "add_new_line"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [6, 6, 6, 6, 9, 9, 9, 11, 16, 16, 16, 16, 51, 51, 51, 51]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_association_element__add_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "add_new_line"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_association_element__add_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_association_element__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "remove_new_line"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [8, 11, 12, 13, 19, 20, 21, 22, 27, 29, 30, 32, 40, 41, 42, 43, 53, 54, 55, 56]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_association_element__remove_new_line(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "remove_new_line"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_association_element__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_ignore_single_line__yes(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "add_new_line"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "add_new_line"
        oRule.ignore_single_line = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure_call")
        self.assertEqual(oRule.identifier, "003")

        lExpected = [8, 9, 9, 9, 9, 11, 11, 14, 16, 16, 16, 16, 16, 19, 40, 53]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_ignore_single_line__yes(self):
        oRule = procedure_call.rule_003()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "add_new_line"
        oRule.association_list_comma = "ignore"
        oRule.association_element = "add_new_line"
        oRule.ignore_single_line = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_ignore_single_line__yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

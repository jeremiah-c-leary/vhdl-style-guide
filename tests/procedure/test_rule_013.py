# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import procedure

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_013_test_input.vhd"))

lExpected_first_open_paren__add_new_line = []
lExpected_first_open_paren__add_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_first_open_paren__add_new_line.vhd"), lExpected_first_open_paren__add_new_line)

lExpected_first_open_paren__remove_new_line = []
lExpected_first_open_paren__remove_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_first_open_paren__remove_new_line.vhd"), lExpected_first_open_paren__remove_new_line)

lExpected_last_close_paren__add_new_line = []
lExpected_last_close_paren__add_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_last_close_paren__add_new_line.vhd"), lExpected_last_close_paren__add_new_line)

lExpected_last_close_paren__remove_new_line = []
lExpected_last_close_paren__remove_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_last_close_paren__remove_new_line.vhd"), lExpected_last_close_paren__remove_new_line)

lExpected_interface_list_semicolon__remove_new_line = []
lExpected_interface_list_semicolon__remove_new_line.append("")
utils.read_file(
    os.path.join(sTestDir, "rule_013_test_input.fixed_interface_list_semicolon__remove_new_line.vhd"),
    lExpected_interface_list_semicolon__remove_new_line,
)

lExpected_interface_element__add_new_line = []
lExpected_interface_element__add_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_interface_element__add_new_line.vhd"), lExpected_interface_element__add_new_line)

lExpected_interface_element__remove_new_line = []
lExpected_interface_element__remove_new_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_interface_element__remove_new_line.vhd"), lExpected_interface_element__remove_new_line)

lExpected_ignore_single_line__yes = []
lExpected_ignore_single_line__yes.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_ignore_single_line__yes.vhd"), lExpected_ignore_single_line__yes)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_013_first_open_paren__add_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertEqual(oRule.groups, ["structure"])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [3, 11, 13, 16, 19, 34]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_first_open_paren__add_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_open_paren__add_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_013_first_open_paren__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "remove_new_line"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_first_open_paren__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "remove_new_line"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_open_paren__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_013_last_close_paren__add_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "add_new_line"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [11, 14, 24, 32]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_last_close_paren__add_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "add_new_line"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_close_paren__add_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_013_last_close_paren__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "remove_new_line"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [9, 17, 45]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_last_close_paren__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "remove_new_line"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_close_paren__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_013_interface_list_semicolon__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "remove_new_line"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [36, 38, 41]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_interface_list_semicolon__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "remove_new_line"
        oRule.interface_element = "ignore"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_interface_list_semicolon__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_013_interface_element__add_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "add_new_line"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [11, 11, 11, 11, 11, 14, 14, 14, 14, 16, 16, 16, 16, 16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_interface_element__add_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "add_new_line"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_interface_element__add_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_013_interface_element__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "remove_new_line"
        oRule.ignore_single_line = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [4, 5, 6, 7, 8, 14, 20, 21, 22, 23, 24, 28, 29, 30, 31, 32, 35, 37, 39, 42, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_interface_element__remove_new_line(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "ignore"
        oRule.last_close_paren = "ignore"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "remove_new_line"
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_interface_element__remove_new_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_013_ignore_single_line__yes(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "add_new_line"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "add_new_line"
        oRule.ignore_single_line = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [3, 13, 14, 14, 14, 14, 14, 16, 16, 16, 16, 16, 16, 19, 24, 32, 34]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_013_ignore_single_line__yes(self):
        oRule = procedure.rule_013()
        oRule.first_open_paren = "add_new_line"
        oRule.last_close_paren = "add_new_line"
        oRule.interface_list_semicolon = "ignore"
        oRule.interface_element = "add_new_line"
        oRule.ignore_single_line = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_ignore_single_line__yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

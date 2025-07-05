# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import comment

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_010_test_input.vhd"))

dIndentMap = utils.read_indent_file()


class test_comment_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_010_false_false(self):
        oRule = comment.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "comment")
        self.assertEqual(oRule.identifier, "010")

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = False
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = False
        self.oFile.set_indent_map(dIndentMap)

        lExpected = [3, 8, 10, 11, 14, 15, 16, 19, 27, 28, 33, 34, 66, 68, 74, 80, 86, 99]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_010_false_false(self):
        oRule = comment.rule_010()

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = False
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = False
        self.oFile.set_indent_map(dIndentMap)

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_010_test_input.fixed_false_false.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_010_false_true(self):
        oRule = comment.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "comment")
        self.assertEqual(oRule.identifier, "010")

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = False
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = True
        self.oFile.set_indent_map(dIndentMap)

        lExpected = [3, 8, 10, 11, 14, 15, 16, 27, 28, 32, 34, 66, 99]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_010_false_true(self):
        oRule = comment.rule_010()

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = False
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = True
        self.oFile.set_indent_map(dIndentMap)

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_010_test_input.fixed_false_true.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_010_true_false(self):
        oRule = comment.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "comment")
        self.assertEqual(oRule.identifier, "010")

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = True
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = False
        self.oFile.set_indent_map(dIndentMap)

        lExpected = [3, 8, 10, 11, 14, 15, 16, 19, 26, 28, 33, 34, 68, 74, 80, 86, 99]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_010_true_false(self):
        oRule = comment.rule_010()

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = True
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = False
        self.oFile.set_indent_map(dIndentMap)

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_010_test_input.fixed_true_false.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_010_true_true(self):
        oRule = comment.rule_010()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "comment")
        self.assertEqual(oRule.identifier, "010")

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = True
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = True
        self.oFile.set_indent_map(dIndentMap)

        lExpected = [3, 8, 10, 11, 14, 15, 16, 26, 28, 32, 34, 99]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_010_true_true(self):
        oRule = comment.rule_010()

        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_declarative_part"] = True
        dIndentMap["indent"]["options"]["comment"]["align_with_end_of_statement_part"] = True
        self.oFile.set_indent_map(dIndentMap)

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_010_test_input.fixed_true_true.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

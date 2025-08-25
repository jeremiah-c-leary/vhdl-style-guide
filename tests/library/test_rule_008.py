# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import library

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_008_test_input.vhd"))

dIndentMap = utils.read_indent_file()


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_008(self):
        oRule = library.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "library")
        self.assertEqual(oRule.identifier, "008")

        lExpected = [10, 11, 21, 28, 42, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_008(self):
        oRule = library.rule_008()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_008_test_input.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_008_indent_size_zero(self):
        oRule = library.rule_008()
        oRule.indent_size = 0

        lExpected = [3, 4, 10, 11, 21, 28, 35, 42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_008_indent_size_zero(self):
        oRule = library.rule_008()
        oRule.indent_size = 0

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_008_test_input.fixed_with_indent_size_0.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_008_token_if_no_matching_library_clause_current(self):
        oRule = library.rule_008()

        lExpected = [10, 11, 21, 28, 35, 42, 44]

        dIndentMap = utils.read_indent_file()
        dIndentMap["indent"]["tokens"]["use_clause"]["keyword"]["token_if_no_matching_library_clause"] = "current"

        self.oFile.set_indent_map(dIndentMap)

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_008_token_if_no_matching_library_clause_current(self):
        oRule = library.rule_008()

        dIndentMap = utils.read_indent_file()
        dIndentMap["indent"]["tokens"]["use_clause"]["keyword"]["token_if_no_matching_library_clause"] = "current"

        self.oFile.set_indent_map(dIndentMap)

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_008_test_input.fixed_token_if_no_matching_library_clause_current.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import process

sTestDir = os.path.dirname(__file__)

dIndentMap = utils.read_indent_file()

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_028_test_input.vhd"))

lExpected_spaces = []
lExpected_spaces.append("")
utils.read_file(os.path.join(sTestDir, "rule_028_test_input.fixed_spaces.vhd"), lExpected_spaces)

lExpected_smart_tabs = []
lExpected_smart_tabs.append("")
utils.read_file(os.path.join(sTestDir, "rule_028_test_input.fixed_smart_tabs.vhd"), lExpected_smart_tabs)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_028_spaces(self):
        oRule = process.rule_028()
        oRule.align_to = "keyword"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "process")
        self.assertEqual(oRule.identifier, "028")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [19, 24, 30, 35, 40, 45]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_028_spaces(self):
        oRule = process.rule_028()
        oRule.align_to = "keyword"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_028_smart_tabs(self):
        oRule = process.rule_028()
        oRule.indent_style = "smart_tabs"
        oRule.align_to = "keyword"

        lExpected = [12, 19, 24, 30, 40, 45]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_028_smart_tabs(self):
        oRule = process.rule_028()
        oRule.indent_style = "smart_tabs"
        oRule.align_to = "keyword"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_028_spaces_align_to_current_indent(self):
        oRule = process.rule_028()
        oRule.align_to = "current_indent"

        lExpected = [12, 19, 24, 30, 35, 40, 45]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_028_spaces_align_to_current_indent(self):
        oRule = process.rule_028()
        oRule.align_to = "current_indent"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_028_test_input.fixed_align_to_current_indent.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

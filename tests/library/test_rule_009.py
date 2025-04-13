# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import library

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_009_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected_spaces = []
lExpected_spaces.append("")
utils.read_file(os.path.join(sTestDir, "rule_009_test_input.fixed_spaces.vhd"), lExpected_spaces)

lExpected_smart_tabs = []
lExpected_smart_tabs.append("")
utils.read_file(os.path.join(sTestDir, "rule_009_test_input.fixed_smart_tabs.vhd"), lExpected_smart_tabs)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_009_spaces(self):
        oRule = library.rule_009()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "library")
        self.assertEqual(oRule.identifier, "009")

        lExpected = [9, 11, 13, 15, 19]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_009_spaces(self):
        oRule = library.rule_009()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_009_smart_tabs(self):
        oRule = library.rule_009()
        oRule.indent_style = "smart_tabs"

        lExpected = [3, 5, 9, 12, 13, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_009_smart_tabs(self):
        oRule = library.rule_009()
        oRule.indent_style = "smart_tabs"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

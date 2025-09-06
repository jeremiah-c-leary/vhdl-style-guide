# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import signal

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_001_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected_spaces = []
lExpected_spaces.append("")
utils.read_file(os.path.join(sTestDir, "rule_001_test_input.fixed_spaces.vhd"), lExpected_spaces)

lExpected_smart_tabs = []
lExpected_smart_tabs.append("")
utils.read_file(os.path.join(sTestDir, "rule_001_test_input.fixed_smart_tabs.vhd"), lExpected_smart_tabs)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_001_spaces(self):
        oRule = signal.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "signal")
        self.assertEqual(oRule.identifier, "001")

        lExpected = [5, 9, 10, 13, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_spaces(self):
        oRule = signal.rule_001()
        oRule.indent_style = "spaces"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_001_smart_tabs(self):
        oRule = signal.rule_001()
        oRule.indent_style = "smart_tabs"

        lExpected = [4, 9, 10, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_smart_tabs(self):
        oRule = signal.rule_001()
        oRule.indent_style = "smart_tabs"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

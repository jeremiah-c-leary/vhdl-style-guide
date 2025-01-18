# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import if_statement

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_009_test_input_smarttabs.vhd"))

dIndentMap = utils.read_indent_file()


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_009(self):
        oRule = if_statement.rule_009()
        oRule.indent_style = "smart_tabs"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "if")
        self.assertEqual(oRule.identifier, "009")
        self.assertEqual(oRule.align_left, "no")
        self.assertEqual(oRule.align_paren, "yes")

        lExpected = [25, 26, 29, 30, 39, 50]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_009(self):
        oRule = if_statement.rule_009()
        oRule.indent_style = "smart_tabs"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")

        utils.read_file(os.path.join(sTestDir, "rule_009_test_input_smarttabs.fixed.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

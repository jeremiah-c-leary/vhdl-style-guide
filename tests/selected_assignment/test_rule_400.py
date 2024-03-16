# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import selected_assignment

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_400_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected_align_left_yes_align_paren_no = []
lExpected_align_left_yes_align_paren_no.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed.vhd"), lExpected_align_left_yes_align_paren_no)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_400_align_left_yes_align_paren_no(self):
        oRule = selected_assignment.rule_400()
        oRule.align_left = "yes"
        oRule.align_paren = "no"

        lExpected = [39, 40, 41, 44, 45, 46, 49, 50, 51, 56, 57, 58, 63, 64, 65]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_400_align_left_true_align_paren_false(self):
        oRule = selected_assignment.rule_400()
        oRule.align_left = True
        oRule.align_paren = False

        lExpected = [39, 40, 41, 44, 45, 46, 49, 50, 51, 56, 57, 58, 63, 64, 65]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_align_left_yes_align_paren_no(self):
        oRule = selected_assignment.rule_400()
        oRule.align_left = "yes"
        oRule.align_paren = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

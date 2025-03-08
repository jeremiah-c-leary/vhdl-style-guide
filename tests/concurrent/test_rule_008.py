# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import concurrent

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_008_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_008_yes_yes_yes_no(self):
        oRule = concurrent.rule_008()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.include_lines_without_comment = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "concurrent")
        self.assertEqual(oRule.identifier, "008")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [15, 16, 17, 18, 29, 30, 31, 33, 53, 54, 61, 62, 71]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_008_true_true_true_false(self):
        oRule = concurrent.rule_008()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.include_lines_without_comment = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "concurrent")
        self.assertEqual(oRule.identifier, "008")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [15, 16, 17, 18, 29, 30, 31, 33, 53, 54, 61, 62, 71]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_008_yes_yes_yes_no(self):
        oRule = concurrent.rule_008()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.include_lines_without_comment = "no"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_008_test_input.fixed_yes_yes_yes_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

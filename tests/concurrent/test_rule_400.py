# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import concurrent

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_400_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400_no_no(self):
        oRule = concurrent.rule_400()
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "concurrent")
        self.assertEqual(oRule.identifier, "400")

        lExpected = [10, 14, 15, 16]
        lExpected.extend([26])
        lExpected.extend([33, 34, 35])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_no_no(self):
        oRule = concurrent.rule_400()
        oRule.aggregate_parens_ends_group = "no"
        oRule.ignore_single_line_aggregates = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_no_no.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400_yes_no(self):
        oRule = concurrent.rule_400()
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "no"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "concurrent")
        self.assertEqual(oRule.identifier, "400")

        lExpected = [10, 14, 15, 16]
        lExpected.extend([27])
        lExpected.extend([33, 34, 35])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_yes_no(self):
        oRule = concurrent.rule_400()
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_yes_no.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400_yes_yes(self):
        oRule = concurrent.rule_400()
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "yes"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "concurrent")
        self.assertEqual(oRule.identifier, "400")

        lExpected = [10, 14, 15, 16]
        lExpected.extend([33, 34, 35])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_yes_yes(self):
        oRule = concurrent.rule_400()
        oRule.aggregate_parens_ends_group = "yes"
        oRule.ignore_single_line_aggregates = "yes"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_yes_yes.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

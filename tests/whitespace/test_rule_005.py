# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import whitespace

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_005_test_input.vhd"))

lExpected_ignore_spaces_before_numbers_false = []
lExpected_ignore_spaces_before_numbers_false.append("")
utils.read_file(os.path.join(sTestDir, "rule_005_test_input.fixed_ignore_spaces_before_numbers_false.vhd"), lExpected_ignore_spaces_before_numbers_false)

lExpected_ignore_spaces_before_numbers_true = []
lExpected_ignore_spaces_before_numbers_true.append("")
utils.read_file(os.path.join(sTestDir, "rule_005_test_input.fixed_ignore_spaces_before_numbers_true.vhd"), lExpected_ignore_spaces_before_numbers_true)


class test_whitespace_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_005_ignore_spaces_before_numbers_false(self):
        oRule = whitespace.rule_005()
        oRule.ignore_spaces_before_numbers = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "whitespace")
        self.assertEqual(oRule.identifier, "005")
        self.assertEqual(oRule.groups, ["whitespace"])

        lExpected = [5, 10, 12]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_005_ignore_spaces_before_numbers_true(self):
        oRule = whitespace.rule_005()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "whitespace")
        self.assertEqual(oRule.identifier, "005")
        self.assertEqual(oRule.groups, ["whitespace"])

        lExpected = [12]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_005_ignore_spaces_before_numbers_false(self):
        oRule = whitespace.rule_005()
        oRule.ignore_spaces_before_numbers = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_ignore_spaces_before_numbers_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_005_ignore_spaces_before_numbers_true(self):
        oRule = whitespace.rule_005()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_ignore_spaces_before_numbers_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

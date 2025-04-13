# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import selected_assignment

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_503_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_503_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_503_test_input.fixed_upper.vhd"), lExpected_upper)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_503_lower(self):
        oRule = selected_assignment.rule_503()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "selected_assignment")
        self.assertEqual(oRule.identifier, "503")

        lExpected = [38, 39, 40, 43, 44, 45, 48, 49, 50, 55, 56, 57, 65, 66, 67, 70, 71, 72, 75, 76, 77, 82, 83, 84]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_503_upper(self):
        oRule = selected_assignment.rule_503()
        oRule.case = "upper"

        lExpected = [11, 12, 13, 16, 17, 18, 21, 22, 23, 28, 29, 30, 38, 39, 40, 43, 44, 45, 48, 49, 50, 55, 56, 57]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_503_lower(self):
        oRule = selected_assignment.rule_503()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_503_upper(self):
        oRule = selected_assignment.rule_503()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

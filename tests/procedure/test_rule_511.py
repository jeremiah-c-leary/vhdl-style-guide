# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import procedure

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_511_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_511_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_511_test_input.fixed_upper.vhd"), lExpected_upper)


class test_function_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_511_lower(self):
        oRule = procedure.rule_511()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "511")

        lExpected = [13, 14, 15, 16, 36, 37, 38, 39]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_511_upper(self):
        oRule = procedure.rule_511()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "procedure")
        self.assertEqual(oRule.identifier, "511")

        lExpected = [5, 6, 7, 8, 25, 26, 27, 28]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_511_lower(self):
        oRule = procedure.rule_511()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_511_upper(self):
        oRule = procedure.rule_511()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

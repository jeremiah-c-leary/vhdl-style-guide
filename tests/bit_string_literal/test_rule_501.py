# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import bit_string_literal

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_501_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_501_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_501_test_input.fixed_upper.vhd"), lExpected_upper)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_501_lower(self):
        oRule = bit_string_literal.rule_501()
        oRule.case = "lower"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "bit_string_literal")
        self.assertEqual(oRule.identifier, "501")

        lExpected = [9, 12, 14, 15, 17, 18, 19, 20, 22, 23, 24, 27, 28, 30, 39, 42, 44, 45, 47, 48, 49, 50, 52, 53, 54, 57, 58, 60]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_501_upper(self):
        oRule = bit_string_literal.rule_501()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "bit_string_literal")
        self.assertEqual(oRule.identifier, "501")

        lExpected = [
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            86,
            87,
            88,
            89,
            90,
            91,
            92,
            93,
            94,
            103,
            104,
            105,
            106,
            107,
            108,
            109,
            110,
            111,
            117,
            118,
            119,
            120,
            121,
            122,
            123,
            124,
            125,
        ]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_501_lower(self):
        oRule = bit_string_literal.rule_501()
        oRule.case = "lower"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_501_upper(self):
        oRule = bit_string_literal.rule_501()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

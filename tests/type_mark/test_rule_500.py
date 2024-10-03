# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import type_mark

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_500_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_500_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_500_test_input.fixed_upper.vhd"), lExpected_upper)


class test_type_definition_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_500_lower(self):
        oRule = type_mark.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "type_mark")
        self.assertEqual(oRule.identifier, "500")

        lExpected = [
            88,
            89,
            90,
            91,
            92,
            95,
            96,
            98,
            99,
            100,
            101,
            111,
            112,
            113,
            114,
            115,
            116,
            118,
            119,
            120,
            121,
            122,
            123,
            124,
            125,
            126,
            127,
            128,
            129,
            131,
            132,
            135,
            137,
            138,
            144,
            145,
            146,
            147,
            148,
            151,
            152,
            154,
            155,
            156,
            157,
        ]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_500_upper(self):
        oRule = type_mark.rule_500()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "type_mark")
        self.assertEqual(oRule.identifier, "500")

        lExpected = [
            5,
            6,
            7,
            8,
            9,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            28,
            29,
            30,
            31,
            32,
            33,
            35,
            36,
            37,
            38,
            39,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            48,
            49,
            52,
            54,
            55,
            61,
            62,
            63,
            64,
            65,
            68,
            69,
            70,
            71,
            72,
            73,
            74,
            75,
            97,
            102,
            153,
            158,
        ]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_500_lower(self):
        oRule = type_mark.rule_500()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_500_upper(self):
        oRule = type_mark.rule_500()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

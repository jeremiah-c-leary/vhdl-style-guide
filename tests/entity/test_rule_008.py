# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import entity

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_008_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_008_lower(self):
        oRule = entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "008")

        lExpected = []
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(17, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_008_lower(self):
        oRule = entity.rule_008()

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_008_test_input.fixed_lower.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_008_upper(self):
        oRule = entity.rule_008()
        oRule.case = "upper"

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(8, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(17, 21))
        lExpected.extend(range(23, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_008_upper(self):
        oRule = entity.rule_008()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_008_test_input.fixed_upper.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_008_camelCase(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"

        lExpected = []
        lExpected.extend(range(3, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(13, 16))
        lExpected.extend(range(17, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(38, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(53, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(63, 66))
        lExpected.extend(range(71, 73))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend(range(4, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(14, 16))
        lExpected.extend(range(17, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(39, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(54, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(64, 66))
        lExpected.extend(range(71, 73))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([3, 5])
        lExpected.extend(range(7, 11))
        lExpected.extend([13, 15])
        lExpected.extend(range(17, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend([38, 40])
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend([53, 55])
        lExpected.extend(range(57, 61))
        lExpected.extend([63, 65])
        lExpected.extend(range(71, 73))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend(range(7, 11))
        lExpected.extend(range(17, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(71, 73))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.case_exceptions.append("e_MyFifo")

        lExpected = []
        lExpected.extend(range(3, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(13, 16))
        lExpected.extend(range(17, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend([32, 34, 35])
        lExpected.extend(range(38, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(53, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(63, 66))
        lExpected.extend(range(71, 73))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_relaxedCamelCase(self):
        oRule = entity.rule_008()
        oRule.case = "relaxedCamelCase"

        lExpected = []
        lExpected.extend(range(3, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(13, 16))
        lExpected.extend(range(17, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(38, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(48, 51))
        lExpected.extend(range(53, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(63, 66))
        lExpected.extend([72, 75])
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(18, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(33, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(58, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(93, 95))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(19, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(34, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(59, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(93, 95))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend([18, 20])
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend([33, 35])
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend([58, 60])
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(93, 95))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(93, 95))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.case_exceptions.append("myFifo")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(18, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(33, 36))
        lExpected.extend(range(38, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(58, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(70, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))
        lExpected.extend(range(93, 95))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_RelaxedPascalCase(self):
        oRule = entity.rule_008()
        oRule.case = "RelaxedPascalCase"

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(18, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(33, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(43, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(58, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(18, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(85, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(19, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(86, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend([18, 20])
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend([85, 87])
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.case_exceptions.append("myFifo")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(7, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(18, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(32, 36))
        lExpected.extend(range(38, 41))
        lExpected.extend(range(42, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(57, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(70, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(85, 88))
        lExpected.extend(range(91, 98))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(8, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(18, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(33, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(43, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(58, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(9, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(19, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(34, 36))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(44, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(59, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend([8, 10])
        lExpected.extend(range(12, 16))
        lExpected.extend([18, 20])
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend([33, 35])
        lExpected.extend(range(37, 41))
        lExpected.extend([43, 45])
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend([58, 60])
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(37, 41))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(69, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.case_exceptions.append("myFifo")

        lExpected = []
        lExpected.extend(range(2, 6))
        lExpected.extend(range(8, 11))
        lExpected.extend(range(12, 16))
        lExpected.extend(range(18, 21))
        lExpected.extend(range(22, 26))
        lExpected.extend(range(27, 31))
        lExpected.extend(range(33, 36))
        lExpected.extend(range(38, 41))
        lExpected.extend(range(43, 46))
        lExpected.extend(range(47, 51))
        lExpected.extend(range(52, 56))
        lExpected.extend(range(58, 61))
        lExpected.extend(range(62, 66))
        lExpected.extend(range(70, 76))
        lExpected.extend(range(79, 83))
        lExpected.extend(range(84, 88))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

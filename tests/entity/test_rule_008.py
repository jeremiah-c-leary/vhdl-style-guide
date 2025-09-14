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
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

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
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

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
        lExpected.extend([3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([13, 14, 15])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend([4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([14, 15])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([3, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([13, 15])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([38, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([53, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([63, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "camelCase"
        oRule.case_exceptions.append("e_MyFifo")

        lExpected = []
        lExpected.extend([3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([13, 14, 15])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 34, 35])
        lExpected.extend([38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_relaxedCamelCase(self):
        oRule = entity.rule_008()
        oRule.case = "relaxedCamelCase"

        lExpected = []
        lExpected.extend([3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([13, 14, 15])
        lExpected.extend([17, 18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([48, 49, 50])
        lExpected.extend([53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([83, 84])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([83, 84])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([33, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([58, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([83, 84])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([83, 84])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "PascalCase"
        oRule.case_exceptions.append("myFifo")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([33, 34, 35])
        lExpected.extend([38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])
        lExpected.extend([83, 84])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_RelaxedPascalCase(self):
        oRule = entity.rule_008()
        oRule.case = "RelaxedPascalCase"

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([75, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_Pascal_Snake_Case_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "Pascal_Snake_Case"
        oRule.case_exceptions.append("myFifo")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([7, 8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([32, 33, 34, 35])
        lExpected.extend([38, 39, 40])
        lExpected.extend([42, 43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([57, 58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([75, 76, 77])
        lExpected.extend([81, 82, 83, 84, 85, 86, 87])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([33, 34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.prefix_exceptions.append("e_")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([34, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([8, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([33, 35])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([43, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([58, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.prefix_exceptions.append("e_")
        oRule.suffix_exceptions.append("_a")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_regex_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = "regex"
        oRule.regex = r"[A-Z][A-Za-z\d]*"
        oRule.case_exceptions.append("myFifo")

        lExpected = []
        lExpected.extend([2, 3, 4, 5])
        lExpected.extend([8, 9, 10])
        lExpected.extend([12, 13, 14, 15])
        lExpected.extend([18, 19, 20])
        lExpected.extend([22, 23, 24, 25])
        lExpected.extend([27, 28, 29, 30])
        lExpected.extend([33, 34, 35])
        lExpected.extend([38, 39, 40])
        lExpected.extend([43, 44, 45])
        lExpected.extend([47, 48, 49, 50])
        lExpected.extend([52, 53, 54, 55])
        lExpected.extend([58, 59, 60])
        lExpected.extend([62, 63, 64, 65])
        lExpected.extend([69, 70, 71, 72])
        lExpected.extend([74, 75, 76, 77])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

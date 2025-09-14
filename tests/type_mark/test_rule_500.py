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


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_500_lower(self):
        oRule = type_mark.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "type_mark")
        self.assertEqual(oRule.identifier, "500")

        lExpected = []
        lExpected.extend(range(88, 93))
        lExpected.extend(range(95, 103))
        lExpected.extend(range(112, 117))
        lExpected.extend([118])
        lExpected.extend(range(126, 130))
        lExpected.extend(range(131, 133))
        lExpected.extend([135])
        lExpected.extend(range(137, 139))
        lExpected.extend(range(144, 149))
        lExpected.extend(range(151, 159))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_500_upper(self):
        oRule = type_mark.rule_500()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "type_mark")
        self.assertEqual(oRule.identifier, "500")

        lExpected = []
        lExpected.extend(range(5, 10))
        lExpected.extend(range(12, 20))
        lExpected.extend(range(29, 34))
        lExpected.extend([35])
        lExpected.extend(range(43, 47))
        lExpected.extend(range(48, 50))
        lExpected.extend([52])
        lExpected.extend(range(54, 56))
        lExpected.extend(range(61, 66))
        lExpected.extend(range(68, 76))

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

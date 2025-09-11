# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import attribute

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
        oRule = attribute.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "attribute")
        self.assertEqual(oRule.identifier, "500")

        lExpected = []
        lExpected.extend(range(5, 19))
        lExpected.extend(range(21, 29))
        lExpected.extend(range(31, 42))
        lExpected.extend(range(44, 47))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_500_upper(self):
        oRule = attribute.rule_500()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "attribute")
        self.assertEqual(oRule.identifier, "500")

        lExpected = []
        lExpected.extend(range(5, 19))
        lExpected.extend(range(21, 29))
        lExpected.extend(range(31, 42))
        lExpected.extend(range(44, 47))

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_500_lower(self):
        oRule = attribute.rule_500()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_500_upper(self):
        oRule = attribute.rule_500()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import protected_type_body

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_501_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_501_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_501_test_input.fixed_upper.vhd"), lExpected_upper)


class test_protected_type_body_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_501_lower(self):
        oRule = protected_type_body.rule_501()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "protected_type_body")
        self.assertEqual(oRule.identifier, "501")

        lExpected = [7, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_501_upper(self):
        oRule = protected_type_body.rule_501()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "protected_type_body")
        self.assertEqual(oRule.identifier, "501")

        lExpected = [4, 14]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_501_lower(self):
        oRule = protected_type_body.rule_501()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_501_upper(self):
        oRule = protected_type_body.rule_501()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

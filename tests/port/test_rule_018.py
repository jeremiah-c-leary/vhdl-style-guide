# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import port

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_018_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_018_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_018_test_input.fixed_upper.vhd"), lExpected_upper)


class test_port_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_018_lower(self):
        oRule = port.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "port")
        self.assertEqual(oRule.identifier, "018")
        self.assertEqual(oRule.groups, ["case", "case::keyword"])

        lExpected = [23, 24, 26, 27, 28, 29]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_018_upper(self):
        oRule = port.rule_018()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "port")
        self.assertEqual(oRule.identifier, "018")

        lExpected = [5, 6, 8, 9, 10, 11]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_018_lower(self):
        oRule = port.rule_018()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_018_upper(self):
        oRule = port.rule_018()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import process

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_013_test_input.vhd"))

lExpected_lower = []
lExpected_lower.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_lower.vhd"), lExpected_lower)

lExpected_upper = []
lExpected_upper.append("")
utils.read_file(os.path.join(sTestDir, "rule_013_test_input.fixed_upper.vhd"), lExpected_upper)


class test_process_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_013_lower(self):
        oRule = process.rule_013()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "process")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [13]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_013_upper(self):
        oRule = process.rule_013()
        oRule.case = "upper"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "process")
        self.assertEqual(oRule.identifier, "013")

        lExpected = [7]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_013_lower(self):
        oRule = process.rule_013()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_013_upper(self):
        oRule = process.rule_013()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

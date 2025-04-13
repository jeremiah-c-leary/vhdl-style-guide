# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import generate

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_002_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed.vhd"), lExpected)

lExpected_w_0_spaces = []
lExpected_w_0_spaces.append("")
utils.read_file(os.path.join(sTestDir, "rule_002_test_input.fixed_w_0_spaces.vhd"), lExpected_w_0_spaces)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_002(self):
        oRule = generate.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "002")

        lExpected = [20, 24, 28]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002(self):
        oRule = generate.rule_002()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_002_with_0_spaces(self):
        oRule = generate.rule_002()
        oRule.number_of_spaces = 0

        lExpected = [6, 10, 14, 24, 28]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002_with_0_spaces(self):
        oRule = generate.rule_002()
        oRule.number_of_spaces = 0

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_w_0_spaces, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

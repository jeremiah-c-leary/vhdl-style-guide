# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import variable_assignment

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_400_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed.vhd"), lExpected)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400(self):
        oRule = variable_assignment.rule_400()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable_assignment")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [9, 10, 11]
        lExpected.extend([14, 15, 16])
        lExpected.extend([19, 20, 21])
        lExpected.extend([24, 25, 26, 27])
        lExpected.extend([30, 31, 32, 33, 34])
        lExpected.extend([37, 38, 39, 40])
        lExpected.extend([45, 46, 47, 48, 49])
        lExpected.extend([52, 53, 54, 55, 56])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400(self):
        oRule = variable_assignment.rule_400()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import function

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_508_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_508_test_input.fixed.vhd"), lExpected)


class test_function_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)
        self.maxDiff = None

    def test_rule_508(self):
        oRule = function.rule_508()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "function")
        self.assertEqual(oRule.identifier, "508")
        self.assertEqual(oRule.groups, ["case", "case::name"])

        lExpected = []
        lExpected.extend([12, 13, 16, 17, 18, 19, 20, 30, 31, 32, 33, 34, 37, 37, 38, 38, 43, 43, 43, 43, 44, 44, 44])
        lExpected.extend([44, 45, 45, 45, 45, 46, 46, 46, 46, 47, 47, 47, 47, 48, 48, 49, 49, 50, 50, 51, 51, 51, 51])
        lExpected.extend([52, 52, 53, 53, 54, 54, 56, 56, 63, 63, 64, 64, 65, 65, 66, 66, 67, 67, 68, 69, 70, 71, 71])
        lExpected.extend([72, 73, 74, 77, 77, 78, 78, 79, 79, 80, 80, 81, 81, 94, 95, 100, 100, 101, 101, 102, 102])
        lExpected.extend([103, 103, 104, 104, 105, 106, 107, 108, 108, 109, 110, 111, 113])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_508(self):
        oRule = function.rule_508()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

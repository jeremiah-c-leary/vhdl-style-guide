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


class test_rule(unittest.TestCase):
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
        lExpected.extend([13, 14, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 25, 26, 27, 27, 28, 29, 30, 32, 71, 72])
        lExpected.extend([82, 94, 99, 99, 100, 100, 101, 101, 102, 102, 103, 103, 104, 105, 107, 107, 108, 109, 112])
        lExpected.extend([119, 119, 120, 120, 121, 121, 122, 122, 123, 123, 124, 125, 126, 127, 127, 128, 129, 130])
        lExpected.extend([133, 134, 135, 136, 137, 174, 179, 180, 181, 182, 183, 183, 185, 186, 187, 187, 189, 190])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_508(self):
        oRule = function.rule_508()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

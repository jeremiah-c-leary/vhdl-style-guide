# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import block

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_201_test_input.vhd"))

lExpected_require_blank_line = []
lExpected_require_blank_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_201_test_input.fixed_require_blank_line.vhd"), lExpected_require_blank_line, False)

lExpected_no_blank_line = []
lExpected_no_blank_line.append("")
utils.read_file(os.path.join(sTestDir, "rule_201_test_input.fixed_no_blank_line.vhd"), lExpected_no_blank_line, False)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_201_require_blank_line(self):
        oRule = block.rule_201()
        oRule.style = "require_blank_line"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "block")
        self.assertEqual(oRule.identifier, "201")

        lExpected = [55, 60, 64]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_201_require_blank_line(self):
        oRule = block.rule_201()
        oRule.style = "require_blank_line"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_require_blank_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_201_no_blank_line(self):
        oRule = block.rule_201()
        oRule.style = "no_blank_line"

        lExpected = [12, 23, 34, 49]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_201_no_blank_line(self):
        oRule = block.rule_201()
        oRule.style = "no_blank_line"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_no_blank_line, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


lFile_issue_1564, eError_issue_1564 = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_201_test_input.issue_1564.vhd"))


class test_rule_issue_1564(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile_issue_1564)
        self.assertIsNone(eError_issue_1564)

    def test_rule_201_does_not_flag_leading_comments(self):
        # A block whose optional "is" keyword is omitted, in a file with no
        # "is"/guard tokens at all, must not be misreported against the leading
        # comment lines (issue #1564).
        oRule = block.rule_201()
        oRule.style = "require_blank_line"

        oRule.analyze(self.oFile)
        self.assertEqual([], utils.extract_violation_lines_from_violation_object(oRule.violations))

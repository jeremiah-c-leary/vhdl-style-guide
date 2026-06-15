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

lFile_block_without_is, eError_block_without_is = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_201_test_input.block_without_is.vhd"))


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

    def test_rule_201_block_without_is_keyword(self):
        # Issue #1564: a block whose optional "is" keyword is omitted, in a
        # file with no other is/guard tokens, was misreported against the
        # leading comment (line 1) instead of the block line. Check both styles.
        self.assertIsNone(eError_block_without_is)

        oRule = block.rule_201()
        oRule.style = "require_blank_line"
        self.oFile = vhdlFile.vhdlFile(lFile_block_without_is)
        oRule.analyze(self.oFile)
        self.assertEqual([], utils.extract_violation_lines_from_violation_object(oRule.violations))

        oRule = block.rule_201()
        oRule.style = "no_blank_line"
        self.oFile = vhdlFile.vhdlFile(lFile_block_without_is)
        oRule.analyze(self.oFile)
        self.assertEqual([9], utils.extract_violation_lines_from_violation_object(oRule.violations))

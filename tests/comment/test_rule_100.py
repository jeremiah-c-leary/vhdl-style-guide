# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import parser, vhdlFile
from vsg.rules import comment

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_100_test_input.vhd"))

dIndentMap = utils.read_indent_file()

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_100_test_input.fixed.vhd"), lExpected)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.oFile.lAllObjects[-2].is_block_comment = True
        self.oFile.lAllObjects[-4].is_block_comment = True
        self.oFile.lAllObjects[-6].is_block_comment = True
        self.oFile.lAllObjects[-8].is_block_comment = True
        self.oFile.lAllObjects[-10].is_block_comment = True
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_100(self):
        oRule = comment.rule_100()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "comment")
        self.assertEqual(oRule.identifier, "100")
        self.assertEqual(oRule.groups, ["whitespace"])

        lExpected = [7, 8, 14, 20, 23]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual('Change "--T" to "-- T"', oRule.violations[0].sSolution)

    def test_fix_rule_100(self):
        oRule = comment.rule_100()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import case_generate_statement

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_400_test_input.vhd"))

lExpected_true = []
lExpected_true.append("")
utils.read_file(os.path.join(sTestDir, "rule_400_test_input.fixed_compact_alignment__true.vhd"), lExpected_true)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400_true(self):
        oRule = case_generate_statement.rule_400()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "case_generate_statement")
        self.assertEqual(oRule.identifier, "400")
        self.assertEqual(oRule.compact_alignment, "yes")
        self.assertEqual(oRule.blank_line_ends_group, "no")
        self.assertEqual(oRule.comment_line_ends_group, "no")
        self.assertEqual(oRule.separate_generic_port_alignment, "no")

        lExpected = [8, 10]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_400_true(self):
        oRule = case_generate_statement.rule_400()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import generate

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_401_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed.vhd"), lExpected)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_401_yes_yes_yes_no_no(self):
        oRule = generate.rule_401()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "401")
        self.assertEqual(oRule.groups, ["alignment"])

        lExpected = [48, 49, 50, 51, 52]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_401(self):
        oRule = generate.rule_401()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

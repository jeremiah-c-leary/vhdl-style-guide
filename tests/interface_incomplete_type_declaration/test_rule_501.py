# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import interface_incomplete_type_declaration

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_501_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_501_lower(self):
        oRule = interface_incomplete_type_declaration.rule_501()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "interface_incomplete_type_declaration")
        self.assertEqual(oRule.identifier, "501")

        lExpected = [5, 6, 18, 19]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_501_lower(self):
        oRule = interface_incomplete_type_declaration.rule_501()

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_501_test_input.fixed_lower.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_501_upper(self):
        oRule = interface_incomplete_type_declaration.rule_501()
        oRule.case = "upper"

        lExpected = [4, 5, 17, 18]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_501_upper(self):
        oRule = interface_incomplete_type_declaration.rule_501()
        oRule.case = "upper"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_501_test_input.fixed_upper.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

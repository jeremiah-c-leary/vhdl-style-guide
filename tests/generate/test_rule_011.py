# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import generate

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_011_test_input.vhd"))

lExpected_add = []
lExpected_add.append("")
utils.read_file(os.path.join(sTestDir, "rule_011_test_input.fixed_add.vhd"), lExpected_add)

lExpected_remove = []
lExpected_remove.append("")
utils.read_file(os.path.join(sTestDir, "rule_011_test_input.fixed_remove.vhd"), lExpected_remove)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_011_add(self):
        oRule = generate.rule_011()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "011")
        self.assertEqual(oRule.groups, ["structure", "structure::optional"])

        lExpected = [22, 26, 30, 40, 44, 46, 52, 56, 58, 60]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_011_add(self):
        oRule = generate.rule_011()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_add, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_011_remove(self):
        oRule = generate.rule_011()
        oRule.action = "remove"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "generate")
        self.assertEqual(oRule.identifier, "011")
        self.assertEqual(oRule.groups, ["structure", "structure::optional"])

        lExpected = [8, 12, 16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_011_remove(self):
        oRule = generate.rule_011()
        oRule.action = "remove"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

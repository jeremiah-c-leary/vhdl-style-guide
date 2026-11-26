# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import interface_list

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_001_test_input.vhd"))

lExpected_add = []
lExpected_add.append("")
utils.read_file(os.path.join(sTestDir, "rule_001_test_input.fixed_add.vhd"), lExpected_add)

lExpected_remove = []
lExpected_remove.append("")
utils.read_file(os.path.join(sTestDir, "rule_001_test_input.fixed_remove.vhd"), lExpected_remove)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_001_remove(self):
        oRule = interface_list.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "interface_list")
        self.assertEqual(oRule.identifier, "001")
        self.assertEqual(oRule.groups, ["structure", "structure::optional"])
        self.assertEqual(oRule.action, "remove")

        lExpected = [5, 19, 28, 39]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_remove(self):
        oRule = interface_list.rule_001()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_001_add(self):
        oRule = interface_list.rule_001()
        oRule.action = "add"

        lExpected = [9, 15, 34, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_add(self):
        oRule = interface_list.rule_001()
        oRule.action = "add"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_add, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import package

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_014_test_input.vhd"))

lExpected_add = []
lExpected_add.append("")
utils.read_file(os.path.join(sTestDir, "rule_014_test_input.fixed_add.vhd"), lExpected_add)

lExpected_remove = []
lExpected_remove.append("")
utils.read_file(os.path.join(sTestDir, "rule_014_test_input.fixed_remove.vhd"), lExpected_remove)


class test_package_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_014_add(self):
        oRule = package.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "package")
        self.assertEqual(oRule.identifier, "014")
        self.assertEqual(oRule.groups, ["structure", "structure::optional"])

        lExpected = [8, 12]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_014_add(self):
        oRule = package.rule_014()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_add, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_014_remove(self):
        oRule = package.rule_014()
        oRule.action = "remove"

        lExpected = [4]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_014_remove(self):
        oRule = package.rule_014()
        oRule.action = "remove"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

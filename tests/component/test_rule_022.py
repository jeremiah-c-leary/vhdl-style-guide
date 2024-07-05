# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import component

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_022_test_input.vhd"))

lExpected_add = []
lExpected_add.append("")
utils.read_file(os.path.join(sTestDir, "rule_022_test_input.fixed_add.vhd"), lExpected_add)

lExpected_remove = []
lExpected_remove.append("")
utils.read_file(os.path.join(sTestDir, "rule_022_test_input.fixed_remove.vhd"), lExpected_remove)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_022_add(self):
        oRule = component.rule_022()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "component")
        self.assertEqual(oRule.identifier, "022")
        self.assertEqual(oRule.groups, ["structure", "structure::optional"])

        lExpected = [10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_022_add(self):
        oRule = component.rule_022()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_add, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_022_remove(self):
        oRule = component.rule_022()
        oRule.action = "remove"

        lExpected = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_022_remove(self):
        oRule = component.rule_022()
        oRule.action = "remove"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_remove, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

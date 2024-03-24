# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import component

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_017_test_input.vhd"))


class test_component_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_017_with_combined_generic(self):
        oRule = component.rule_017()
        oRule.separate_generic_port_alignment = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "component")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [11, 12, 13, 20, 21, 22, 26, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_with_combined_generic(self):
        oRule = component.rule_017()
        oRule.separate_generic_port_alignment = False

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_017_test_input.fixed_combined_generic.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_017_with_seperate_generic(self):
        oRule = component.rule_017()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "component")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [20, 21, 22, 25, 26, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_with_seperate_generic(self):
        oRule = component.rule_017()

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_017_test_input.fixed_seperate_generic.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

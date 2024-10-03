# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import instantiation

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_005_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_005__aiu_anl__agma_anl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "add_new_line"
        oRule.after_generic_map_aspect = "add_new_line"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "instantiation")
        self.assertEqual(oRule.identifier, "005")

        lExpected = [62, 73, 79, 85, 91, 97, 103]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_005__aiu_anl__agma_anl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "add_new_line"
        oRule.after_generic_map_aspect = "add_new_line"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_005_test_input.fixed__aiu_anl__agma_anl.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_005__aiu_anl__agma_rnl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "add_new_line"
        oRule.after_generic_map_aspect = "remove_new_line"

        lExpected = [14, 79, 85, 91, 97, 103, 172]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_005__aiu_anl__agma_rnl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "add_new_line"
        oRule.after_generic_map_aspect = "remove_new_line"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_005_test_input.fixed__aiu_anl__agma_rnl.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_005__aiu_rnl__agma_anl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "remove_new_line"
        oRule.after_generic_map_aspect = "add_new_line"

        lExpected = [21, 28, 35, 42, 49, 62, 73, 179, 186, 193, 200, 207]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_005__aiu_rnl__agma_anl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "remove_new_line"
        oRule.after_generic_map_aspect = "add_new_line"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_005_test_input.fixed__aiu_rnl__agma_anl.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_005__aiu_rnl__agma_rnl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "remove_new_line"
        oRule.after_generic_map_aspect = "remove_new_line"

        lExpected = [14, 21, 28, 35, 42, 49, 172, 179, 186, 193, 200, 207]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_005__aiu_rnl__agma_rnl(self):
        oRule = instantiation.rule_005()
        oRule.after_instantiated_unit = "remove_new_line"
        oRule.after_generic_map_aspect = "remove_new_line"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_005_test_input.fixed__aiu_rnl__agma_rnl.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

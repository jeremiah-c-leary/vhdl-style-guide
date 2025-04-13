# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import entity

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_017_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    ###############################################################################
    def test_rule_017_yes_yes_yes_no(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.separate_generic_port_alignment = "no"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [5, 6, 7, 10, 11, 13, 16, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_017_true_true_true_false(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.separate_generic_port_alignment = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [5, 6, 7, 10, 11, 13, 16, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_yes_yes_yes_no(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.separate_generic_port_alignment = False

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_017_test_input.fixed_yes_yes_yes_no.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_017_yes_yes_no_yes(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.separate_generic_port_alignment = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [5, 6, 7, 9, 10, 11, 13, 16, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_017_true_true_false_true(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = False
        oRule.separate_generic_port_alignment = True

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [5, 6, 7, 9, 10, 11, 13, 16, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_yes_yes_no_yes(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "no"
        oRule.separate_generic_port_alignment = "yes"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_017_test_input.fixed_yes_yes_no_yes.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_017_yes_no_yes_yes(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"
        oRule.separate_generic_port_alignment = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [4, 5, 6, 7, 10, 11, 13, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_017_true_false_true_true(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = True
        oRule.separate_generic_port_alignment = True

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [4, 5, 6, 7, 10, 11, 13, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_yes_no_yes_yes(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = "yes"
        oRule.blank_line_ends_group = "no"
        oRule.comment_line_ends_group = "yes"
        oRule.separate_generic_port_alignment = "yes"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_017_test_input.fixed_yes_no_yes_yes.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    ###############################################################################
    def test_rule_017_no_yes_yes_yes(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.separate_generic_port_alignment = "yes"

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [4, 5, 7, 9, 11, 16, 17, 18, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_017_false_true_true_true(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.separate_generic_port_alignment = True

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "entity")
        self.assertEqual(oRule.identifier, "017")

        lExpected = [4, 5, 7, 9, 11, 16, 17, 18, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_017_no_yes_yes_yes(self):
        oRule = entity.rule_017()
        oRule.compact_alignment = "no"
        oRule.blank_line_ends_group = "yes"
        oRule.comment_line_ends_group = "yes"
        oRule.separate_generic_port_alignment = "yes"

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_017_test_input.fixed_no_yes_yes_yes.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

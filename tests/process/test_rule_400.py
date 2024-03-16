# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import process
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_400_test_input.vhd'))


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400_yes_yes_yes_yes_yes_yes(self):
        oRule = process.rule_400()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'yes'
        oRule.comment_line_ends_group = 'yes'
        oRule.if_control_statements_ends_group = 'yes'
        oRule.case_control_statements_ends_group = 'yes'
        oRule.loop_control_statements_ends_group = 'yes'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '400')

        lExpected = [27, 28, 30, 31, 39, 43, 46, 49, 55, 58, 61, 66, 78, 79, 80, 81]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_400_true_true_true_true_true_true(self):
        oRule = process.rule_400()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = True
        oRule.if_control_statements_ends_group = True
        oRule.case_control_statements_ends_group = True
        oRule.loop_control_statements_ends_group = True

        lExpected = [27, 28, 30, 31, 39, 43, 46, 49, 55, 58, 61, 66, 78, 79, 80, 81]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_yes_yes_yes_yes_yes_yes(self):
        oRule = process.rule_400()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'yes'
        oRule.comment_line_ends_group = 'yes'
        oRule.if_control_statements_ends_group = 'yes'
        oRule.case_control_statements_ends_group = 'yes'
        oRule.loop_control_statements_ends_group = 'yes'

        oRule.fix(self.oFile)

        lExpected_all = []
        lExpected_all.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed_yes_yes_yes_yes_yes_yes.vhd'), lExpected_all, False)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

###############################################################################
    def test_rule_400_no_no_no_no_no_no(self):
        oRule = process.rule_400()
        oRule.compact_alignment = 'no'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'no'
        oRule.if_control_statements_ends_group = 'no'
        oRule.case_control_statements_ends_group = 'no'
        oRule.loop_control_statements_ends_group = 'no'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'process')
        self.assertEqual(oRule.identifier, '400')

        lExpected = [24, 25, 27, 28, 31, 39, 40, 43, 44, 46, 47, 49, 50, 55, 56, 58, 59, 61, 66, 78, 79, 80]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_400_false_false_false_false_false_false(self):
        oRule = process.rule_400()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        oRule.if_control_statements_ends_group = False
        oRule.case_control_statements_ends_group = False
        oRule.loop_control_statements_ends_group = False

        lExpected = [24, 25, 27, 28, 31, 39, 40, 43, 44, 46, 47, 49, 50, 55, 56, 58, 59, 61, 66, 78, 79, 80]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_no_no_no_no_no_no(self):
        oRule = process.rule_400()
        oRule.compact_alignment = 'no'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'no'
        oRule.if_control_statements_ends_group = 'no'
        oRule.case_control_statements_ends_group = 'no'
        oRule.loop_control_statements_ends_group = 'no'

        oRule.fix(self.oFile)

        lExpected_all = []
        lExpected_all.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed_no_no_no_no_no_no.vhd'), lExpected_all, False)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

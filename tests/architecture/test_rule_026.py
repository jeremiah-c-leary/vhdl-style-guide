# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from tests import utils
from vsg import token

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_026_test_input.vhd'))


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_026_yes_no_no_no(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'no'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '026')

        lExpected = [5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_026_true_false_false_false(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        oRule.include_type_is_keyword = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '026')

        lExpected = [5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_yes_no_no_no(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'no'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_yes_no_no_no.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

###############################################################################
    def test_rule_026_no_no_no_no(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'no'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'no'

        lExpected = [4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 19, 20, 22, 23, 24, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_026_false_false_false_false(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        oRule.include_type_is_keyword = False

        lExpected = [4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 19, 20, 22, 23, 24, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_false_false_false_false(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'no'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_no_no_no_no.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

###############################################################################
    def test_rule_026_yes_no_yes_no(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'yes'
        oRule.include_type_is_keyword = 'no'

        lExpected = [4, 5, 7, 8, 9, 12, 13, 14, 15, 17, 18, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_026_true_false_true_false(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = True
        oRule.include_type_is_keyword = False

        lExpected = [4, 5, 7, 8, 9, 12, 13, 14, 15, 17, 18, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_yes_no_yes_no(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'no'
        oRule.comment_line_ends_group = 'yes'
        oRule.include_type_is_keyword = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_yes_no_yes_no.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

###############################################################################
    def test_rule_026_yes_yes_no_no(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'yes'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'no'

        lExpected = [4, 5, 6, 7, 8, 9, 12, 13, 15, 17, 18, 19, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_026_true_true_false_false(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = False
        oRule.include_type_is_keyword = False

        lExpected = [4, 5, 6, 7, 8, 9, 12, 13, 15, 17, 18, 19, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_yes_yes_no_no(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'yes'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_yes_yes_no_no.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

##############################################################################
    def test_rule_026_yes_yes_no_yes(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'yes'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'yes'

        lExpected = [4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 17, 18, 19, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_026_true_true_false_true(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = True
        oRule.blank_line_ends_group = True
        oRule.comment_line_ends_group = False
        oRule.include_type_is_keyword = True

        lExpected = [4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 17, 18, 19, 20, 22, 23, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
        oRule.lTokens = []

    def test_fix_rule_026_yes_yes_no_yes(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = 'yes'
        oRule.blank_line_ends_group = 'yes'
        oRule.comment_line_ends_group = 'no'
        oRule.include_type_is_keyword = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_yes_yes_no_yes.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


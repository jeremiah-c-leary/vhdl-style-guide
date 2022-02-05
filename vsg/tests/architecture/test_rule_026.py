
import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_026_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_allowing_comments_and_blank_lines.vhd'), lExpected)


class test_architecture_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_026_allowing_comments_and_blank_lines(self):
        oRule = architecture.rule_026()
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'architecture')
        self.assertEqual(oRule.identifier, '026')

        lExpected = [5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_allowing_comments_and_blank_lines(self):
        oRule = architecture.rule_026()
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_026_allowing_comments_and_blank_lines_without_condensed(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False

        lExpected = [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 18, 19, 21, 22, 23, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_allowing_comments_and_blank_lines_without_condensed(self):
        oRule = architecture.rule_026()
        oRule.compact_alignment = False
        oRule.blank_line_ends_group = False
        oRule.comment_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_allowing_comments_and_blank_lines_without_condensed.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_026_allowing_blank_lines(self):
        oRule = architecture.rule_026()
        oRule.blank_line_ends_group = False

        lExpected = [4, 5, 7, 8, 9, 11, 12, 13, 14, 16, 17, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_allowing_blank_lines(self):
        oRule = architecture.rule_026()
        oRule.blank_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_allowing_blank_lines.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_026_allowing_comments(self):
        oRule = architecture.rule_026()
        oRule.comment_line_ends_group = False

        lExpected = [4, 5, 6, 7, 8, 9, 11, 12, 14, 16, 17, 18, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026_allowing_comments(self):
        oRule = architecture.rule_026()
        oRule.comment_line_ends_group = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed_allowing_comments.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_026(self):
        oRule = architecture.rule_026()

        lExpected = [4, 5, 7, 8, 9, 11, 12, 14, 16, 17, 19, 21, 22, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_026(self):
        oRule = architecture.rule_026()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_026_test_input.fixed.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

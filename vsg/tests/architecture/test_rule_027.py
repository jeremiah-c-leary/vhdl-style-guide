
import os
import unittest

from vsg.rules import architecture
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_027_test_input.vhd'))

#lExpected = []
#lExpected.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_027_test_input.fixed_allowing_comments_and_blank_lines.vhd'), lExpected)


class test_architecture_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

#    def test_rule_027_allowing_comments_and_blank_lines(self):
#        oRule = architecture.rule_027()
#        oRule.blank_line_ends_group = False
#        oRule.comment_line_ends_group = False
#        self.assertTrue(oRule)
#        self.assertEqual(oRule.name, 'architecture')
#        self.assertEqual(oRule.identifier, '027')
#
#        lExpected = [5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 22]
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
#
#    def test_fix_rule_027_allowing_comments_and_blank_lines(self):
#        oRule = architecture.rule_027()
#        oRule.blank_line_ends_group = False
#        oRule.comment_line_ends_group = False
#
#        oRule.fix(self.oFile)
#
#        lActual = self.oFile.get_lines()
#
#        self.assertEqual(lExpected, lActual)
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, [])
#
#    def test_rule_027_allowing_comments_and_blank_lines_without_condensed(self):
#        oRule = architecture.rule_027()
#        oRule.compact_alignment = False
#        oRule.blank_line_ends_group = False
#        oRule.comment_line_ends_group = False
#
#        lExpected = [4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 17, 19, 20, 21, 22]
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
#
#    def test_fix_rule_027_allowing_comments_and_blank_lines_without_condensed(self):
#        oRule = architecture.rule_027()
#        oRule.compact_alignment = False
#        oRule.blank_line_ends_group = False
#        oRule.comment_line_ends_group = False
#
#        oRule.fix(self.oFile)
#
#        lActual = self.oFile.get_lines()
#
#        lExpected = []
#        lExpected.append('')
#        utils.read_file(os.path.join(sTestDir, 'rule_027_test_input.fixed_allowing_comments_and_blank_lines_without_condensed.vhd'), lExpected)
#
#        self.assertEqual(lExpected, lActual)
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, [])
#
#    def test_rule_027_allowing_blank_lines(self):
#        oRule = architecture.rule_027()
#        oRule.blank_line_ends_group = False
#
#        lExpected = [4, 5, 7, 9, 10, 11, 12, 14, 15, 17, 19, 20, 22]
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
#
#    def test_fix_rule_027_allowing_blank_lines(self):
#        oRule = architecture.rule_027()
#        oRule.blank_line_ends_group = False
#
#        oRule.fix(self.oFile)
#
#        lActual = self.oFile.get_lines()
#
#        lExpected = []
#        lExpected.append('')
#        utils.read_file(os.path.join(sTestDir, 'rule_027_test_input.fixed_allowing_blank_lines.vhd'), lExpected)
#
#        self.assertEqual(lExpected, lActual)
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, [])
#
#    def test_rule_027_allowing_comments(self):
#        oRule = architecture.rule_027()
#        oRule.comment_line_ends_group = False
#
#        lExpected = [4, 5, 6, 7, 9, 10, 12, 14, 15, 16, 17, 19, 20, 22]
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
#
#    def test_fix_rule_027_allowing_comments(self):
#        oRule = architecture.rule_027()
#        oRule.comment_line_ends_group = False
#
#        oRule.fix(self.oFile)
#
#        lActual = self.oFile.get_lines()
#
#        lExpected = []
#        lExpected.append('')
#        utils.read_file(os.path.join(sTestDir, 'rule_027_test_input.fixed_allowing_comments.vhd'), lExpected)
#
#        self.assertEqual(lExpected, lActual)
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(oRule.violations, [])
#
    def test_rule_027(self):
        oRule = architecture.rule_027()

        lExpected = []
        lExpected.extend(range(4, 8))
        lExpected.extend(range(10, 12))
        lExpected.extend(range(13, 15))
        lExpected.extend(range(16, 18))
        lExpected.extend(range(19, 21))
        lExpected.extend(range(22, 24))
        lExpected.extend(range(25, 27))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_027(self):
        oRule = architecture.rule_027()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_027_test_input.fixed.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

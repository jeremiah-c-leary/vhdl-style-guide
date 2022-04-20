
import os
import unittest

from vsg.rules import block_comment
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

dIndentMap = utils.read_indent_file()

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input.vhd'))


class test_block_comment_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_003_default(self):
        oRule = block_comment.rule_003()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'block_comment')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [8, 12, 16, 20, 24, 30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_default_wo_allow_indenting(self):
        oRule = block_comment.rule_003()
        oRule.allow_indenting = False

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'block_comment')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [8, 12, 16, 20, 24, 30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_plus(self):
        oRule = block_comment.rule_003()
        oRule.footer_left = '+'
        oRule.max_footer_column = 80

        lExpected = [4, 12, 16, 20, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_bar(self):
        oRule = block_comment.rule_003()
        oRule.footer_left = '|'
        oRule.max_footer_column = 80

        lExpected = [4, 8, 16, 20, 24, 30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_bar_w_footer_string_centered(self):
        oRule = block_comment.rule_003()
        oRule.footer_left = '|'
        oRule.max_footer_column = 80
        oRule.footer_string = '[ abcdef ]'
        oRule.footer_right_repeat = '='
        oRule.footer_alignment = 'center'

        lExpected = [4, 8, 12, 20, 24, 30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_bar_w_footer_string_left_justified(self):
        oRule = block_comment.rule_003()
        oRule.footer_left = '|'
        oRule.max_footer_column = 80
        oRule.footer_string = '[ abcdef ]'
        oRule.footer_right_repeat = '='
        oRule.footer_alignment = 'left'

        lExpected = [4, 8, 12, 16, 24, 30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_bar_w_footer_string_right_justified(self):
        oRule = block_comment.rule_003()
        oRule.footer_left = '|'
        oRule.max_footer_column = 80
        oRule.footer_string = '[ abcdef ]'
        oRule.footer_right_repeat = '='
        oRule.footer_alignment = 'right'

        lExpected = [4, 8, 12, 16, 20, 30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))


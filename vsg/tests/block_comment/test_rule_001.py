
import os
import unittest

from vsg.rules import block_comment
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

dIndentMap = utils.read_indent_file()

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))

lFile_align_left, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.align_left.vhd'))


class test_block_comment_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_001_default(self):
        oRule = block_comment.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'block_comment')
        self.assertEqual(oRule.identifier, '001')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [6, 14, 18, 22, 27, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_default_do_not_allow_indenting(self):
        oRule = block_comment.rule_001()
        oRule.allow_indenting = False

        lExpected = [6, 14, 18, 22, 27, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_plus(self):
        oRule = block_comment.rule_001()
        oRule.header_left = '+'
        oRule.max_header_column = 80

        lExpected = [2, 14, 18, 22, 27, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_plus_w_header_string_centered(self):
        oRule = block_comment.rule_001()
        oRule.header_left = '+'
        oRule.max_header_column = 80
        oRule.header_string = '[ abcdef ]'
        oRule.header_right_repeat = '='
        oRule.header_alignment = 'center'

        lExpected = [2, 6, 18, 22, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_plus_w_header_string_left_justified(self):
        oRule = block_comment.rule_001()
        oRule.header_left = '+'
        oRule.max_header_column = 80
        oRule.header_string = '[ abcdef ]'
        oRule.header_right_repeat = '='
        oRule.header_alignment = 'left'

        lExpected = [2, 6, 14, 22, 27, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_plus_w_header_string_right_justified(self):
        oRule = block_comment.rule_001()
        oRule.header_left = '+'
        oRule.max_header_column = 80
        oRule.header_string = '[ abcdef ]'
        oRule.header_right_repeat = '='
        oRule.header_alignment = 'right'

        lExpected = [2, 6, 14, 18, 27, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_default_w_header(self):
        oRule = block_comment.rule_001()
        oRule.header_left_repeat = '-'
        oRule.header_string = '<-    80 chars    ->'
        oRule.header_right_repeat = '-'
        oRule.header_alignment = 'center'
        oRule.max_header_column = 80

        lExpected = [2, 6, 14, 18, 22, 27]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_001_align_left(self):
        self.oFile = vhdlFile.vhdlFile(lFile_align_left)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

        oRule = block_comment.rule_001()

        oRule.header_left_repeat = '-'
        oRule.header_string = '<-    80 chars    ->'
        oRule.header_right_repeat = '-'
        oRule.header_alignment = 'center'
        oRule.max_header_column = 80
        oRule.allow_indenting = False

        lExpected = []

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))


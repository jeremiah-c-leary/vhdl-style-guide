# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils

from vsg import exceptions, vhdlFile
from vsg.rules import block_comment

sTestDir = os.path.dirname(__file__)

dIndentMap = utils.read_indent_file()

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "multistyle_test_input.vhd"))
lFixedFile, eFixedError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "multistyle_test_input.fixed.vhd"))


class test_multistyle(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.oFixedFile = vhdlFile.vhdlFile(lFixedFile)

        self.assertIsNone(eError)
        self.assertIsNone(eFixedError)

        self.oFile.set_indent_map(dIndentMap)
        self.oFixedFile.set_indent_map(dIndentMap)

    def configure_multistyle(self, oRule, lHeaderColumns, lFooterColumns):
        oRule.header_left = ["|", "|", "!"]
        oRule.header_left_repeat = ["-", "=", "-"]
        oRule.header_string = ["", "", ""]
        oRule.header_right_repeat = ["-", "=", "-"]
        oRule.header_alignment = ["center", "center", "center"]
        oRule.max_header_column = lHeaderColumns

        oRule.comment_left = ["|", "|", "!"]

        oRule.footer_left = ["|", "|", "!"]
        oRule.footer_left_repeat = ["-", "=", "-"]
        oRule.footer_string = ["", "", ""]
        oRule.footer_right_repeat = ["-", "=", "-"]
        oRule.footer_alignment = ["center", "center", "center"]
        oRule.max_footer_column = lFooterColumns

        oRule._block_comment_style_count = oRule._validate_and_get_style_count()

    def test_rule_001_accepts_multiple_styles(self):
        oRule = block_comment.rule_001()
        self.configure_multistyle(oRule, [79, 84, 79], [79, 84, 79])

        oRule.analyze(self.oFile)

        self.assertEqual([], utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_002_uses_one_consistent_style_for_the_whole_block(self):
        oRule = block_comment.rule_002()
        self.configure_multistyle(oRule, [79, 84, 79], [79, 84, 79])

        oRule.analyze(self.oFile)

        self.assertEqual([19], utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_003_accepts_multiple_styles(self):
        oRule = block_comment.rule_003()
        self.configure_multistyle(oRule, [79, 84, 79], [79, 84, 79])

        oRule.analyze(self.oFile)

        self.assertEqual([], utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_style_count_mismatch_raises_configuration_error(self):
        oRule = block_comment.rule_001()

        oRule.header_left = ["|", "|"]
        oRule.header_left_repeat = ["-", "="]
        oRule.header_string = ["", ""]
        oRule.header_right_repeat = ["-", "="]

        oRule.comment_left = ["|", "|", "!"]

        oRule.footer_left = ["|", "|"]
        oRule.footer_left_repeat = ["-", "="]
        oRule.footer_string = ["", ""]
        oRule.footer_right_repeat = ["-", "="]

        with self.assertRaises(exceptions.ConfigurationError):
            oRule._validate_and_get_style_count()

    def test_rule_001_autofixes_separator_only_headers(self):
        oRule = block_comment.rule_001()
        self.configure_multistyle(oRule, [80, 85, 80], [80, 85, 80])

        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual([], utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual(self.oFixedFile.get_lines(), self.oFile.get_lines())

    def test_rule_003_autofixes_separator_only_footers(self):
        oRule = block_comment.rule_003()
        self.configure_multistyle(oRule, [80, 85, 80], [80, 85, 80])

        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual([], utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual(self.oFixedFile.get_lines(), self.oFile.get_lines())

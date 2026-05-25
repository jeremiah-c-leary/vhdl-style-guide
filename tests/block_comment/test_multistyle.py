# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import exceptions, rule_list, severity, vhdlFile
from vsg.rules import block_comment

sTestDir = os.path.dirname(__file__)

dIndentMap = utils.read_indent_file()

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "multistyle_test_input.vhd"))
lHeadersFixedFile, eHeadersFixedError = vhdlFile.utils.read_vhdlfile(
    os.path.join(sTestDir, "multistyle_test_input.headers.fixed.vhd"),
)
lFootersFixedFile, eFootersFixedError = vhdlFile.utils.read_vhdlfile(
    os.path.join(sTestDir, "multistyle_test_input.footers.fixed.vhd"),
)


class test_multistyle(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.oHeadersFixedFile = vhdlFile.vhdlFile(lHeadersFixedFile)
        self.oFootersFixedFile = vhdlFile.vhdlFile(lFootersFixedFile)

        self.assertIsNone(eError)
        self.assertIsNone(eHeadersFixedError)
        self.assertIsNone(eFootersFixedError)

        self.oFile.set_indent_map(dIndentMap)
        self.oHeadersFixedFile.set_indent_map(dIndentMap)
        self.oFootersFixedFile.set_indent_map(dIndentMap)

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
        self.assertEqual(self.oHeadersFixedFile.get_lines(), self.oFile.get_lines())

    def test_rule_003_autofixes_separator_only_footers(self):
        oRule = block_comment.rule_003()
        self.configure_multistyle(oRule, [80, 85, 80], [80, 85, 80])

        oRule.fix(self.oFile)
        oRule.analyze(self.oFile)

        self.assertEqual([], utils.extract_violation_lines_from_violation_object(oRule.violations))
        self.assertEqual(self.oFootersFixedFile.get_lines(), self.oFile.get_lines())

    def test_multi_style_configuration_via_yaml(self):
        # Drive the same multi-style configuration through the YAML loading
        # path a user actually exercises: tests.utils.read_configuration ->
        # rule_list.configure -> block_rule._synchronize_block_comment_style_attributes.
        oConfig = utils.read_configuration(os.path.join(sTestDir, "multistyle_config.yaml"))
        oRuleList = rule_list.rule_list(self.oFile, severity.create_list({}))
        oRuleList.configure(oConfig)

        dRuleByName = {oRule.unique_id: oRule for oRule in oRuleList.rules}
        oRule001 = dRuleByName["block_comment_001"]
        oRule002 = dRuleByName["block_comment_002"]
        oRule003 = dRuleByName["block_comment_003"]

        # The YAML lists must reach the rule attributes as Python lists, not strings.
        self.assertEqual(["|", "|", "!"], oRule001.header_left)
        self.assertEqual([79, 84, 79], oRule001.max_header_column)
        self.assertEqual(["|", "|", "!"], oRule002.comment_left)
        self.assertEqual(["|", "|", "!"], oRule003.footer_left)
        self.assertEqual([79, 84, 79], oRule003.max_footer_column)

        # Each rule must see all three style families synchronized so it can
        # pick a coherent style per block.
        self.assertEqual(3, oRule001.get_style_count())
        self.assertEqual(3, oRule002.get_style_count())
        self.assertEqual(3, oRule003.get_style_count())
        # Cross-pollination: rule_001 must know rule_002's comment_left and
        # rule_003's footer_*, otherwise matching_style_indexes can't work.
        self.assertEqual(["|", "|", "!"], oRule001.comment_left)
        self.assertEqual(["|", "|", "!"], oRule001.footer_left)

        # End-to-end: with the input matching widths [79, 84, 79], the only
        # remaining violation must be the mixed-body line.
        oRuleList.check_rules()
        lViolations = []
        for sRuleName in ("block_comment_001", "block_comment_002", "block_comment_003"):
            for oViolation in dRuleByName[sRuleName].violations:
                lViolations.append((sRuleName, oViolation.get_line_number()))
        self.assertEqual([("block_comment_002", 19)], lViolations)

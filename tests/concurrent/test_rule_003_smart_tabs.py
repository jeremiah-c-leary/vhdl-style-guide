# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_003_test_input_smart_tabs.vhd'))

dIndentMap = utils.read_indent_file()

lExpected_align_left_no_align_paren_yes = []
lExpected_align_left_no_align_paren_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_align_left_no_align_paren_yes__smart_tabs.vhd'), lExpected_align_left_no_align_paren_yes)

lExpected_align_left_yes_align_paren_no = []
lExpected_align_left_yes_align_paren_no.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_align_left_yes_align_paren_no__smart_tabs.vhd'), lExpected_align_left_yes_align_paren_no)

lExpected_align_left_yes_align_paren_yes = []
lExpected_align_left_yes_align_paren_yes.append('')
utils.read_file(os.path.join(sTestDir, 'rule_003_test_input.fixed_align_left_yes_align_paren_yes__smart_tabs.vhd'), lExpected_align_left_yes_align_paren_yes)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_003_align_left_no_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.indent_style = 'smart_tabs'
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '003')

        lExpected = [11, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_align_left_no_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.indent_style = 'smart_tabs'
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_no_align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_align_left_yes_align_paren_no(self):
        oRule = concurrent.rule_003()
        oRule.indent_style = 'smart_tabs'
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'

        lExpected = [11, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_align_left_yes_align_paren_no(self):
        oRule = concurrent.rule_003()
        oRule.indent_style = 'smart_tabs'
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_no, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_003_align_left_yes_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.indent_style = 'smart_tabs'
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'

        lExpected = [11, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_003_align_left_yes_align_paren_yes(self):
        oRule = concurrent.rule_003()
        oRule.indent_style = 'smart_tabs'
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_yes_align_paren_yes, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

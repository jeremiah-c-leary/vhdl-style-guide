# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import assert_statement

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))

dIndentMap = utils.read_indent_file()

dIndentMap = utils.read_indent_file()

lExpected_spaces = []
lExpected_spaces.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_spaces.vhd'), lExpected_spaces)

lExpected_smart_tabs = []
lExpected_smart_tabs.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_smart_tabs.vhd'), lExpected_smart_tabs)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_001_spaces(self):
        oRule = assert_statement.rule_001()
        oRule.indent_style = 'spaces'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'assert')
        self.assertEqual(oRule.identifier, '001')
        self.assertEqual(oRule.groups, ['indent'])

        lExpected = [32, 35, 38, 41, 42, 44, 47, 50, 53, 54]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_spaces(self):
        oRule = assert_statement.rule_001()
        oRule.indent_style = 'spaces'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_001_smart_tabs(self):
        oRule = assert_statement.rule_001()
        oRule.indent_style = 'smart_tabs'
        self.assertTrue(oRule)

        lExpected = [7, 9, 10, 12, 13, 15, 16, 17, 19, 21, 22, 24, 25, 27, 28, 29, 32, 34, 35, 37, 38, 40, 41, 42, 44, 46, 47, 49, 50, 52, 53, 54]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_smart_tabs(self):
        oRule = assert_statement.rule_001()
        oRule.indent_style = 'smart_tabs'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_smart_tabs, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

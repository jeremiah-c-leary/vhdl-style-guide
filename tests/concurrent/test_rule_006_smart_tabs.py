# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import concurrent

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_006_test_input_smart_tabs.vhd"))

lExpected_indent_2 = []
lExpected_indent_2.append("")
utils.read_file(os.path.join(sTestDir, "rule_006_test_input_smart_tabs.fixed_indent_2.vhd"), lExpected_indent_2)

lExpected_indent_4 = []
lExpected_indent_4.append("")
utils.read_file(os.path.join(sTestDir, "rule_006_test_input_smart_tabs.fixed_indent_4.vhd"), lExpected_indent_4)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_fix_rule_006_indent_2(self):
        oRule = concurrent.rule_006()
        oRule.indent_size = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_indent_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_006_indent_4(self):
        oRule = concurrent.rule_006()
        oRule.indent_size = 4

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_indent_4, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

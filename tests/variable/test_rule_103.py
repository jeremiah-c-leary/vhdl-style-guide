# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import variable

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_103_test_input.vhd"))

dIndentMap = utils.read_indent_file()



class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_103(self):
        oRule = variable.rule_103()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable")
        self.assertEqual(oRule.identifier, "103")

        lExpected = [5, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_103(self):
        oRule = variable.rule_103()

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_103_test_input.fixed.vhd"), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

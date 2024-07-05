# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import pragma

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_401_test_input.vhd"))

dIndentMap = utils.read_indent_file()


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_default(self):
        oRule = pragma.rule_401()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "pragma")
        self.assertEqual(oRule.identifier, "401")

        lExpected = [10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_default(self):
        oRule = pragma.rule_401()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append("")
        utils.read_file(os.path.join(sTestDir, "rule_401_test_input.fixed_default.vhd"), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

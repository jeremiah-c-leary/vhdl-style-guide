# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import block

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_004_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_004_test_input.fixed.vhd"), lExpected, False)


class test_block_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_004(self):
        oRule = block.rule_004()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "block")
        self.assertEqual(oRule.identifier, "004")

        lExpected = [9]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_004(self):
        oRule = block.rule_004()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

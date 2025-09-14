# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import signal

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_403_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_403_test_input.fixed.vhd"), lExpected)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_403(self):
        oRule = signal.rule_403()
        oRule.ignore_single_line = "no"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "signal")
        self.assertEqual(oRule.identifier, "403")
        self.assertEqual(oRule.groups, ["structure"])

        lExpected = [9, 20, 20, 20, 20, 20, 20, 20, 20]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_403(self):
        oRule = signal.rule_403()
        oRule.ignore_single_line = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

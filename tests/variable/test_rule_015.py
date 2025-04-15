# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import variable

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_015_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_015_test_input.fixed.vhd"), lExpected)


class test_variable_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_015(self):
        oRule = variable.rule_015()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "variable")
        self.assertEqual(oRule.identifier, "015")
        self.assertEqual(oRule.groups, ["structure"])

        lExpected = [7, 9, 76, 78, 79, 81]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_015(self):
        oRule = variable.rule_015()
        self.maxDiff = None

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

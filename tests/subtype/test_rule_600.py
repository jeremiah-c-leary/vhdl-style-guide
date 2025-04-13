# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import subtype

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_600_test_input.vhd"))


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_600(self):
        oRule = subtype.rule_600()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "subtype")
        self.assertEqual(oRule.identifier, "600")
        self.assertEqual(oRule.groups, ["naming"])

        lExpected = [7, 8, 10, 11, 13, 14, 16, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_600_capitalized(self):
        oRule = subtype.rule_600()
        oRule.suffixes = ["_ST"]
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "subtype")
        self.assertEqual(oRule.identifier, "600")

        lExpected = [7, 8, 10, 11, 13, 14, 16, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_004_w_single_regexp(self):
        oRule = subtype.rule_600()
        oRule.exceptions = ["major_.*"]

        lExpected = [7, 8, 10, 11, 16, 17]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_004_w_two_regexp(self):
        oRule = subtype.rule_600()
        oRule.exceptions = ["major_.*", "minor_.*"]

        lExpected = [7, 8, 10, 11]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

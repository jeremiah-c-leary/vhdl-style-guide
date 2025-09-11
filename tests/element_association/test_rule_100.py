# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import element_association

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_100_test_input.vhd"))

lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_100_test_input.fixed.vhd"), lExpected)

lExpected_spaces_gte2 = []
lExpected_spaces_gte2.append("")
utils.read_file(os.path.join(sTestDir, "rule_100_test_input.fixed_spaces_gte2.vhd"), lExpected_spaces_gte2)


class test_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_100(self):
        oRule = element_association.rule_100()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "element_association")
        self.assertEqual(oRule.identifier, "100")

        lExpected = [21, 21, 25, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_100(self):
        oRule = element_association.rule_100()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_100_spaces_2_plus(self):
        oRule = element_association.rule_100()
        oRule.number_of_spaces = "2+"

        lExpected = [6, 6, 10, 10, 21, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_100_spaces_2_plus(self):
        oRule = element_association.rule_100()
        oRule.number_of_spaces = "2+"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_spaces_gte2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import reserved

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_001_test_input.vhd"))


class test_reserved_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_all_standards(self):
        oRule = reserved.rule_001()
        oRule.standard = "all"
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "reserved")
        self.assertEqual(oRule.identifier, "001")
        self.assertFalse(oRule.fixable)

        lExpected = [7, 9, 10, 11, 14, 15, 19, 21, 21, 23, 24, 25, 30, 30, 32, 38, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_1987_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "1987"

        lExpected = [7, 11, 19, 21, 21, 25, 30, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_1993_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "1987"

        lExpected = [7, 11, 19, 21, 21, 25, 30, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_2000_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "2000"

        lExpected = [7, 11, 19, 21, 21, 24, 25, 30, 32, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_2002_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "2002"

        lExpected = [7, 11, 19, 21, 21, 24, 25, 30, 32, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_2008_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "2008"

        lExpected = [7, 10, 11, 15, 19, 21, 21, 25, 30, 30, 38, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_2019_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "2019"

        lExpected = [7, 9, 10, 11, 14, 15, 19, 21, 21, 23, 25, 30, 30, 38, 44]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

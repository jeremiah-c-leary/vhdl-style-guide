# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import reserved

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_001_test_input.vhd"))


class test_rule(unittest.TestCase):
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

        lExpected = [7, 9, 10, 14, 18, 20, 20, 22, 23, 28, 28, 30, 36, 42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_1987_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "1987"

        lExpected = [7, 10, 18, 20, 20, 23, 28, 42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_1993_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "1987"

        lExpected = [7, 10, 18, 20, 20, 23, 28, 42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_2000_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "2000"

        lExpected = [7, 10, 18, 20, 20, 22, 23, 28, 30, 42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_2002_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "2002"

        lExpected = [7, 10, 18, 20, 20, 22, 23, 28, 30, 42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_2008_standard(self):
        oRule = reserved.rule_001()
        oRule.standard = "2008"

        lExpected = [7, 9, 10, 14, 18, 20, 20, 23, 28, 28, 36, 42]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

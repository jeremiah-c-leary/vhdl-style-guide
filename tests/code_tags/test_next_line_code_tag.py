# -*- coding: utf-8 -*-
import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import architecture, process

# Read in test file used for all tests

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__), "next_line_code_tag_test_input.vhd"))
oFile = vhdlFile.vhdlFile(lFile)


class testCodeTags(unittest.TestCase):
    def setUp(self):
        self.assertIsNone(eError)

    def test_rule_process_016(self):
        oRule = process.rule_016()

        lExpected = [13, 25]

        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_process_018(self):
        oRule = process.rule_018()

        lExpected = [15, 27]

        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_process_014(self):
        oRule = process.rule_014()

        lExpected = [19]

        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_architecture_024(self):
        oRule = architecture.rule_024()

        lExpected = []

        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_process_002(self):
        oRule = process.rule_002()

        lExpected = []

        oRule.analyze(oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

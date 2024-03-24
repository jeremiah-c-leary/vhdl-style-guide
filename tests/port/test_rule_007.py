# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import port
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_007_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_before_1_after_4.vhd'), lExpected)

lExpected_before_0_after_1 = []
lExpected_before_0_after_1.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_before_0_after_1.vhd'), lExpected_before_0_after_1)


class test_port_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_007(self):
        oRule = port.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'port')
        self.assertEqual(oRule.identifier, '007')

        lExpected = [14, 15, 16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007(self):
        oRule = port.rule_007()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_before_0_after_1(self):
        oRule = port.rule_007()
        oRule.spaces_before = 0
        oRule.spaces_after = 1

        lExpected = [4, 5, 6, 15, 16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007_before_0_after_1(self):
        oRule = port.rule_007()
        oRule.spaces_before = 0
        oRule.spaces_after = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_before_0_after_1, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import conditional_waveforms

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_001_test_input.vhd'))

lExpected_true = []
lExpected_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_true.vhd'), lExpected_true)

lExpected_false = []
lExpected_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_001_test_input.fixed_false.vhd'), lExpected_false)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_001_w_allow_single_line_false(self):
        oRule = conditional_waveforms.rule_001()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'conditional_waveforms')
        self.assertEqual(oRule.identifier, '001')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [8, 18, 18, 18, 20, 20, 21, 23, 24, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_w_allow_single_line_false(self):
        oRule = conditional_waveforms.rule_001()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_001_w_allow_single_line_true(self):
        oRule = conditional_waveforms.rule_001()
        oRule.allow_single_line = 'yes'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'conditional_waveforms')
        self.assertEqual(oRule.identifier, '001')

        lExpected = [18, 18, 18, 20, 20, 21, 23, 24, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_001_w_allow_single_line_true(self):
        oRule = conditional_waveforms.rule_001()
        oRule.allow_single_line = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

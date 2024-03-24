# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import conditional_waveforms
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_501_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_501_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_501_test_input.fixed_upper.vhd'), lExpected_upper)


class test_conditional_waveforms_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_501_lower(self):
        oRule = conditional_waveforms.rule_501()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'conditional_waveforms')
        self.assertEqual(oRule.identifier, '501')

        lExpected = [19]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_501_upper(self):
        oRule = conditional_waveforms.rule_501()
        oRule.case = 'upper'

        lExpected = [21]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_501_lower(self):
        oRule = conditional_waveforms.rule_501()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_501_upper(self):
        oRule = conditional_waveforms.rule_501()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


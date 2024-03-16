# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import ieee

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_500_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_500_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_500_test_input.fixed_upper.vhd'), lExpected_upper)

class test_port_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_500_lower(self):
        oRule = ieee.rule_500()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'ieee')
        self.assertEqual(oRule.identifier, '500')
        self.assertEqual(oRule.groups, ['case', 'case::keyword'])

        lExpected = [66, 67, 68, 69, 70]
        lExpected.extend([73, 74, 76, 77, 78,79])
        lExpected.extend(range(87, 89))
        lExpected.extend([91])
        lExpected.extend(range(93, 95))
        lExpected.extend(range(100, 105))
        lExpected.extend([107, 108, 110, 111, 112, 113])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_500_upper(self):
        oRule = ieee.rule_500()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'ieee')
        self.assertEqual(oRule.identifier, '500')

        lExpected = []
        lExpected.extend(range(5, 10))
        lExpected.extend([12, 13, 15, 16, 17, 18])
        lExpected.extend(range(26, 28))
        lExpected.extend([30])
        lExpected.extend(range(32, 34))
        lExpected.extend(range(39, 44))
        lExpected.extend([46, 47, 49, 50, 51, 52])

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_500_lower(self):
        oRule = ieee.rule_500()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_500_upper(self):
        oRule = ieee.rule_500()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


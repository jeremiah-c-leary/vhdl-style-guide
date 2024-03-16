# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import selected_assignment
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_107_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_107_test_input.fixed.vhd'), lExpected)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_107(self):
        oRule = selected_assignment.rule_107()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'selected_assignment')
        self.assertEqual(oRule.identifier, '107')

        lExpected = [38, 43, 48, 55, 65, 66, 67, 70, 71, 72, 75, 76, 77, 82, 83, 84]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_107(self):
        oRule = selected_assignment.rule_107()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

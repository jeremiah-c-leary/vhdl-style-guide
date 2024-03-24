# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import generic
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_014_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_014_test_input.fixed.vhd'), lExpected)


class test_generic_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_014(self):
        oRule = generic.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '014')

        lExpected = [13, 15]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_014(self):
        oRule = generic.rule_014()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

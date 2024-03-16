# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import generate
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_602_test_input.vhd'))


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule(self):
        oRule = generate.rule_602()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '602')
        self.assertEqual(oRule.groups, ['naming'])

        lExpected = [10, 13]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_w_uppercase(self):
        oRule = generate.rule_602()
        oRule.suffixes = ['_GV']
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generate')
        self.assertEqual(oRule.identifier, '602')

        lExpected = [10, 13]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_w_exception(self):
        oRule = generate.rule_602()
        oRule.exceptions.append('index')

        lExpected = [13]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))


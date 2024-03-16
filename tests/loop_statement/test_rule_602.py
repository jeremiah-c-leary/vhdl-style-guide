# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import loop_statement
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_602_test_input.vhd'))


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule(self):
        oRule = loop_statement.rule_602()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'loop_statement')
        self.assertEqual(oRule.identifier, '602')
        self.assertEqual(oRule.groups, ['naming'])

        lExpected = [13, 16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_w_uppercase(self):
        oRule = loop_statement.rule_602()
        oRule.suffixes = ['L_V']
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'loop_statement')
        self.assertEqual(oRule.identifier, '602')

        lExpected = [13, 16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_w_exception(self):
        oRule = loop_statement.rule_602()
        oRule.exceptions.append('index')

        lExpected = [16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))


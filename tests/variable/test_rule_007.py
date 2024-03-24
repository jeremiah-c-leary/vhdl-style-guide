# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import variable
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_007_test_input.vhd'))


class test_variable_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_007(self):
        oRule = variable.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable')
        self.assertEqual(oRule.identifier, '007')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [19, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

# -*- coding: utf-8 -*-

import os
import unittest

from vsg.rules import function
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_018_test_input.vhd'))


class test_function_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_018_add(self):
        oRule = function.rule_018()
        oRule.action = 'add'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '018')
        self.assertEqual(oRule.groups, ['structure', 'structure::optional'])

        lExpected = [26, 30]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_018_add(self):
        oRule = function.rule_018()
        oRule.action = 'add'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_018_test_input.fixed_add.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_018_remove(self):
        oRule = function.rule_018()
        oRule.action = 'remove'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '018')
        self.assertEqual(oRule.groups, ['structure', 'structure::optional'])

        lExpected = [18, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_018_remove(self):
        oRule = function.rule_018()
        oRule.action = 'remove'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_018_test_input.fixed_remove.vhd'), lExpected)

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

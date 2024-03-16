# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import entity

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_008_test_input.vhd'))


class test_entity_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_008_lower(self):
        oRule = entity.rule_008()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'entity')
        self.assertEqual(oRule.identifier, '008')

        lExpected = [6, 10, 14, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_008_lower(self):
        oRule = entity.rule_008()

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_008_test_input.fixed_lower.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_008_upper(self):
        oRule = entity.rule_008()
        oRule.case = 'upper'

        lExpected = [2, 10, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_008_upper(self):
        oRule = entity.rule_008()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_008_test_input.fixed_upper.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_008_camelCase(self):
        oRule = entity.rule_008()
        oRule.case = 'camelCase'

        lExpected = [6, 10, 14, 18, 22, 30, 34, 38, 42, 46, 54, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = 'camelCase'
        oRule.prefix_exceptions.append('e_')

        lExpected = [6, 10, 14, 18, 22, 34, 38, 46, 54, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = 'camelCase'
        oRule.suffix_exceptions.append('_a')

        lExpected = [6, 10, 14, 18, 22, 30, 34, 38, 42, 46, 54, 58, 62]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = 'camelCase'
        oRule.prefix_exceptions.append('e_')
        oRule.suffix_exceptions.append('_a')

        lExpected = [6, 10, 14, 18, 22, 30, 34, 38, 42, 46, 54, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_camelCase_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = 'camelCase'
        oRule.case_exceptions.append('e_MyFifo')

        lExpected = [6, 10, 14, 18, 22, 30, 38, 42, 46, 54, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase(self):
        oRule = entity.rule_008()
        oRule.case = 'PascalCase'

        lExpected = [2, 6, 14, 18, 26, 30, 34, 38, 42, 50, 54, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_prefix(self):
        oRule = entity.rule_008()
        oRule.case = 'PascalCase'
        oRule.prefix_exceptions.append('e_')

        lExpected = [2, 6, 14, 18, 26, 30, 42, 50, 54, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_suffix(self):
        oRule = entity.rule_008()
        oRule.case = 'PascalCase'
        oRule.suffix_exceptions.append('_a')

        lExpected = [2, 6, 14, 18, 26, 30, 34, 38, 42, 50, 54, 58, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_prefix_and_suffix(self):
        oRule = entity.rule_008()
        oRule.case = 'PascalCase'
        oRule.prefix_exceptions.append('e_')
        oRule.suffix_exceptions.append('_a')

        lExpected = [2, 6, 14, 18, 26, 30, 34, 38, 42, 50, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_008_PascalCase_with_whole_exception(self):
        oRule = entity.rule_008()
        oRule.case = 'PascalCase'
        oRule.case_exceptions.append('myFifo')

        lExpected = [2, 6, 14, 18, 22, 30, 34, 38, 42, 50, 54, 58, 62, 66]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

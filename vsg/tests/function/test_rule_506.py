
import os
import unittest

from vsg.rules import function
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_506_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_506_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_lower_with_upper_prefix = []
lExpected_lower_with_upper_prefix.append('')
utils.read_file(os.path.join(sTestDir, 'rule_506_test_input.fixed_lower_with_upper_prefix.vhd'), lExpected_lower_with_upper_prefix)

lExpected_lower_with_upper_suffix = []
lExpected_lower_with_upper_suffix.append('')
utils.read_file(os.path.join(sTestDir, 'rule_506_test_input.fixed_lower_with_upper_suffix.vhd'), lExpected_lower_with_upper_suffix)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_506_test_input.fixed_upper.vhd'), lExpected_upper)

lExpected_upper_with_lower_prefix = []
lExpected_upper_with_lower_prefix.append('')
utils.read_file(os.path.join(sTestDir, 'rule_506_test_input.fixed_upper_with_lower_prefix.vhd'), lExpected_upper_with_lower_prefix)

lExpected_upper_with_lower_suffix = []
lExpected_upper_with_lower_suffix.append('')
utils.read_file(os.path.join(sTestDir, 'rule_506_test_input.fixed_upper_with_lower_suffix.vhd'), lExpected_upper_with_lower_suffix)


class test_function_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_506_lower(self):
        oRule = function.rule_506()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '506')

        lExpected = [6]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_506_lower_with_upper_prefix(self):
        oRule = function.rule_506()
        oRule.prefix_exceptions = []
        oRule.prefix_exceptions.append('F_')

        lExpected = [4, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_506_lower_with_upper_suffix(self):
        oRule = function.rule_506()
        oRule.suffix_exceptions = []
        oRule.suffix_exceptions.append('_F')

        lExpected = [4, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_506_upper(self):
        oRule = function.rule_506()
        oRule.case = 'upper'
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'function')
        self.assertEqual(oRule.identifier, '506')

        lExpected = [4]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_506_upper_with_lower_prefix(self):
        oRule = function.rule_506()
        oRule.case = 'upper'
        oRule.prefix_exceptions = []
        oRule.prefix_exceptions.append('f_')

        lExpected = [4, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_rule_506_upper_with_lower_suffix(self):
        oRule = function.rule_506()
        oRule.case = 'upper'
        oRule.suffix_exceptions = []
        oRule.suffix_exceptions.append('_f')

        lExpected = [4, 6]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_506_lower(self):
        oRule = function.rule_506()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_506_lower_with_upper_prefix(self):
        oRule = function.rule_506()
        oRule.prefix_exceptions = []
        oRule.prefix_exceptions.append('F_')

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower_with_upper_prefix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_506_lower_with_upper_suffix(self):
        oRule = function.rule_506()
        oRule.suffix_exceptions = []
        oRule.suffix_exceptions.append('_F')

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower_with_upper_suffix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_506_upper(self):
        oRule = function.rule_506()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_506_upper_with_lower_prefix(self):
        oRule = function.rule_506()
        oRule.case = 'upper'
        oRule.prefix_exceptions = []
        oRule.prefix_exceptions.append('f_')

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper_with_lower_prefix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_506_upper_with_lower_suffix(self):
        oRule = function.rule_506()
        oRule.case = 'upper'
        oRule.suffix_exceptions = []
        oRule.suffix_exceptions.append('_f')

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper_with_lower_suffix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


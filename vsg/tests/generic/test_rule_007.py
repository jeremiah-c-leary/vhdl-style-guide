
import os
import unittest

from vsg.rules import generic
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_007_test_input.vhd'))

lExpected_lower = []
lExpected_lower.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_lower.vhd'), lExpected_lower)

lExpected_lower_with_upper_prefix  = []
lExpected_lower_with_upper_prefix .append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_lower_with_upper_prefix.vhd'), lExpected_lower_with_upper_prefix)

lExpected_lower_with_upper_suffix  = []
lExpected_lower_with_upper_suffix .append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_lower_with_upper_suffix.vhd'), lExpected_lower_with_upper_suffix)

lExpected_lower_with_upper_prefix_and_suffix  = []
lExpected_lower_with_upper_prefix_and_suffix .append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_lower_with_upper_prefix_and_suffix.vhd'), lExpected_lower_with_upper_prefix_and_suffix)

lExpected_upper = []
lExpected_upper.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_upper.vhd'), lExpected_upper)

lExpected_upper_with_lower_prefix = []
lExpected_upper_with_lower_prefix.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_upper_with_lower_prefix.vhd'), lExpected_upper_with_lower_prefix)

lExpected_upper_with_lower_suffix = []
lExpected_upper_with_lower_suffix.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_upper_with_lower_suffix.vhd'), lExpected_upper_with_lower_suffix)

lExpected_upper_with_lower_prefix_and_suffix = []
lExpected_upper_with_lower_prefix_and_suffix.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_upper_with_lower_prefix_and_suffix.vhd'), lExpected_upper_with_lower_prefix_and_suffix)


class test_generic_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_007_lower(self):
        oRule = generic.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'generic')
        self.assertEqual(oRule.identifier, '007')

        lExpected = [4, 5, 6, 16, 17, 18, 28, 29, 30, 40, 41, 42, 66, 78, 90]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_lower(self):
        oRule = generic.rule_007()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_lower_with_upper_prefix(self):
        oRule = generic.rule_007()
        oRule.prefix_exceptions = ['PREFIX_']

        lExpected = [4, 5, 6, 16, 17, 18, 28, 29, 30, 40, 41, 42, 54, 78, 90]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_lower_with_upper_prefix(self):
        oRule = generic.rule_007()
        oRule.prefix_exceptions = ['PREFIX_']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower_with_upper_prefix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_lower_with_upper_suffix(self):
        oRule = generic.rule_007()
        oRule.suffix_exceptions = ['_SUFFIX']

        lExpected = [4, 5, 6, 16, 17, 18, 28, 29, 30, 40, 41, 42, 54, 66, 90]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_lower_with_upper_suffix(self):
        oRule = generic.rule_007()
        oRule.suffix_exceptions = ['_SUFFIX']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower_with_upper_suffix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_lower_with_upper_prefix_and_suffix(self):
        oRule = generic.rule_007()
        oRule.prefix_exceptions = ['PREFIX_']
        oRule.suffix_exceptions = ['_SUFFIX']

        lExpected = [4, 5, 6, 16, 17, 18, 28, 29, 30, 40, 41, 42, 54, 66, 78]

        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_lower_with_upper_prefix_and_suffix(self):
        oRule = generic.rule_007()
        oRule.prefix_exceptions = ['PREFIX_']
        oRule.suffix_exceptions = ['_SUFFIX']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_lower_with_upper_prefix_and_suffix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_upper(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'

        lExpected = [6, 18, 30, 51, 52, 53, 54, 63, 64, 65, 66, 75, 76, 77, 78, 87, 88, 89, 90]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_upper(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_upper_with_lower_prefix(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'
        oRule.prefix_exceptions = ['prefix_']

        lExpected = [6, 18, 42, 51, 52, 53, 54, 63, 64, 65, 66, 75, 76, 77, 78, 87, 88, 89, 90]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_upper_with_lower_prefix(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'
        oRule.prefix_exceptions = ['prefix_']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper_with_lower_prefix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
 
    def test_rule_007_upper_with_lower_suffix(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'
        oRule.suffix_exceptions = ['_suffix']

        lExpected = [6, 30, 42, 51, 52, 53, 54, 63, 64, 65, 66, 75, 76, 77, 78, 87, 88, 89, 90]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_upper_with_lower_suffix(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'
        oRule.suffix_exceptions = ['_suffix']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper_with_lower_suffix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
 
    def test_rule_007_upper_with_lower_prefix_and_suffix(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'
        oRule.prefix_exceptions = ['prefix_']
        oRule.suffix_exceptions = ['_suffix']

        lExpected = [18, 30, 42, 51, 52, 53, 54, 63, 64, 65, 66, 75, 76, 77, 78, 87, 88, 89, 90]
        oRule.analyze(self.oFile)
        self.assertEqual(utils.extract_violation_lines_from_violation_object(oRule.violations), lExpected)

    def test_fix_rule_007_upper_with_lower_prefix_and_suffix(self):
        oRule = generic.rule_007()
        oRule.case = 'upper'
        oRule.prefix_exceptions = ['prefix_']
        oRule.suffix_exceptions = ['_suffix']

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_upper_with_lower_prefix_and_suffix, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

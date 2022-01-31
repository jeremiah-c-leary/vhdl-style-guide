
import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_014_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_014_test_input.fixed.vhd'), lExpected)

lExpected_align_left_true_align_paren_false = []
lExpected_align_left_true_align_paren_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_014_test_input.fixed_align_left_true_align_paren_false.vhd'), lExpected_align_left_true_align_paren_false)


class test_constant_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_014(self):
        oRule = constant.rule_014()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '014')
        self.assertEqual(oRule.groups, ['alignment'])

        lExpected = [31, 34, 37]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_014(self):
        oRule = constant.rule_014()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_014_align_left_true_align_paren_false(self):
        oRule = constant.rule_014()
        oRule.align_left = "yes"
        oRule.align_paren = "no"

        lExpected = [7, 10, 31, 34, 37]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_014_align_left_true_align_paren_false(self):
        oRule = constant.rule_014()
        oRule.align_left = "yes"
        oRule.align_paren = "no"

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_align_paren_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

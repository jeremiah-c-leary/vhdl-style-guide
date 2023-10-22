
import os
import unittest

from vsg.rules import concurrent_selected_signal_assignment as Rule
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_400_test_input.vhd'))


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_400_yes_no_no_no_no(self):
        oRule = Rule.rule_400()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent_selected_signal_assignment')
        self.assertEqual(oRule.identifier, '400')

        lExpected = [12, 13, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_yes_no_no_no_no(self):
        oRule = Rule.rule_400()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed_yes_no_no_no_no.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(oRule.groups, ['alignment'])
        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400_no_no_no_no_no(self):
        oRule = Rule.rule_400()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent_selected_signal_assignment')
        self.assertEqual(oRule.identifier, '400')

        lExpected = [7, 8, 9, 12, 13, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))


    def test_fix_rule_400_no_no_no_no_no(self):
        oRule = Rule.rule_400()
        oRule.align_left = 'no'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'no'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed_no_no_no_no_no.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(oRule.groups, ['alignment'])
        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_400_yes_no_yes_no_no(self):
        oRule = Rule.rule_400()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent_selected_signal_assignment')
        self.assertEqual(oRule.identifier, '400')

        lExpected = [7, 8, 12, 12, 13, 13, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_400_yes_no_yes_no_no(self):
        oRule = Rule.rule_400()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.align_when_keywords = 'yes'
        oRule.wrap_at_when = 'no'
        oRule.align_else_keywords = 'no'

        oRule.fix(self.oFile)

        lExpected = []
        lExpected.append('')
        utils.read_file(os.path.join(sTestDir, 'rule_400_test_input.fixed_yes_no_yes_no_no.vhd'), lExpected)

        lActual = self.oFile.get_lines()

        self.assertEqual(oRule.groups, ['alignment'])
        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


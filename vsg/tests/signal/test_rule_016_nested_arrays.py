
import os
import unittest

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_016_test_input.nested_arrays.vhd'))

lExpected_array_first_paren_new_line_true = []
lExpected_array_first_paren_new_line_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.nested_arrays.fixed_array_first_paren_new_line_true.vhd'), lExpected_array_first_paren_new_line_true)

lExpected_array_first_paren_new_line_false = []
lExpected_array_first_paren_new_line_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.nested_arrays.fixed_array_first_paren_new_line_false.vhd'), lExpected_array_first_paren_new_line_false)

#lExpected_first_paren_new_line_false = []
#lExpected_first_paren_new_line_false.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_first_paren_new_line_false.vhd'), lExpected_first_paren_new_line_false)
#
#lExpected_last_paren_new_line_true = []
#lExpected_last_paren_new_line_true.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_last_paren_new_line_true.vhd'), lExpected_last_paren_new_line_true)
#
#lExpected_last_paren_new_line_false = []
#lExpected_last_paren_new_line_false.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_last_paren_new_line_false.vhd'), lExpected_last_paren_new_line_false)
#
#lExpected_last_paren_new_line_true_move_last_comment_true = []
#lExpected_last_paren_new_line_true_move_last_comment_true.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_last_paren_new_line_true_move_last_comment_true.vhd'), lExpected_last_paren_new_line_true_move_last_comment_true)
#
#lExpected_open_paren_new_line_true = []
#lExpected_open_paren_new_line_true.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_open_paren_new_line_true.vhd'), lExpected_open_paren_new_line_true)
#
#lExpected_open_paren_new_line_false = []
#lExpected_open_paren_new_line_false.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_open_paren_new_line_false.vhd'), lExpected_open_paren_new_line_false)
#
#lExpected_close_paren_new_line_true = []
#lExpected_close_paren_new_line_true.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_close_paren_new_line_true.vhd'), lExpected_close_paren_new_line_true)
#
#lExpected_close_paren_new_line_false = []
#lExpected_close_paren_new_line_false.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_close_paren_new_line_false.vhd'), lExpected_close_paren_new_line_false)
#
#lExpected_new_line_after_comma_true = []
#lExpected_new_line_after_comma_true.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_new_line_after_comma_true.vhd'), lExpected_new_line_after_comma_true)
#
#lExpected_new_line_after_comma_false = []
#lExpected_new_line_after_comma_false.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_new_line_after_comma_false.vhd'), lExpected_new_line_after_comma_false)

lExpected_all_true = []
lExpected_all_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_all_true.vhd'), lExpected_all_true)

#lExpected_all_false = []
#lExpected_all_false.append('')
#utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_all_false.vhd'), lExpected_all_false)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_016_array_first_open_paren_new_line_yes(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.array_first_paren_new_line = 'yes'
        oRule.ignore_single_line = 'no'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '016')

        lExpected = [16, 19, 25, 25]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_016_array_first_open_paren_new_line_yes(self):
        self.maxDiff = None
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.array_first_paren_new_line = 'yes'
        oRule.ignore_single_line = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_array_first_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_016_array_first_open_paren_new_line_no(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.array_first_paren_new_line = 'no'
        oRule.ignore_single_line = 'no'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '016')

        lExpected = [6, 10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_016_array_first_open_paren_new_line_no(self):
        self.maxDiff = None
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.array_first_paren_new_line = 'no'
        oRule.ignore_single_line = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_array_first_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

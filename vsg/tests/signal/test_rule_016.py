
import os
import unittest

from vsg.rules import signal
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_016_test_input.vhd'))

lExpected_first_paren_new_line_true = []
lExpected_first_paren_new_line_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_first_paren_new_line_true.vhd'), lExpected_first_paren_new_line_true)

lExpected_first_paren_new_line_false = []
lExpected_first_paren_new_line_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_first_paren_new_line_false.vhd'), lExpected_first_paren_new_line_false)

lExpected_last_paren_new_line_true = []
lExpected_last_paren_new_line_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_last_paren_new_line_true.vhd'), lExpected_last_paren_new_line_true)

lExpected_last_paren_new_line_false = []
lExpected_last_paren_new_line_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_last_paren_new_line_false.vhd'), lExpected_last_paren_new_line_false)

lExpected_last_paren_new_line_true_move_last_comment_true = []
lExpected_last_paren_new_line_true_move_last_comment_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_last_paren_new_line_true_move_last_comment_true.vhd'), lExpected_last_paren_new_line_true_move_last_comment_true)

lExpected_open_paren_new_line_true = []
lExpected_open_paren_new_line_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_open_paren_new_line_true.vhd'), lExpected_open_paren_new_line_true)

lExpected_open_paren_new_line_false = []
lExpected_open_paren_new_line_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_open_paren_new_line_false.vhd'), lExpected_open_paren_new_line_false)

lExpected_close_paren_new_line_true = []
lExpected_close_paren_new_line_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_close_paren_new_line_true.vhd'), lExpected_close_paren_new_line_true)

lExpected_close_paren_new_line_false = []
lExpected_close_paren_new_line_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_close_paren_new_line_false.vhd'), lExpected_close_paren_new_line_false)

lExpected_new_line_after_comma_true = []
lExpected_new_line_after_comma_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_new_line_after_comma_true.vhd'), lExpected_new_line_after_comma_true)

lExpected_new_line_after_comma_false = []
lExpected_new_line_after_comma_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_new_line_after_comma_false.vhd'), lExpected_new_line_after_comma_false)

lExpected_all_true = []
lExpected_all_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_all_true.vhd'), lExpected_all_true)

lExpected_all_false = []
lExpected_all_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input.fixed_all_false.vhd'), lExpected_all_false)


class test_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_first_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'yes'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        self.assertEqual(oRule.groups, ['structure'])

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'signal')
        self.assertEqual(oRule.identifier, '016')

        lExpected = [16]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_first_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'no'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [25, 32, 38, 44, 58, 70, 84, 95]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_last_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'yes'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [35, 39, 92]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_last_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'no'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [20, 29, 55, 65, 79, 104]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_open_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'yes'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [58, 58, 61]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_open_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'no'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [16, 25, 32, 38, 44, 45, 50, 70, 71, 75, 84, 85, 89, 95, 96, 100]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_close_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'yes'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [74, 78, 88, 92, 99, 103]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_close_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'no'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [49, 54, 61, 64]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_new_line_after_comma_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'yes'
        oRule.assign_on_single_line = 'ignore'

        lExpected = []
        lExpected.extend([39, 39, 61])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_new_line_after_comma_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'no'
        oRule.assign_on_single_line = 'ignore'

        lExpected = [17, 18]
        lExpected.extend([26, 27])
        lExpected.extend([33, 34])
        lExpected.extend([46, 47, 49, 51, 52])
        lExpected.extend([58, 59, 61, 62])
        lExpected.extend([72, 73, 74, 76, 77])
        lExpected.extend([86, 87, 88, 90, 91, 97, 98, 99, 101, 102])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

#    def test_rule_016_assign_on_single_line(self):
#        oRule = signal.rule_016()
#        oRule.first_paren_new_line = 'ignore'
#        oRule.last_paren_new_line = 'ignore'
#        oRule.open_paren_new_line = 'ignore'
#        oRule.close_paren_new_line = 'ignore'
#        oRule.new_line_after_comma = 'ignore'
#        oRule.assign_on_single_line = 'yes'
#
#        lExpected = [11, 16, 24, 31, 38, 45, 59, 71, 85, 97]
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_last_paren_new_line_true_move_last_comment_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'yes'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.move_last_comment = 'yes'

        lExpected = [35, 39, 92]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_last_paren_new_line_true_move_last_comment_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'yes'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.move_last_comment = 'no'

        lExpected = [35, 39, 92]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_rule_016_last_paren_new_line_false_move_last_comment_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.move_last_comment = 'yes'

        lExpected = []

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_first_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'yes'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_first_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'no'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_last_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'yes'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_last_paren_new_line_true_move_last_comment_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'yes'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.move_last_comment = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_last_paren_new_line_true_move_last_comment_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'yes'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.move_last_comment = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_true_move_last_comment_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_last_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'no'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_last_paren_new_line_false_move_last_comment_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'no'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'
        oRule.move_last_comment = 'yes'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_open_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'yes'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_open_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_open_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'no'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_open_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_close_paren_new_line_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'yes'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_close_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_close_paren_new_line_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'no'
        oRule.new_line_after_comma = 'ignore'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_close_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_new_line_after_comma_true(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma ='yes'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_comma_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_new_line_after_comma_false(self):
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'no'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_comma_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_all_true(self):
#        self.maxDiff = None
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'yes'
        oRule.last_paren_new_line = 'yes'
        oRule.open_paren_new_line = 'yes'
        oRule.close_paren_new_line = 'yes'
        oRule.new_line_after_comma = 'yes'
        oRule.assign_on_single_line = 'ignore'
        oRule.move_last_comment = 'yes'
        oRule.ignore_single_line = 'no'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    @unittest.skip('Skipping until rule is rewritten')
    def test_fix_rule_016_all_false(self):
#        self.maxDiff = None
        oRule = signal.rule_016()
        oRule.first_paren_new_line = 'no'
        oRule.last_paren_new_line = 'no'
        oRule.open_paren_new_line = 'no'
        oRule.close_paren_new_line = 'no'
        oRule.new_line_after_comma = 'no'
        oRule.assign_on_single_line = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

#    def test_fix_rule_016_assign_on_single_line(self):
#        self.maxDiff = None
#        oRule = signal.rule_016()
#        oRule.first_paren_new_line = 'yes'
#        oRule.last_paren_new_line = 'yes'
#        oRule.open_paren_new_line = 'yes'
#        oRule.close_paren_new_line = 'yes'
#        oRule.new_line_after_comma = 'yes'
#        oRule.assign_on_single_line = 'yes'
#
#        oFile = vhdlFile.vhdlFile(lFileAssignOnSingleLine)
#        oRule.fix(oFile)
#
#        lActual = oFile.get_lines()
#
#        self.assertEqual(lExpected_assign_on_single_line, lActual)
#
#        oRule.analyze(oFile)
#        self.assertEqual(oRule.violations, [])
#

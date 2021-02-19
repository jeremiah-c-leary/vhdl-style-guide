
import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_016_test_input.vhd'))
lFileOthers, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, 'rule_016_test_input_others.vhd'))
lFileAssignment, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, 'rule_016_test_input_assignment.vhd'))
lFilePositional, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, 'rule_016_test_input_positional.vhd'))

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

lExpected_others = []
lExpected_others.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input_others.fixed.vhd'), lExpected_others)

lExpected_assignment = []
lExpected_assignment.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input_assignment.fixed.vhd'), lExpected_assignment)

lExpected_positional = []
lExpected_positional.append('')
utils.read_file(os.path.join(sTestDir, 'rule_016_test_input_positional.fixed.vhd'), lExpected_positional)


class test_constant_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_016_first_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'true'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '016')

        lExpected = [10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_first_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'false'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        lExpected = [14, 17, 21, 27, 41, 57]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_last_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'true'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        lExpected = [11, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_last_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'false'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        lExpected = [18, 24, 38, 54, 72]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_open_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'true'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        lExpected = [11, 11, 14, 14, 14, 17, 17, 17, 22, 23, 28, 33]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_open_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'false'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        lExpected = [10, 21, 27, 41, 42, 48, 57, 58, 65]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_close_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'true'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        lExpected = [11, 11, 14, 14, 17, 17, 22, 23, 32, 37, 47, 53]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_close_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'false'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        lExpected = [64, 71]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_new_line_after_comma_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'true'
        oRule.align_left = 'ignore'

        lExpected = []
        lExpected.extend([11, 11, 11, 11, 11, 11, 11, 11, 11])
        lExpected.extend([14, 14, 14, 14, 14, 14, 14, 14, 14])
        lExpected.extend([17, 17, 17, 17, 17, 17, 17, 17, 17])
        lExpected.extend([22, 22, 22, 22])
        lExpected.extend([23, 23, 23, 23])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_016_new_line_after_comma_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'false'
        oRule.align_left = 'ignore'

        lExpected = [22]
        lExpected.extend(range(28, 37))
        lExpected.extend(range(43, 48))
        lExpected.extend(range(49, 53))
        lExpected.extend(range(59, 63))
        lExpected.append(64)
        lExpected.extend(range(66, 70))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_016_first_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'true'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_first_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'false'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_last_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'true'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_last_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'false'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_open_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'true'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_open_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_open_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'false'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_open_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_close_paren_new_line_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'true'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_close_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_close_paren_new_line_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'false'
        oRule.new_line_after_comma = 'ignore'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_close_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_new_line_after_comma_true(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma ='true'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_comma_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_new_line_after_comma_false(self):
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'ignore'
        oRule.last_paren_new_line = 'ignore'
        oRule.open_paren_new_line = 'ignore'
        oRule.close_paren_new_line = 'ignore'
        oRule.new_line_after_comma = 'false'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_new_line_after_comma_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_all_true(self):
#        self.maxDiff = None
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'true'
        oRule.last_paren_new_line = 'true'
        oRule.open_paren_new_line = 'true'
        oRule.close_paren_new_line = 'true'
        oRule.new_line_after_comma = 'true'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_all_false(self):
#        self.maxDiff = None
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'false'
        oRule.last_paren_new_line = 'false'
        oRule.open_paren_new_line = 'false'
        oRule.close_paren_new_line = 'false'
        oRule.new_line_after_comma = 'false'
        oRule.align_left = 'ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_all_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_others(self):
        self.maxDiff = None
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'true'
        oRule.last_paren_new_line = 'true'
        oRule.open_paren_new_line = 'true'
        oRule.close_paren_new_line = 'true'
        oRule.new_line_after_comma = 'true'

        oFileOthers = vhdlFile.vhdlFile(lFileOthers)
        oRule.fix(oFileOthers)

        lActual = oFileOthers.get_lines()

        self.assertEqual(lExpected_others, lActual)

        oRule.analyze(oFileOthers)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_assignment(self):
        self.maxDiff = None
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'true'
        oRule.last_paren_new_line = 'true'
        oRule.open_paren_new_line = 'true'
        oRule.close_paren_new_line = 'true'
        oRule.new_line_after_comma = 'true'

        oFileAssignment = vhdlFile.vhdlFile(lFileAssignment)
        oRule.fix(oFileAssignment)

        lActual = oFileAssignment.get_lines()

        self.assertEqual(lExpected_assignment, lActual)

        oRule.analyze(oFileAssignment)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_016_positional(self):
        self.maxDiff = None
        oRule = constant.rule_016()
        oRule.first_paren_new_line = 'true'
        oRule.last_paren_new_line = 'true'
        oRule.open_paren_new_line = 'true'
        oRule.close_paren_new_line = 'true'
        oRule.new_line_after_comma = 'ignore_positional'

        oFilePositional = vhdlFile.vhdlFile(lFilePositional)
        oRule.fix(oFilePositional)

        lActual = oFilePositional.get_lines()

        self.assertEqual(lExpected_positional, lActual)

        oRule.analyze(oFilePositional)
        self.assertEqual(oRule.violations, [])



import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_012a_test_input.vhd'))

lExpected_first_paren_new_line_true = []
lExpected_first_paren_new_line_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012a_test_input.fixed_first_paren_new_line_true.vhd'), lExpected_first_paren_new_line_true)

lExpected_first_paren_new_line_false = []
lExpected_first_paren_new_line_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012a_test_input.fixed_first_paren_new_line_false.vhd'), lExpected_first_paren_new_line_false)

lExpected_last_paren_new_line_true = []
lExpected_last_paren_new_line_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012a_test_input.fixed_last_paren_new_line_true.vhd'), lExpected_last_paren_new_line_true)

lExpected_last_paren_new_line_false = []
lExpected_last_paren_new_line_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012a_test_input.fixed_last_paren_new_line_false.vhd'), lExpected_last_paren_new_line_false)


class test_constant_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_012_first_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = True
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '012')

        lExpected = [10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_first_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = False
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        lExpected = [14, 17, 21, 27, 41, 57]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_last_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = True
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        lExpected = [11, 14]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_last_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = False
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        lExpected = [18, 24, 38, 54, 72]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_open_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = True
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        lExpected = [11, 11, 14, 14, 14, 17, 17, 17, 22, 23, 28, 33]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_open_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = False
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        lExpected = [10, 21, 27, 41, 42, 48, 57, 58, 65]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_close_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = True
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        lExpected = [11, 11, 14, 14, 17, 17, 22, 23, 32, 37, 47, 53]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_close_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = False
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        lExpected = [64, 71]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_new_line_after_comma_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = True
        oRule.align_left = 'Ignore'

        lExpected = []
        lExpected.extend([11, 11, 11, 11, 11, 11, 11, 11, 11])
        lExpected.extend([14, 14, 14, 14, 14, 14, 14, 14, 14])
        lExpected.extend([17, 17, 17, 17, 17, 17, 17, 17, 17])
        lExpected.extend([22, 22, 22, 22])
        lExpected.extend([23, 23, 23, 23])

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_rule_012_new_line_after_comma_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = False
        oRule.align_left = 'Ignore'

        lExpected = [22]
        lExpected.extend(range(28, 37))
        lExpected.extend(range(43, 48))
        lExpected.extend(range(49, 53))
        lExpected.extend(range(59, 63))
        lExpected.append(64)
        lExpected.extend(range(66, 70))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

#    def test_rule_012_align_left_true(self):
#        oRule = constant.rule_012()
#        oRule.first_paren_new_line = 'Ignore'
#        oRule.last_paren_new_line = 'Ignore'
#        oRule.open_paren_new_line = 'Ignore'
#        oRule.close_paren_new_line = 'Ignore'
#        oRule.new_line_after_comma = 'Ignore'
#        oRule.align_left = False
#
#        lExpected = []
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))
#
#    def test_rule_012_align_left_false(self):
#        oRule = constant.rule_012()
#        oRule.first_paren_new_line = 'Ignore'
#        oRule.last_paren_new_line = 'Ignore'
#        oRule.open_paren_new_line = 'Ignore'
#        oRule.close_paren_new_line = 'Ignore'
#        oRule.new_line_after_comma = 'Ignore'
#        oRule.align_left = False
#
#        lExpected = [22]
#        lExpected.extend(range(28, 37))
#        lExpected.extend(range(43, 48))
#        lExpected.extend(range(49, 53))
#        lExpected.extend(range(59, 63))
#        lExpected.append(64)
#        lExpected.extend(range(66, 70))
#
#        oRule.analyze(self.oFile)
#        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_first_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = True
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_first_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = False
        oRule.last_paren_new_line = 'Ignore'
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_first_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_last_paren_new_line_true(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = True
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_last_paren_new_line_false(self):
        oRule = constant.rule_012()
        oRule.first_paren_new_line = 'Ignore'
        oRule.last_paren_new_line = False
        oRule.open_paren_new_line = 'Ignore'
        oRule.close_paren_new_line = 'Ignore'
        oRule.new_line_after_comma = 'Ignore'
        oRule.align_left = 'Ignore'

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_last_paren_new_line_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])


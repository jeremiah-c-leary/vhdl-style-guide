
import os
import unittest

from vsg.rules import constant
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_012_test_input.vhd'))

dIndentMap = utils.read_indent_file()

lExpected_align_left_true = []
lExpected_align_left_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_align_left_true.vhd'), lExpected_align_left_true)

lExpected_align_left_true_align_paren_true = []
lExpected_align_left_true_align_paren_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_align_left_true_align_paren_true.vhd'), lExpected_align_left_true_align_paren_true)

lExpected_align_left_false_align_paren_true = []
lExpected_align_left_false_align_paren_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_align_left_false_align_paren_true.vhd'), lExpected_align_left_false_align_paren_true)

lExpected_align_left_false_align_paren_true_indent_step_2 = []
lExpected_align_left_false_align_paren_true_indent_step_2.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_align_left_false_align_paren_true_indent_step_2.vhd'), lExpected_align_left_false_align_paren_true_indent_step_2)

lExpected_align_left_true_indent_step_2 = []
lExpected_align_left_true_indent_step_2.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_align_left_true_indent_step_2.vhd'), lExpected_align_left_true_indent_step_2)


class test_constant_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_012_align_left_false_align_paren_true(self):
        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.indentSize = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '012')
        self.assertEqual(oRule.groups, ['alignment'])

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 39))
        lExpected.extend(range(41, 55))
        lExpected.extend(range(57, 73))
        lExpected.extend(range(79, 95))
        lExpected.extend(range(104, 109))
        lExpected.extend(range(115, 126))
        lExpected.extend(range(128, 134))
        lExpected.extend(range(136, 139))
        lExpected.extend(range(141, 153))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_false_align_paren_true(self):
        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.indentSize = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_false_align_paren_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_align_left_false_align_paren_true_indent_step_2(self):
        oRule = constant.rule_012()
        oRule.align_left = 'no'
        oRule.align_paren = 'yes'
        oRule.indentSize = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_false_align_paren_true_indent_step_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_true_align_paren_false(self):
        oRule = constant.rule_012()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.indentSize = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '012')

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 39))
        lExpected.extend(range(41, 55))
        lExpected.extend(range(57, 73))
        lExpected.extend(range(79, 95))
        lExpected.extend(range(104, 108))
        lExpected.extend(range(115, 126))
        lExpected.extend(range(128, 134))
        lExpected.extend(range(136, 139))
        lExpected.extend(range(141, 153))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_true_align_paren_false(self):
#        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.indentSize = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_true_align_paren_true(self):
        oRule = constant.rule_012()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.indentSize = 1
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '012')

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 39))
        lExpected.extend(range(41, 55))
        lExpected.extend(range(57, 73))
        lExpected.extend(range(79, 95))
        lExpected.extend(range(104, 108))
        lExpected.extend(range(115, 126))
        lExpected.extend(range(128, 134))
        lExpected.extend(range(136, 139))
        lExpected.extend(range(141, 153))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_true_align_paren_true(self):
#        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = 'yes'
        oRule.align_paren = 'yes'
        oRule.indentSize = 1

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_align_paren_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_align_left_true_indent_step_2(self):
#        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = 'yes'
        oRule.align_paren = 'no'
        oRule.indentSize = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_indent_step_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

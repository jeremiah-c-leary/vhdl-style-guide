
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

lExpected_align_left_false = []
lExpected_align_left_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_align_left_false.vhd'), lExpected_align_left_false)

lExpected_align_left_true_indent_step_2 = []
lExpected_align_left_true_indent_step_2.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed_align_left_true_indent_step_2.vhd'), lExpected_align_left_true_indent_step_2)


class test_constant_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)
        self.oFile.set_indent_map(dIndentMap)

    def test_rule_012_align_left_false(self):
        oRule = constant.rule_012()
        oRule.align_left = False
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'constant')
        self.assertEqual(oRule.identifier, '012')

        lExpected = []
        lExpected.append(11)
        lExpected.append(14)
        lExpected.append(17)
        lExpected.append(18)
        lExpected.extend(range(21, 25))
        lExpected.extend(range(27, 39))
        lExpected.extend(range(41, 55))
        lExpected.extend(range(57, 73))
        lExpected.extend(range(79, 95))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_false(self):
        oRule = constant.rule_012()
        oRule.align_left = False

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_012_align_left_true(self):
        oRule = constant.rule_012()
        oRule.align_left = True
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

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012_align_left_true(self):
#        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_fix_rule_012_align_left_true_indent_step_2(self):
#        self.maxDiff = None
        oRule = constant.rule_012()
        oRule.align_left = True
        oRule.indent_step = 2

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_align_left_true_indent_step_2, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

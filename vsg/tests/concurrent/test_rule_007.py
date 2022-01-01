
import os
import unittest

from vsg.rules import concurrent
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_007_test_input.vhd'))

lExpected_true = []
lExpected_true.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_true.vhd'), lExpected_true)

lExpected_false = []
lExpected_false.append('')
utils.read_file(os.path.join(sTestDir, 'rule_007_test_input.fixed_false.vhd'), lExpected_false)


class test_concurrent_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_007_w_allow_single_line_false(self):
        oRule = concurrent.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '007')
        self.assertEqual(oRule.groups, ['structure'])

        lExpected = [8, 18, 18, 18, 20, 20, 21, 23, 24, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007_w_allow_single_line_false(self):
        oRule = concurrent.rule_007()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_false, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])

    def test_rule_007_w_allow_single_line_true(self):
        oRule = concurrent.rule_007()
        oRule.allow_single_line = True
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'concurrent')
        self.assertEqual(oRule.identifier, '007')

        lExpected = [18, 18, 18, 20, 20, 21, 23, 24, 24]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007_w_allow_single_line_true(self):
        oRule = concurrent.rule_007()
        oRule.allow_single_line = True

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected_true, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
